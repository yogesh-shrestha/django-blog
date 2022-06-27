from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, TemplateView, DetailView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from blog.models import Profile
from .forms import RegisterForm, UserSettingForm, PasswordResetForm, UserProfileForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from .models import User
from django.shortcuts import redirect




class UserRegisterView(CreateView):
    form_class = RegisterForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("login")

    
class UserEditView(UpdateView):
    form_class = UserSettingForm
    template_name = "registration/edit_settings.html"
    success_url = reverse_lazy("blog:index")

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_object(self):
        return self.request.user


class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordResetForm
    template_name = "registration/password_change.html"
    success_url = reverse_lazy("core:password-success")

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class PasswordSuccessView(TemplateView):
    template_name = "registration/password_success.html"


class ProfilePageView(TemplateView):
    model = Profile
    template_name = "registration/user_profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = get_object_or_404(Profile, user_id=self.kwargs.get('pk'))
        context['profile'] = profile
        return context


class EditProfileView(UpdateView):
    form_class = UserProfileForm
    # model = Profile
    template_name = "registration/edit_profile_page.html"
    success_url = reverse_lazy('blog:index')
    # fields = ['bio', 'profile_image', 'facebook_url', 'twiiter_url', 'instagram_url', 'linkedin_url', 'pinterest_url']
    
    def get_object(self):
        return self.request.user.profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.profile is not None:
            context['access'] = (self.kwargs.get('pk') == self.request.user.profile.id)
        return context



