from django.db import models


class Projects(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    live_link = models.URLField()
    source_code_link = models.URLField()


class Skill(models.Model):
    PROFICIENCY_CHOICES = [(i, i) for i in range(1, 101)]
    name = models.CharField(max_length=255)
    proficiency = models.ImageField(choices=PROFICIENCY_CHOICES)


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
    skills = models.ManyToManyField(Skill)
    start_date = models.DateField()
    end_date = models.DateField()
    certificate = models.ImageField(upload_to="media/img/certificates", default=None, blank=True)


class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    bio = models.TextField()
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=12)

    profile_picture = models.ImageField(upload_to="static/img", default="profile.jpg")

    contact_email = models.EmailField()
    github_link = models.URLField(blank=True)
    linkedin_link = models.URLField(blank=True)

    projects = models.ForeignKey(Projects, on_delete=models.DO_NOTHING)
    skills = models.ForeignKey(Skill, on_delete=models.DO_NOTHING)
    job_experiences = models.ForeignKey(JobExperience, on_delete=models.DO_NOTHING)
    educations = models.ForeignKey(Education, on_delete=models.DO_NOTHING)
    courses = models.ForeignKey(Course, on_delete=models.DO_NOTHING)
