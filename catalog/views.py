from django.shortcuts import render

# Create your views here.

from .models import Book,Book_Copy_Info,Language,Genre,Author

def index(request):
    total_num_books = Book.objects.count()
    total_num_Book_Copy_Info = Book_Copy_Info.objects.count()
    total_num_Book_Copy_Info_avail = Book_Copy_Info.objects.filter(status_exact = 'a').count()
    total_num_authors = Author.objects.count()

    context = {
        'total_num_books' : total_num_books,
        'total_num_Book_Copy_Info' : total_num_Book_Copy_Info,
        'total_num_Book_Copy_Info_avail' : total_num_Book_Copy_Info_avail,
        'total_num_authors' : total_num_authors,
        'total_num_authors' : total_num_authors,

    }

    return render(request, 'indes,html', context = context)