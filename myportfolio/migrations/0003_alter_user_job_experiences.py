# Generated by Django 5.0.6 on 2024-06-26 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myportfolio', '0002_alter_user_job_experiences'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='job_experiences',
            field=models.ManyToManyField(blank=True, to='myportfolio.jobexperience'),
        ),
    ]