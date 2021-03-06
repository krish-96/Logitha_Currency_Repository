from django.urls import path, include, re_path

from django.contrib.auth import views as auth_views
from .views import register_view, logout_view, login_view, profile_view

urlpatterns = [
    path('register/', register_view, name='register'),

    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),

    path('profile/', profile_view, name='profile'),

    path('password_change/',
         auth_views.PasswordChangeView.as_view(template_name='password_change_form.html'),
         name='password_change'
         ),
    path(
        'password_change/done/',
        auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'),
        name='password_change_done'
    ),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset_form.html'),
         name='reset_password'),
    path(
        'password_reset/done/',
        auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
        name='password_reset_done'
    ),
    path(
        'reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
        name='password_reset_confirm'
    ),
    path(
        'reset/done/',
        auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
        name='password_reset_complete'
    ),

]
