from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.views import UserCreateView, email_confirmation, PasswordRecoveryView

urlpatterns = [
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', UserCreateView.as_view(), name='register'),
    path('email-confirm/<str:token>/', email_confirmation, name='email'),
    path('password-reset/', PasswordRecoveryView.as_view(), name='password_reset'),

]
