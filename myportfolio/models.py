from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    bio = models.TextField()
    profile_picture = models.ImageField(upload_to="media/img/profile_pictures", default="profile.jpg")
    contact_email = models.EmailField()
    github_link = models.URLField(blank=True)
    linkedin_link = models.URLField(blank=True)


class Projects(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    live_link = models.URLField()
    source_code_link = models.URLField()
