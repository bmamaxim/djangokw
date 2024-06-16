from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from django.views.decorators.cache import cache_page

from users.apps import UsersConfig
from users.views import RegisterView, ProfileView, Verify, RestoreView, UserListView, UpdateView, UserDetailView, \
    toggle_activity

app_name = UsersConfig.name

urlpatterns = [
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('list/', cache_page(120)(UserListView.as_view()), name='list'),
    path('detail/<int:pk>/', UserDetailView.as_view(), name='detail'),
    path('activity/<int:pk>/', toggle_activity, name='activity'),
    path('delete/<int:pk>/', ProfileView.as_view(), name='delete'),
    path('profile/', cache_page(120)(ProfileView.as_view()), name='profile'),
    path('verify/', Verify.as_view(), name='verify'),
    path('recovery/', RestoreView.as_view(), name='recovery')
]