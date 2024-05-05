from django.urls import path

from client.apps import ClientConfig
from client.views import ClientListView, ClientCreateView

app_name = ClientConfig.name

urlpatterns = [
    path('', ClientListView.as_view(), name='home'),
    path('create', ClientCreateView.as_view(), name='create')
]