# Generated by Django 4.0.3 on 2022-03-06 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0011_video_timestamp_video_update'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video_id',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
