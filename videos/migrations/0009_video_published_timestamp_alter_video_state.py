# Generated by Django 4.0.3 on 2022-03-06 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0008_video_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='published_timestamp',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='state',
            field=models.CharField(choices=[('PU', 'Published'), ('DR', 'Draft')], default='DR', max_length=2),
        ),
    ]
