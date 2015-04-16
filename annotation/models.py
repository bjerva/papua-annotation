from django.db import models
import datetime

# Create your models here.

class Entry(models.Model):
    english_word = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')
   

    def was_published_today(self):
        return self.pub_date.date() == datetime.date.today()
    
    was_published_today.short_description = 'Published today?'

class Translation(models.Model):
    annotation = models.ForeignKey(Entry)
    foreign_word = models.CharField(max_length=100)
    #votes = models.IntegerField()
