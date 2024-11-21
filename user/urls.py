from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Password reset views
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='user/password_reset.html'), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='user/password_reset_done.html'), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='user/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='user/password_reset_complete.html'), name='password_reset_complete'),

    path('profile/', views.profile, name='profile'),  # Profile page URL

    # Email reset view (added this line)
    path('reset_email/', views.reset_email, name='reset_email'),  # URL to reset/change the email
]