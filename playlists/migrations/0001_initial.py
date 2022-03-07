# Generated by Django 4.0.3 on 2022-03-07 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('describtion', models.TextField(blank=True, null=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('active', models.BooleanField(default=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('state', models.CharField(choices=[('PU', 'Published'), ('DR', 'Draft')], default='DR', max_length=2)),
                ('publish_timestamp', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
