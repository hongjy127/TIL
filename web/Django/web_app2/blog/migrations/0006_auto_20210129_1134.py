# Generated by Django 3.1.5 on 2021-01-29 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_read_cnt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='read_cnt',
        ),
        migrations.AddField(
            model_name='post',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]
