# Generated by Django 5.0.6 on 2024-06-26 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myportfolio', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='skills',
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(max_length=100),
        ),
    ]