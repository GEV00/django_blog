# Generated by Django 2.2 on 2022-06-28 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_board', '0006_auto_20220628_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='is_active',
            field=models.IntegerField(choices=[(0, 'На рассмотрении'), (1, 'Одобрено'), (2, 'Неодобрено')], default=0, verbose_name='Одобрено модерацией'),
        ),
    ]
