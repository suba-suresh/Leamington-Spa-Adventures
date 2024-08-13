from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from taggit.managers import TaggableManager
from django.utils.text import slugify
from django.dispatch import receiver 
from django.db.models.signals import post_save
import random

class Post(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    )
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = CloudinaryField('image', blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    tags = TaggableManager()
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    number_of_likes = models.PositiveIntegerField(default=0)
    number_of_comments = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.generate_unique_slug()
        super().save(*args, **kwargs)

    def generate_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        num = 1
        while Post.objects.filter(slug=unique_slug).exists():
            unique_slug = f"{slug}-{num}"
            num += 1
        return unique_slug

    def update_likes_count(self):
        self.number_of_likes = Like.objects.filter(post=self).count()
        self.save()

    def update_comments_count(self):
        self.number_of_comments = Comment.objects.filter(post=self).count()
        self.save()

    def __str__(self):
        return self.title or "Untitled Post"

    def get_image_url(self):
        return self.image.url if self.image else 'path/to/default/image.jpg'

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.post.update_comments_count()  # Update count after saving a comment

    def delete(self, *args, **kwargs):
        post = self.post
        super().delete(*args, **kwargs)
        post.update_comments_count()  # Update count after deleting a comment


    def __str__(self):
        return f'Comment by {self.author} on {self.post}'

class Like(models.Model):
    post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'post')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.post.update_likes_count()  # Update count after saving a like

    def delete(self, *args, **kwargs):
        post = self.post
        super().delete(*args, **kwargs)
        post.update_likes_count()  # Update count after deleting a like

    def __str__(self):
        return f'{self.user} likes {self.post}'


# Profile model definition
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True)
    profile_image = CloudinaryField('image', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return self.user.username

    def get_image_url(self):
        if self.profile_image:
            return self.profile_image.url
        else:
            return 'path/to/default/profile_image.jpg'


# Ensure that a Profile is created or updated when a User is created or updated
@receiver(post_save, sender=User)
def create_or_update_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
