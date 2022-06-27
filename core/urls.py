from django.urls import path
from . import views


app_name = 'core'
urlpatterns = [
    path('register/', views.UserRegisterView.as_view(), name='register'),
    path('edit-profile/', views.UserEditView.as_view(), name='edit-profile'),
    # path('password/', auth_views.PasswordChangeView.as_view(template_name="registration/change_password.html"), name='password')
    path('password-change/', views.PasswordsChangeView.as_view(), name='password-change'),
    path('password-success/', views.PasswordSuccessView.as_view(), name='password-success'),
    path('<int:pk>/profile/', views.ProfilePageView.as_view(), name='user-profile'),
    path('<int:pk>/edit-profile/', views.EditProfileView.as_view(), name='edit-profile'),
] 