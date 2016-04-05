from django.db import models
from django.utils import timezone


class BaseModel(models.Model):
    date_added = models.DateTimeField(default=timezone.now)

    class Meta:
        abstract = True


class Channel(BaseModel):
    username = models.CharField(max_length=50)
    playlist_id = models.CharField(max_length=32)

    def __str__(self):
        return self.username


class Video(BaseModel):
    video_id = models.CharField(max_length=11)
    title = models.CharField(max_length=255)
    channel = models.ForeignKey(Channel)


class ChannelStatistics(BaseModel):
    total_view_count = models.IntegerField()
    subsciber_count = models.IntegerField()
    video_count = models.IntegerField()
    channel = models.ForeignKey(Channel)
    # date of last upload


class VideoStatistics(BaseModel):
    view_count = models.IntegerField()
    like_count = models.IntegerField()
    video = models.ForeignKey(Video)