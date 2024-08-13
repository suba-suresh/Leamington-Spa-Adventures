from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.safestring import mark_safe 
from .models import Post, Comment, Like, Profile
from .forms import PostForm


class CustomUserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    
    def is_staff(self, obj):
        return "✓" if obj.is_staff else "✗"
    is_staff.short_description = 'Staff Status'
    is_staff.admin_order_field = 'is_staff'


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    form = PostForm
    list_display = ('title', 'author', 'slug', 'created_at', 'updated_at', 'status')
    search_fields = ('title', 'description', 'tags')
    list_filter = ('created_at', 'tags', 'status')
    prepopulated_fields = {'slug': ('title',)}
    actions = ['approve_posts', 'reject_posts']

    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user
        obj.save()
    

    def get_readonly_fields(self, request, obj=None):
        """Dynamically adjust readonly fields based on whether the post is being edited."""
        if obj:  # Editing an existing post
            return self.readonly_fields + ('status',)
        return self.readonly_fields

    def approve_posts(self, request, queryset):
        """Custom action to approve selected posts."""
        queryset.update(status='approved')
        self.message_user(request, "Selected posts have been approved.")

    def reject_posts(self, request, queryset):
        """Custom action to reject selected posts."""
        queryset.update(status='rejected')
        self.message_user(request, "Selected posts have been rejected.")

    approve_posts.short_description = "Approve selected posts"
    reject_posts.short_description = "Reject selected posts"

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'content', 'created_at')
    #readonly_fields = ('created_at', 'updated_at', 'author')  # Keep these fields read-only

    def save_model(self, request, obj, form, change):
        if not obj.author_id:  # If author is not set, use the current logged-in user
            obj.author = request.user
        obj.save()

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        return form


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'created_at')
    list_filter = ('created_at',)
    #readonly_fields = ('created_at', 'user')

    def save_model(self, request, obj, form, change):
        if not obj.user_id:
            obj.user = request.user
        obj.save()

    def render_change_form(self, request, context, add=False, change=False, form_url='', obj=None):
        if add and 'user' in context['adminform'].form.fields:
            context['adminform'].form.fields['user'].initial = request.user
        return super().render_change_form(request, context, add, change, form_url, obj)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'profile_image_display', 'created_at')
    search_fields = ('user__username', 'bio')
    #readonly_fields = ('created_at',)

    def profile_image_display(self, obj):
        if obj.profile_image and obj.profile_image.url != 'path/to/default/profile_image':
            return mark_safe(f'<img src="{obj.profile_image.url}" width="100" height="100"/>')
        return "No Image"

    profile_image_display.short_description = 'Profile Image'