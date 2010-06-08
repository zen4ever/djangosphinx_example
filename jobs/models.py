from django.db import models
from djangosphinx.models import SphinxSearch
from tagging.fields import TagField

class Job(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    tags = TagField()
    latitude = models.FloatField()
    longitude = models.FloatField()

    search = SphinxSearch(
          index='jobs_job',
          weights={
              'title':100,
              'description':50,
              'tags': 70, 
         })
