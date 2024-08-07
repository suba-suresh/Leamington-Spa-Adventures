from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm, PostForm, CommentForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .models import Post, Comment, Like, Draft
from django.core.paginator import Paginator
from django.http import JsonResponse, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
import json
import logging
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.http import HttpResponse
from django.conf import settings
from .email_utils import notify_admin_post_created
from django.utils.text import slugify  


logger = logging.getLogger(__name__)

def index(request):
    return render(request, 'index.html')

def blog_list(request):
    post_list = Post.objects.all()
    post_list = Post.objects.filter(status='approved').order_by('-created_at')
    paginator = Paginator(post_list, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    status = request.GET.get('status', 'pending')  # Default to 'pending' if no status is provided

    print(post_list)  # Print to console for debugging
    
    context = {
        'post_list': page_obj.object_list,
        'page_obj': page_obj,
        'is_paginated': page_obj.has_other_pages(),
    }
    return render(request, 'blogs.html', context)

@login_required
def populate_slugs(request):
    posts_without_slugs = Post.objects.filter(slug__exact='')
    for post in posts_without_slugs:
        post.slug = slugify(post.title)
        post.save()
        logger.debug(f'Populated slug for post: {post.title} with slug: {post.slug}')
    return HttpResponse("Slugs populated successfully.")

    
@login_required
def full_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if post.status != 'approved' and not request.user.is_staff:
        return HttpResponseForbidden("You don't have permission to view this post.")
    
    likes_count = Like.objects.filter(post=post).count()
    comments = Comment.objects.filter(post=post)
    user_has_liked = Like.objects.filter(post=post, user=request.user).exists()

    context = {
        'post': post,
        'likes_count': likes_count,
        'comments': comments,
        'user_has_liked': user_has_liked,
    }
    return render(request, 'full_post.html', context)

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Signup successful!')
            user = authenticate(username=user.username, password=form.cleaned_data['password1'])
            if user is not None:
                auth_login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Signup failed. Please try again.')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                messages.success(request, 'Logged in successfully!')
                return redirect('user_account')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Login failed. Please try again.')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    auth_logout(request)
    messages.success(request, 'Logged out successfully!')
    return redirect('index')

@login_required
def user_account(request):
    user_posts = Post.objects.filter(author=request.user)
    return render(request, 'user_account.html', {'user_posts': user_posts})

@login_required
def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            if not post.slug:
                post.slug = slugify(post.title)
            post.save()
            notify_admin_post_created(post)
            messages.success(request, 'Post added successfully and is pending approval!')
            return redirect('user_account')
        else:
            messages.error(request, 'Failed to add post. Please try again.')
    else:
        form = PostForm()
    return render(request, 'posts/add_post.html', {'form': form})

@login_required
def edit_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.user != post.author and not (request.user.is_staff and post.admin_editable):
        return HttpResponseForbidden("You don't have permission to edit this post.")
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post updated successfully!')
            return redirect('view_post', slug=post.slug)
        else:
            messages.error(request, 'Failed to update post. Please try again.')
    else:
        form = PostForm(instance=post)
    return render(request, 'posts/edit_post.html', {'form': form, 'post': post})

@login_required
def delete_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.user != post.author and not request.user.is_staff:
        return HttpResponseForbidden("You don't have permission to delete this post.")
    post.delete()
    messages.success(request, 'Post deleted successfully!')
    return redirect('user_account')

@login_required
def view_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    user_posts = Post.objects.filter(author=post.author).exclude(id=post.id)
    return render(request, 'posts/view_post.html', {'post': post, 'user_posts': user_posts})

@login_required
def like_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if post.author != request.user:
        like, created = Like.objects.get_or_create(user=request.user, post=post)
        if created:
            messages.success(request, 'You liked the post.')
        else:
            like.delete()
            messages.success(request, 'You unliked the post.')
        post.number_of_likes = Like.objects.filter(post=post).count()
        post.save()
    else:
        messages.error(request, 'You cannot like your own post.')
    return redirect('full_post', slug=slug)

@login_required
def comment_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            post.number_of_comments += 1
            post.save()
            messages.success(request, 'Comment added successfully!')
            return redirect('full_post', slug=slug)
        else:
            messages.error(request, 'Failed to add comment. Please try again.')
    else:
        form = CommentForm()
    return render(request, 'full_post.html', {'post': post, 'form': form})

@login_required
def add_comment(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            comment = Comment.objects.create(post=post, author=request.user, content=content)
            post.comments_count = post.comments.count()  # Update the comment count
            post.save()
            messages.success(request, 'Comment added successfully!')
    return redirect('full_post', slug=slug)
@user_passes_test(lambda u: u.is_superuser)

@login_required
def delete_comment(request, slug, id):
    post = get_object_or_404(Post, slug=slug)
    comment = get_object_or_404(Comment, id=id)
    comment.delete()
    post.number_of_comments -= 1
    post.save()
    messages.success(request, 'Comment deleted successfully!')
    return redirect('full_post', slug=slug)

@csrf_exempt
@login_required
def save_draft(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        title = data.get('title', '')
        content = data.get('content', '')
        draft, created = Draft.objects.get_or_create(author=request.user, title=title)
        draft.content = content
        draft.save()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'}, status=400)

@login_required
def view_drafts(request):
    drafts = Draft.objects.filter(author=request.user)
    return render(request, 'drafts/drafts.html', {'drafts': drafts})


@login_required
def edit_draft(request, id):
    draft = get_object_or_404(Draft, id=id)
    if request.method == 'POST':
        content = request.POST.get('content', '')
        if content:
            draft.content = content
            draft.save()
            messages.success(request, 'Draft updated successfully!')
            return redirect('draft_list')
    return render(request, 'drafts/edit_draft.html', {'draft': draft})


@login_required
def update_profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('user_account')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'update_profile.html', context)
    
@user_passes_test(lambda u: u.is_superuser)
def approve_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if post.status == 'pending':  # Assuming 'pending' is the status for unapproved posts
        post.status = 'approved'  # Change status to 'approved'
        post.save()
        messages.success(request, 'Post approved successfully!')
    else:
        messages.error(request, 'Post cannot be approved.')
    return redirect('admin_dashboard')  # Redirect to an admin dashboard or post list

@user_passes_test(lambda u: u.is_superuser)
def reject_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if post.status == 'pending':  # Assuming 'pending' is the status for unapproved posts
        post.status = 'rejected'  # Change status to 'rejected'
        post.save()
        messages.success(request, 'Post rejected successfully!')
    else:
        messages.error(request, 'Post cannot be rejected.')
    return redirect('admin_dashboard')  # Redirect to an admin dashboard or post list

def filter_posts_by_status(request, status):
    posts = Post.objects.filter(status=status)
    return render(request, 'posts/posts_by_status.html', {'posts': posts, 'status': status})

def send_test_email_view(request):
    try:
        send_mail(
            'Test Email Subject',
            'This is a test email body.',
            settings.DEFAULT_FROM_EMAIL,
            ['test@example.com'],
            fail_silently=False,
        )
        return HttpResponse("Test email sent successfully")
    except Exception as e:
        return HttpResponse(f"Failed to send email: {str(e)}")

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.status = 'pending'  # Default status for new posts
            post.save()
            notify_admin_post_created(post)
            messages.success(request, 'Your post has been submitted for review.')
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'posts/create_post.html', {'form': form})

def about(request):
    return render(request, 'about.html') 

def contact(request):
    return render(request, 'contact.html')