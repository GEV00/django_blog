# Generated by Django 4.1.1 on 2022-09-15 16:22

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_auth', '0007_remove_profile_email'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Profile',
            new_name='Profiles',
        ),
    ]
