from django.db import models
from users_app.models import Booker


class Archive(models.Model):
   name = models.CharField(max_length = 100)
   author = models.CharField(max_length = 150)
   image = models.ImageField(upload_to='booker/book_covers', null = True, blank = True)
   year = models.IntegerField(null = True, blank = True)
   vote = models.IntegerField(default = 0)