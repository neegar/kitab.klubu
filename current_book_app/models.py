from django.db import models
from next_month_app.models import Archive

class CurrentBook(models.Model):
    CurrentBook = models.OneToOneField(Archive, on_delete = models.CASCADE)



