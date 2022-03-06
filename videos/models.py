import re
from django.db import models
from django.forms import SlugField
from django.utils import timezone
from django.utils.text import slugify
from django.db.models.signals import pre_save


class VideoQuerySet(models.QuerySet):
    def published (self):
        now = timezone.now()
        return self.filter(
            state= PublishStateOptions.PUBLISH,
            publish_timestamp__lte=now
            )

class VideoManager(models.Manager):
    def get_queryset(self):
        return VideoQuerySet(self.model,using=self._db)

    def published(self):
        return self.get_queryset().published()


# I stopped at the Using Django Signals lesson


class PublishStateOptions(models.TextChoices):
        #CONSTANT = DB_VALUE,USER_DISPLAY_VA
        PUBLISH = 'PU', 'Published'
        DRAFT = 'DR', 'Draft'
        # UNLISTED = 'UN','Unlisted'
        # Private = 'PR','Private'
# Create your models here.
class Video(models.Model):
    title  = models.CharField(max_length=255)
    describtion = models.TextField(blank=True,null=True)
    slug = models.SlugField(blank=True,null=True) # This-is-my-video
    video_id = models.CharField(max_length=200, unique=True)
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    state = models.CharField(max_length=2,choices=PublishStateOptions.choices,default=PublishStateOptions.DRAFT)
    publish_timestamp = models.DateTimeField(auto_now_add=False,auto_now=False,blank=True,null=True)

    objects = VideoManager()

    @property
    def is_published(self):
        return self.active

    def save(self,*args,**kwargs):

        if self.slug is None:
            self.slug = slugify(self.title)
        super().save(*args,**kwargs)

class VideoAllProxy(Video):
    class Meta:
        proxy = True
        verbose_name = 'All Video'
        verbose_name_plural = 'All Videos'

class VideoPublishedProxy(Video):
    class Meta:
        proxy = True
        verbose_name = 'Published Video'
        verbose_name_plural = 'Published Videos'

def publish_state_pre_save(sender,instance,*args,**kwargs):

    is_publish = instance.state==PublishStateOptions.PUBLISH
    is_drafr = instance.state ==PublishStateOptions.DRAFT
    if is_publish and instance.publish_timestamp is None:
        instance.publish_timestamp=timezone.now()
    elif is_drafr:
        instance.publish_timestamp==None

pre_save.connect(publish_state_pre_save,sender=Video)
