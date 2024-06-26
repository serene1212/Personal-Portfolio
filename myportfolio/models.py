from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    live_link = models.URLField(null=True, blank=True)
    source_code_link = models.URLField()


class Skill(models.Model):
    name = models.CharField(max_length=255)
    proficiency = models.IntegerField(choices=[(i, i) for i in range(101)])


class Interest(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()


class JobExperience(models.Model):
    job_title = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField()


class Education(models.Model):
    degree = models.CharField(max_length=255)
    school_name = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    score = models.FloatField(blank=True, null=True)
    description = models.TextField()


class Course(models.Model):
    name = models.CharField(max_length=255)
    certificate = models.URLField(default=None, blank=True, null=True)


class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    bio = models.TextField()
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)

    profile_picture = models.ImageField(upload_to="static/img", default="profile.jpg")

    contact_email = models.EmailField()
    github_link = models.URLField(blank=True)
    linkedin_link = models.URLField(blank=True)

    projects = models.ManyToManyField(Project)
    skills = models.ManyToManyField(Skill)
    interests = models.ManyToManyField(Interest)
    job_experiences = models.ManyToManyField(JobExperience, blank=True, null=True)
    educations = models.ManyToManyField(Education)
    courses = models.ManyToManyField(Course)


class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
