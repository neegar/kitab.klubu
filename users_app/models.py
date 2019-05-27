from django.db import models
from django.contrib.auth.models import User
#from datetime

# Create your models here.
class Booker (models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    image = models.ImageField(upload_to='booker/user_avatar', null = True, blank = True)
    birth_day = models.DateField( null = True, blank = True)
    


