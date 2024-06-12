from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.apps import UsersConfig
from users.views import RegisterView, ProfileView, Verify, RestoreView, UserListView, UpdateView, UserDetailView

app_name = UsersConfig.name

urlpatterns = [
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('list/', UserListView.as_view(), name='list'),
    path('detail/<int:pk>/', UserDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', UpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', ProfileView.as_view(), name='delete'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('verify/', Verify.as_view(), name='verify'),
    path('recovery/', RestoreView.as_view(), name='recovery')
]