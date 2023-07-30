from django.views import generic
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm, ProfileForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Profile
from django.urls import reverse_lazy
from django.shortcuts import redirect
# Create your views here.


class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('accounts:login')


class ProfileView(generic.DeleteView):
    model = Profile
    template_name = 'accounts/profile_user.html'
    context_object_name = 'user'


# class ProfileView(LoginRequiredMixin, generic.CreateView):
#     form_class = ProfileForm
#     template_name = 'accounts/profile_form.html'
#     context_object_name = 'form'
#



class EditProfileView(generic.UpdateView):
    model = Profile
    fields = ['first_name', 'description', ]
    template_name = 'accounts/profile_form.html'


