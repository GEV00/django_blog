# Generated by Django 2.2 on 2022-06-29 09:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog_board', '0007_auto_20220628_1732'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModerComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(default='', max_length=200, verbose_name='Комментарий от модератора')),
            ],
            options={
                'db_table': 'Комментарий модератора',
            },
        ),
        migrations.AddField(
            model_name='blogs',
            name='moder_comment',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='moder_com', to='blog_board.ModerComment', verbose_name='Комментарий от модератора'),
        ),
    ]
