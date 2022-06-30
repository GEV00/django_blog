# Generated by Django 2.2 on 2022-06-30 12:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog_board', '0011_auto_20220630_1125'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPhotos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='post1', to='blog_board.Blogs', verbose_name='Публикация')),
            ],
            options={
                'db_table': 'Фото публикаций',
            },
        ),
    ]