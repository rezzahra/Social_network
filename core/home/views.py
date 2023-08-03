from django.shortcuts import redirect
from django.views import View, generic
from .models import Post
from accounts.models import CustomUserModel, Profile
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.contrib import messages
from .forms import PostCreateUpdateForm
from django.utils.text import slugify

# Create your views here.

# class HomeView(View):
#     def get (self, request):
#         return render(request, 'home/index.html')
class HomeView(generic.ListView):
    model = Post
    template_name = 'home/index.html'
    context_object_name = 'posts'


class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'home/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']
        user = Post.objects.get(id=pk).user
        profile = user.users.get(user=user)
        context['profile'] = profile
        return context


class PostDeletView(generic.DeleteView):
    model = Post
    success_url = reverse_lazy('home:home')

    def get(self, request, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs['pk'])
        if request.user.id != post.user.id :
            messages.error(request, 'you cant dell this post', 'danger')
            return redirect('home:home')
        return super().get(request, *args, **kwargs)


class PostUpdateView(generic.UpdateView):
    model = Post
    form_class = PostCreateUpdateForm
    template_name = 'home/post_form.html'

    def dispatch(self, request, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs['pk'])
        if request.user.id != post.user.id :
            messages.error(request, 'you cant update this post', 'danger')
            return redirect('home:home')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.slug =slugify(form.cleaned_data['body'][:30])
        return super(PostUpdateView, self).form_valid(form)


class PostCreateView(generic.CreateView):
    model = Post
    form_class = PostCreateUpdateForm
    template_name = 'home/post_form.html'

    def form_valid(self, form):
        form.instance.slug = slugify(form.cleaned_data['body'][:30])
        form.instance.user = self.request.user
        return super().form_valid(form)
