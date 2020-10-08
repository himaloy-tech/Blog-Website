from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Contact, Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import UpdateView
from django.core.paginator import Paginator
# Create your views here.

login = lambda request: render(request, 'login.html')
logout = lambda request: render(request, 'logout.html')
signup = lambda request: render(request, 'signup.html')
test = lambda request: render(request, 'test.html')
def PostList(request):
    post = Post.objects.all()
    return render(request, 'home.html', {"blogs":post})

def PostDetail(request, post_id):
    details = Post.objects.filter(postid__icontains=post_id)
    return render(request, 'detail.html', {"Post":details})


@login_required(login_url='/login')
def PostCreate(request):
    if request.method == "POST":
        title = request.POST.get('title')
        body = request.POST.get('body')
        post = Post(title=title, body=body, user=request.user)
        post.save()
        return redirect('/')
    else:
        return render(request, 'create.html')

class PostUpdateView(UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'body']
    template_name = "create.html"
    success_url = reverse_lazy('home')
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        else:
            return False

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        details = Contact(name, email, subject, message)
        details.save()
    return render(request, 'contact.html')

@login_required(login_url='/login')
def profile(request):
    posts = Post.objects.filter(user__username__icontains=request.user.username).order_by('-pub_date')
    context = {
        'post':posts
    }
    return render(request, 'profile.html', context)