from django.urls import path
from .views import *

# app_name = 'user_app'

urlpatterns = [
    path('discussion/<book_id>', discussion, name = 'discussion')
]