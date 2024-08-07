from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from taggit.managers import TaggableManager
from django.utils.text import slugify
from django.dispatch import receiver 
from django.db.models.signals import post_save
import random
from cloudinary.models import CloudinaryField

class Post(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    )
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = CloudinaryField('image')
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
        super(Post, self).save(*args, **kwargs)

    def generate_unique_slug(self):
        base_slug = slugify(self.title)
        slug = base_slug
        while Post.objects.filter(slug=slug).exists():
            slug = f"{base_slug}-{random.randint(1, 10000)}"
        return slug

    def get_likes_count(self):
        return self.like_set.count()

    def __str__(self):
        return self.title or 'Untitled Post'
    

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = CloudinaryField('image', null=True, blank=True)

    def __str__(self):
        return f'Comment by {self.author} on {self.post}'

class Like(models.Model):
    post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'post')

    def __str__(self):
        return f'{self.user} likes {self.post}'

class Draft(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title if self.title else 'Untitled Draft'

# Profile model definition
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_image = CloudinaryField('image', blank=True, null=True)

    def __str__(self):
         return f"{self.user.username} Profile" or " "

# Ensure that a Profile is created or updated when a User is created or updated
@receiver(post_save, sender=User)
def create_or_update_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    else:
        instance.profile.save()

# Optional: Ensure that a Profile is created for existing users who don't have one
def create_profiles_for_existing_users():
    for user in User.objects.all():
        if not hasattr(user, 'profile'):
            Profile.objects.create(user=user)

# Run this function manually if you have existing users who need profiles
# create_profiles_for_existing_users()