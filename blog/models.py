from django.db import models
from django.utils import timezone
from django.conf import settings


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    publish_at = models.DateTimeField(null=True, blank=True)

    def publish(self):
        self.publish_at = timezone.now()
        self.save()

    def __str__(self):
        return self.title

