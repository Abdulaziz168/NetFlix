# Generated by Django 4.0.3 on 2022-03-06 07:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0010_rename_published_timestamp_video_publish_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2022, 3, 6, 7, 58, 49, 942572, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='video',
            name='update',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
