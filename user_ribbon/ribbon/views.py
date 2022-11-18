from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
    )
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    View,
    )
from ribbon.models import Post
from ribbon.forms import (
    UserRegisterForm
    )
from django.http import HttpResponse


class RegisterView(View):
    def get(self, request):
        template_name = 'ribbon/register.html'
        form = UserRegisterForm()
        return render(request, template_name, {'form': form})

    def post(self, request):
        form = UserRegisterForm(request.POST)
        print(form.errors.as_text)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Ваш аккаунт создан: можно войти на сайт.')
            return redirect('login')
        else:
            messages.error(request, 'Your account is disabled')
            return render(request, 'ribbon/register.html', {'form': form})

class PostListView(ListView):
    model = Post
    template_name = 'ribbon/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user-posts.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

