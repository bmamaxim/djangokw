from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from blog.forms import BlogForms
from blog.models import Blog


class BlogCreateView(CreateView):
    model = Blog
    form_class = BlogForms
    success_url = reverse_lazy('blog:blog')


    def form_valid(self, form):
        self.object = form.save()
        self.object.seller = self.request.user
        self.object.save()

        return super().form_valid(form)


class BlogListView(ListView):
    model = Blog
    template_name = 'blog/home.html'

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(publication_sign=True)
        return queryset


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object()
        self.object.number_of_views += 1
        self.object.save()
        return self.object


class BlogUpdateView(UpdateView):
    model = Blog
    form_class = BlogForms

    def form_valid(self, form):
        self.object = form.save()
        self.object.seller = self.request.user
        self.object.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:detail', args=[self.kwargs.get('pk')])


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:blog')
