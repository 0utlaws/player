from django.urls import path

from . import views

app_name = 'accounts'

urlpatterns = [
    path('sign_up/', views.SignUpView.as_view(), name='sign-up'),
    path('sign_in/', views.SignInView.as_view(), name='sign-in'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('change_password/', views.ChangePasswordView.as_view(), name='change-password'),
    path('password_reset/', views.PasswordResetView.as_view(), name='password-reset'),
]
