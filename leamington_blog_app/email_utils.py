import logging
from django.core.mail import send_mail
from django.conf import settings

logger = logging.getLogger(__name__)

def notify_admin_post_created(post):
    """Notify the admin when a new post is submitted for approval."""
    subject = f"New Post Submitted: {post.title}"
    message = (
        f"{post.author.username} has submitted a new post titled '{post.title}' for approval.\n\n"
        f"Description:\n{post.description}\n\n"
        f"Please review it in the admin panel."
    )
    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [settings.ADMIN_EMAIL],  # Ensure you have this email set in settings
        fail_silently=False,
    )

def notify_user_post_status_change(post):
    """Notify the user when their post's status is changed."""
    subject = f"Your Post '{post.title}' Status Updated"
    if post.status == 'approved':
        message = f"Congratulations! Your post titled '{post.title}' has been approved by the admin."
    elif post.status == 'rejected':
        message = f"Sorry, your post titled '{post.title}' has been rejected by the admin.\n\nReason:\n{post.rejection_reason}"
    else:
        message = f"Your post titled '{post.title}' status has been updated to {post.get_status_display()}."

    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [post.author.email],
        fail_silently=False,
    )
