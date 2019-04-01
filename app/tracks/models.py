from django.db import models

from django.contrib.auth import get_user_model
# Create your models here.


class Track(models.Model):
    # id will be created automatically
    title = models.CharField(max_length=50)
    # we make it optional by using blank=True
    description = models.TextField(blank=True)
    url = models.URLField()
    # It is automatically populated
    created_at = models.DateTimeField(auto_now_add=True)
    posted_by = models.ForeignKey(
        get_user_model(), null=True, on_delete=models.CASCADE)
