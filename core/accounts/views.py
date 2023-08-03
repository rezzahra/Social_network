from django.views import generic, View
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm, ProfileForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Profile, CustomUserModel, Follow
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from home.models import Post
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.contrib import messages

# Create your views here.


class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('accounts:login')


class ProfileView(LoginRequiredMixin, generic.DetailView):
    model = Profile
    template_name = 'accounts/profile_user.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']
        user = CustomUserModel.objects.get(id=pk)
        context['user'] = Profile.objects.get(user=user)
        context['posts']= Post.objects.filter(user=user)
        context['is_following'] = Follow.objects.filter(from_user = self.request.user, to_user = user).exists()
        return context


class EditProfileView(LoginRequiredMixin, generic.UpdateView):
    model = Profile
    fields = ['first_name', 'description', ]
    template_name = 'accounts/profile_form.html'

    def dispatch(self, request, *args, **kwargs):
        profile= get_object_or_404(Profile, pk=kwargs['pk'])
        if request.user.id != profile.user.id :
            return HttpResponseRedirect("/")
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        pk = self.kwargs["pk"]
        return reverse_lazy("profile", kwargs={"pk": pk})


class UserFollowView(LoginRequiredMixin, View):
    def get(self, request, pk):
        user = CustomUserModel.objects.get(id=pk)
        follow_user = Follow.objects.filter(from_user = request.user, to_user = user).exists()
        if follow_user :
            messages.error(request, 'you are already following this user', 'danger')
        else:
            Follow(from_user = request.user, to_user = user).save()
            messages.error(request, 'you followed this user', 'success')
        return redirect('profile', user.id )


class UserUnFollowView(LoginRequiredMixin, View):
    def get(self, request, pk):
        user = CustomUserModel.objects.get(id=pk)
        follow_user = Follow.objects.filter(from_user = request.user, to_user = user)
        if follow_user.exists() :
            follow_user.delete()
            messages.error(request, 'you unfollowed this user', 'success')
        else:
            messages.error(request, 'you are not following this user', 'danger')
        return redirect('profile', user.id )

