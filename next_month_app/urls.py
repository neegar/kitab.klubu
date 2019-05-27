from django.urls import path
from .views import *

# app_name = 'user_app'

urlpatterns = [
    path('nextbook/', book, name = 'nextbook'),
    path('nextbook/<b_id>', vote, name = 'votebook'),
    path('archive/', archive, name = 'bookarchive')
]