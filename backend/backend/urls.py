from django.contrib import admin
from django.urls import path
from login.views import UserRegistrationView, UserLoginView, UserDashboardView

urlpatterns = [
path('admin/', admin.site.urls),
path('register/', UserRegistrationView.as_view(), name='user_registration'),
path('login/', UserLoginView.as_view(), name='user_login'),
path('dashboard/', UserDashboardView.as_view(), name='dashboard'),
]

