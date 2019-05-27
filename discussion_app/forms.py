from django import forms
from next_month_app.models import Archive
from django.contrib.auth.models import User
from .models import BookDiscussion

class CommentForm(forms.ModelForm):
    form = BookDiscussion()
    comment = models.TextField()
    
    class Meta:
        model = BookDiscussion
        fields = ("comment",)



