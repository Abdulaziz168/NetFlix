from django.db import models
from django.forms import SlugField
from django.utils import timezone
from django.utils.text import slugify
from django.db.models.signals import pre_save
from djangoflix.db.models import PublishStateOptions
from djangoflix.db.recivers import publish_state_pre_save,slugify_pre_save
from videos.models import Video

class PlaylistQuerySet(models.QuerySet):
    def published (self):
        now = timezone.now()
        return self.filter(
            state= PublishStateOptions.PUBLISH,
            publish_timestamp__lte=now
            )

class PlaylistManager(models.Manager):
    def get_queryset(self):
        return PlaylistQuerySet(self.model,using=self._db)

    def published(self):
        return self.get_queryset().published()


# I stopped at the Using Django Signals lesson



# Create your models here.
class Playlist(models.Model):
    title  = models.CharField(max_length=255)
    describtion = models.TextField(blank=True,null=True)
    slug = models.SlugField(blank=True,null=True) 
    video = models.ForeignKey(Video) #### one video per playlist
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    state = models.CharField(max_length=2,choices=PublishStateOptions.choices,default=PublishStateOptions.DRAFT)
    publish_timestamp = models.DateTimeField(auto_now_add=False,auto_now=False,blank=True,null=True)

    objects = PlaylistManager()

    @property
    def is_published(self):
        return self.active

    def save(self,*args,**kwargs):

        if self.slug is None:
            self.slug = slugify(self.title)
        super().save(*args,**kwargs)




pre_save.connect(publish_state_pre_save,sender=Playlist)
pre_save.connect(slugify_pre_save,sender=Playlist)
