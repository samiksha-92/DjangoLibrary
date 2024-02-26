from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

from .models import Book,Book_Copy_Info,Language,Genre,Author
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    total_num_books = Book.objects.count()
    total_num_Book_Copy_Info = Book_Copy_Info.objects.count()
    total_num_Book_Copy_Info_avail = Book_Copy_Info.objects.filter(status__exact = 'a').count()
    total_num_authors = Author.objects.count()
    total_num_genres = Genre.objects.count()

    context = {
        'total_num_books' : total_num_books,
        'total_num_Book_Copy_Info' : total_num_Book_Copy_Info,
        'total_num_Book_Copy_Info_avail' : total_num_Book_Copy_Info_avail,
        'total_num_authors' : total_num_authors,
        'total_num_genres' : total_num_genres,
        

    }

    return render(request, 'index.html', context = context)


class BookListView(generic.ListView):
    model = Book

class BookDetailView(generic.DetailView):
    model = Book    


class AuthorListView(generic.ListView):
    model = Author
    
class AuthorDetailView(generic.DetailView):
    model = Author




class LoanedBooksByUserListView(LoginRequiredMixin,generic.ListView):
    model = Book_Copy_Info
    template_name = 'catalog/borrowed_books.html'
    

    def get_queryset(self):
        return (
           Book_Copy_Info.objects.filter(borrower=self.request.user)
            .filter(status__exact='o')
            .order_by('due_back')
        )

