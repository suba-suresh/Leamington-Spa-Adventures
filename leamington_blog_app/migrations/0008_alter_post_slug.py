# Generated by Django 4.2.14 on 2024-08-06 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leamington_blog_app', '0007_post_admin_editable_post_status_alter_like_post_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, unique=True),
        ),
    ]