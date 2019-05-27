from django.shortcuts import render
from .models import CurrentBook
from next_month_app.models import Archive


# Create your views here.
def index(request):
    query_archive = Archive.objects.all()[4:]
    query_results = CurrentBook.objects.all()
    return render(request, 'index.html', {'query_results':query_results, 'query_archive':query_archive})