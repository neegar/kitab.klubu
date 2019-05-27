from django.db import models
from django.contrib.auth.models import User
from next_month_app.models import Archive
#from django import datetime

# Create your models here.
class BookDiscussion(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    book = models.ForeignKey(Archive, on_delete = models.CASCADE)
    #date = models.DateField(_("Date"), default=datetime.date.today)
    comment = models.TextField()
    
