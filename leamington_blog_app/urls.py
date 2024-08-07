from django.urls import path
from . import views
from .views import (
    index, signup, login_view, logout_view, user_account, add_post, about, contact, 
    view_post, edit_post, delete_post, blog_list, full_post, add_comment, 
    like_post, comment_post, save_draft, view_drafts, edit_draft, 
    update_profile, approve_post, reject_post, filter_posts_by_status
)


urlpatterns = [
    path('', index, name='index'),
    path('blogs/', blog_list, name='blogs'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('blogs/<slug:slug>/', full_post, name='full_post'),
    path('posts/<slug:slug>/like/', like_post, name='like_post'),
    path('blogs/<slug:slug>/comment/', comment_post, name='comment_post'),
    path('save_draft/', save_draft, name='save_draft'),
    path('accounts/signup/', signup, name='accounts_signup'),
    path('accounts/login/', login_view, name='accounts_login'),
    path('accounts/signout/', logout_view, name='accounts_signout'), 
    path('user-account/', user_account, name='user_account'), 
    path('posts/add/', add_post, name='add_post'),
    path('post/<slug:slug>/comment/add/', add_comment, name='add_comment'),
    path('posts/<slug:slug>/', view_post, name='view_post'),
    path('posts/<slug:slug>/edit/', edit_post, name='edit_post'),
    path('posts/<slug:slug>/delete/', delete_post, name='delete_post'),
    path('drafts/', view_drafts, name='drafts'),
    path('drafts/<int:id>/edit/', edit_draft, name='edit_draft'),
    path('update-profile/', update_profile, name='update_profile'),
    path('admin/posts/<slug:slug>/approve/', approve_post, name='approve_post'),
    path('admin/posts/<slug:slug>/reject/', reject_post, name='reject_post'),
    path('posts/<str:status>/', filter_posts_by_status, name='filter_posts_by_status'),
    path('populate-slugs/', views.populate_slugs, name='populate_slugs'),

]
