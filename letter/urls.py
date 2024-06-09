from django.urls import path

from letter.apps import LetterConfig
from letter.views import LetterCreateView, LetterUpdateView, LetterDeleteView, LetterDetailView, LetterListView

app_name = LetterConfig.name

urlpatterns = [
    path('create_letter/', LetterCreateView.as_view(), name='create_letter'),
    path('letters/', LetterListView.as_view(), name='letters'),
    path('letter/<int:pk>/', LetterDetailView.as_view(), name='letter'),
    path('letter_update/<int:pk>/', LetterUpdateView.as_view(), name='letter_update'),
    path('letter_delete/<int:pk>/', LetterDeleteView.as_view(), name='letter_delete'),
]