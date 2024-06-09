from django.urls import path

from mailing.apps import MailingConfig
from mailing.views import MailingLettersCreateView, MailingLettersListView, MailingLettersUpdateView, \
    MailingLettersDetailView, MailingLettersDeleteView

app_name = MailingConfig.name

urlpatterns = [
    path('mailings/', MailingLettersListView.as_view(), name='mailings'),
    path('create/', MailingLettersCreateView.as_view(), name='create'),
    path('update/<int:pk>/', MailingLettersUpdateView.as_view(), name='update'),
    path('mailing/<int:pk>/', MailingLettersDetailView.as_view(), name='mailing'),
    path('delete/<int:pk>/', MailingLettersDeleteView.as_view(), name='delete'),
]
