from django import forms

from blog.models import Blog


class BlogForms(forms.ModelForm):
    """
    Форма заполнения блга
    """

    class Meta:
        model = Blog
        fields = ('title', 'content', 'preview',)


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fild_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'