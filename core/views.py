from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Post, Comment, Like
from .forms import PostForm, CommentForm, UsernameChangeForm
from django.contrib import messages
from django.db.models import Q
from .forms import CustomSignupForm

# Signup View
def signup(request):
    if request.method == 'POST':
        form = CustomSignupForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()

            # SAVE PROFILE DATA
            profile = user.profile
            profile.date_of_birth = form.cleaned_data['date_of_birth']
            profile.address = form.cleaned_data['address']
            if form.cleaned_data.get('profile_picture'):
                profile.profile_picture = form.cleaned_data['profile_picture']
            profile.save()

            login(request, user)
            return redirect('feed')
    else:
        form = CustomSignupForm()
    
    return render(request, 'signup.html', {'form': form})

# Login View
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('feed')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


# Logout View
@login_required
def logout_view(request):
    logout(request)
    return redirect('login')


# Feed
def feed(request):
    posts = Post.objects.all().order_by('-created_at')  # newest first
    if request.user.is_authenticated:
        return render(request, 'feed.html', {'posts': posts})
    else:
        return render(request, 'guest_feed.html', {'posts': posts})
        # FIXED wrong template name


# Create Post
@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('feed')
    else:
        form = PostForm()

    return render(request, 'post_create.html', {'form': form})


# Delete Post
@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk, user=request.user)   # FIXED "post" → "Post"
    post.delete()
    return redirect('feed')


# Create Comment
@login_required
def comment_create(request, pk):
    post = get_object_or_404(Post, pk=pk)  # FIXED "post" → "Post"
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            return redirect('feed')
    else:
        form = CommentForm()

    return render(request, 'comment_create.html', {'form': form, 'post': post})


# Delete Comment
@login_required
def comment_delete(request, pk):
    comment = get_object_or_404(Comment, pk=pk, user=request.user)
    comment.delete()
    return redirect('feed')


# Like / Unlike
@login_required
def like(request, pk):
    post = get_object_or_404(Post, pk=pk)
    like_obj, created = Like.objects.get_or_create(
        user=request.user,
        post=post
    )
    if not created:
        like_obj.delete()  # Unlike

    return redirect('feed')


# User Profile
def user_profile(request, username):
    profile_user = get_object_or_404(User, username=username)
    posts = Post.objects.filter(user=profile_user)
    likes = Like.objects.filter(user=profile_user)

    context = {
        'profile_user': profile_user,
        'posts': posts,
        'likes': likes,
    }

    return render(request, 'user_profile.html', context)


# Guest User Profile
def guest_profile(request, username):
    profile_user = get_object_or_404(User, username=username)
    posts = Post.objects.filter(user=profile_user)
    return render(request, 'guest_profile.html', {
        'profile_user': profile_user,
        'posts': posts
    })


# Change Username
@login_required
def change_username(request):
    if request.method == "POST":
        form = UsernameChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)     # FIXED
            messages.success(request, 'Your username has been updated!')
            return redirect('user_profile', user.username)
    else:
        form = UsernameChangeForm(instance=request.user)

    return render(request, 'change_username.html', {'form': form})


# Search Users
def search_users(request):
    query = request.GET.get('q', '')

    users = User.objects.filter(
        Q(username__icontains=query) |
        Q(first_name__icontains=query) |
        Q(last_name__icontains=query)
    ) if query else []

    return render(request, 'search_users.html', {
        'users': users,
        'query': query
    })
