# Generated by Django 5.0.6 on 2024-06-26 18:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myportfolio', '0002_remove_course_skills_alter_user_phone_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='course',
            name='start_date',
        ),
    ]
