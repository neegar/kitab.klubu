from django.shortcuts import render
from next_month_app.models import Archive
from .models import BookDiscussion

def discussion(request, book_id):
    query_book = Archive.objects.get(pk=book_id)
    query_discussion = BookDiscussion.objects.filter(book=book_id)

    return render(request, 'discussion.html', {'query_book':query_book, 'query_discussion':query_discussion})
