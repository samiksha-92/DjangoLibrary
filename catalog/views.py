from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
import datetime
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from catalog.forms import BookRenewForm

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


def renew_books(request,pk):
    Book_Copy_Info = get_object_or_404(Book_Copy_Info,pk=pk)

    if request.Method == 'POST':
        filled_form = BookRenewForm(request.POST)

    if form.is_valid():
      Book_Copy_Info_form_due_back = form.cleaned_data['due_back']
      Book_Copy_Info_form_due_back.save()

      return HttpResponseRedirect(reverse('my-borrowed'))


    else:
      proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
      form = RenewBookForm(initial={'renewal_date': proposed_renewal_date})

context = {
    'form': form,
    'Book_Copy_Info': Book_Copy_Info,
}

return render(request, 'catalog/book_renew_librarian.html', context)
 
