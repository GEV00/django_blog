# Generated by Django 2.2 on 2022-07-05 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_board', '0013_auto_20220630_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogphotos',
            name='file',
            field=models.ImageField(upload_to='blog_photos/'),
        ),
    ]
