from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from blog.forms import BlogForms
from blog.models import Blog
from client.models import Client
from logmail.models import LogMail
from mailing.models import MailingLetters


class BlogCreateView(CreateView):
    model = Blog
    form_class = BlogForms
    success_url = reverse_lazy('blog:home')

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()

        return super().form_valid(form)


class BlogListView(ListView):
    model = Blog
    template_name = 'blog/home.html'

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(publication_sign=True)
        return queryset

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        # blog = Blog.objects.all()
        # print(blog[:3])
        # context_data['massage'] = blog[:3]
        context_data['title'] = 'Информация по рассылкам'
        context_data['mailings_all'] = len(LogMail.objects.all())
        context_data['mailings_started'] = len(MailingLetters.objects.filter(status='started'))
        context_data['mailings_clients'] = len(set(Client.objects.all()))
        return context_data


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object()
        self.object.number_of_views += 1
        self.object.save()
        return self.object


class BlogUpdateView(UserPassesTestMixin, UpdateView):
    model = Blog
    form_class = BlogForms

    def test_func(self):
        if self.get_object().owner == self.request.user:
            return True
        return self.handle_no_permission()

    def form_valid(self, form):
        self.object = form.save()
        self.object.seller = self.request.user
        self.object.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:detail', args=[self.kwargs.get('pk')])


class BlogDeleteView(UserPassesTestMixin, DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:home')

    def test_func(self):
        if self.get_object().owner == self.request.user:
            return True
        return self.handle_no_permission()
