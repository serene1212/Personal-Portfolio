from django.db import models


class Projects(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    live_link = models.URLField()
    source_code_link = models.URLField()


class Skill(models.Model):
    name = models.CharField(max_length=255)
    proficiency = models.IntegerField(choices=[(i, i) for i in range(101)])


class WorkFlow(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()


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

    projects = models.ForeignKey(Projects, on_delete=models.DO_NOTHING)
    skills = models.ForeignKey(Skill, on_delete=models.DO_NOTHING)
    work_flows = models.ForeignKey(WorkFlow, on_delete=models.DO_NOTHING)
    interests = models.ForeignKey(Interest, on_delete=models.DO_NOTHING)
    job_experiences = models.ForeignKey(JobExperience, on_delete=models.DO_NOTHING)
    educations = models.ForeignKey(Education, on_delete=models.DO_NOTHING)
    courses = models.ForeignKey(Course, on_delete=models.DO_NOTHING)


class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
