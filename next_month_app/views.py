import requests
import xml.etree.ElementTree as ET
from django.shortcuts import render, redirect
from .forms import BookForm
from .models import Archive
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def book(request):
   url = "https://www.goodreads.com/search/index.xml?key=g1ZZmWQsmm33TkUiw6GNg&q={}"

   if request.method == 'POST':
       form = BookForm(request.POST)
       if form.is_valid():
           try:
               name = form.cleaned_data.get('name')
               result = requests.get(url.format(name))
               root = ET.fromstring(result.text)
               result_len = int(next(root.iter('total-results')).text)

               b = [[book[8][1].text, book[8][2][1].text, book[4].text, book[8][3].text, book[8][4].text] for book in root.iter('work')]
               about_book ={
                   'name' : b[0][0],
                   'author': b[0][1],
                   'year' : b[0][2],
                   'image' : b[0][3]
               }
               query_results = Archive.objects.all().order_by('-vote')

               choice = Archive.objects.filter(name = about_book['name'])
               if choice:
                   messages.success(request, f'Bu kitab artiq movcuddur.')
               else:
                   a = Archive(name = b[0][0], author = b[0][1], year= b[0][2], image = b[0][3])
                   a.save()

               return render(request,'book.html',{'query_results':query_results})

           except:
               messages.success(request, f'Tapilmadi.')
   else:
       form = BookForm()
       query_results = Archive.objects.all().order_by('-vote')
       return render(request,'book.html',{'query_results':query_results})
   book_data = []


   context = {'book_data': book_data, 'form': form}
   return render(request, 'book.html', context)

@login_required(login_url='login')
def vote(request, b_id):
   if request.method == 'POST':
       book = Archive.objects.get(pk=b_id)
       book.vote +=1
       book.save()
   return redirect('nextbook')



def archive(request):
   query_results = Archive.objects.all()
   return render(request, 'archive.html')
import requests
import xml.etree.ElementTree as ET
from django.shortcuts import render, redirect
from .forms import BookForm
from .models import Archive
from django.contrib import messages

# Create your views here.
def book(request):
   url = "https://www.goodreads.com/search/index.xml?key=g1ZZmWQsmm33TkUiw6GNg&q={}"

   if request.method == 'POST':
       form = BookForm(request.POST)
       if form.is_valid():
           try:
               name = form.cleaned_data.get('name')
               result = requests.get(url.format(name))
               root = ET.fromstring(result.text)
               result_len = int(next(root.iter('total-results')).text)

               b = [[book[8][1].text, book[8][2][1].text, book[4].text, book[8][3].text, book[8][4].text] for book in root.iter('work')]
               about_book ={
                   'name' : b[0][0],
                   'author': b[0][1],
                   'year' : b[0][2],
                   'image' : b[0][3]
               }
               query_results = Archive.objects.all().order_by('-vote')

               choice = Archive.objects.filter(name = about_book['name'])
               if choice:
                   messages.success(request, f'Bu kitab artiq movcuddur.')
               else:
                   a = Archive(name = b[0][0], author = b[0][1], year= b[0][2], image = b[0][3])
                   a.save()

               return render(request,'book.html',{'query_results':query_results})

           except:
               messages.success(request, 'Axtardığınız kitab tapılmadı.')
   else:
       form = BookForm()
       query_results = Archive.objects.all().order_by('-vote')
       return render(request,'book.html',{'query_results':query_results})
   book_data = []


   context = {'book_data': book_data, 'form': form}
   return render(request, 'book.html', context)


def vote(request, b_id):
   if request.method == 'POST':
       book = Archive.objects.get(pk=b_id)
       book.vote +=1
       book.save()
   return redirect('nextbook')

def archive(request):
    query_results = Archive.objects.all()
    return render(request, 'archive.html', {'query_results':query_results})
