from django.urls import path, reverse_lazy

from django.contrib.auth import views as auth_views

from . import views

app_name = 'accounts'

urlpatterns = [
    path('sign_up/', views.SignUpView.as_view(), name='sign-up'),
    path('sign_in/', views.SignInView.as_view(), name='sign-in'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('change_password/', views.ChangePasswordView.as_view(), name='change-password'),

    path('password_reset/', views.PasswordResetView.as_view(), name='password-reset'),

    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='accounts/password_reset_done.html'),
         name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name="accounts/password_reset_confirm.html",
        success_url=reverse_lazy('accounts:password_reset_complete')),
         name='password_reset_confirm'),

    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='accounts/password_reset_complete.html'),
         name='password_reset_complete'),
]
