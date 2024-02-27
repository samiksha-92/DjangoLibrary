from django.db import models
from django.urls import reverse
from django.conf import settings
import uuid
from datetime import date


# Create your models here.

class Book(models.Model):
  title = models.CharField(max_length = 200)
  author = models.ForeignKey('Author', on_delete=models.RESTRICT,null =True)
  summary = models.TextField(max_length = 900, help_text = 'Enter a brief description here')
  isbn = models.CharField('ISBN', max_length = 200, unique = True, help_text = '13 Character <a href="https://www.isbn-international.org/content/what-isbn'
   '">ISBN number</a>')
  genre = models.ManyToManyField('Genre', help_text = "Select a genre for this book")
  #language = models.ForeignKey('Language', on_delete =models.RESTRICT, null = True)
 
  def __str__(self):
    return f"{self.title}"

  def get_absolute_url(self):
    return reverse('book-detail', args=[str(self.id)])

  def display_genre(self):
    return ','.join(genre.name for genre in self.genre.all()[:2])
    display_genre.short_description = 'Genre'  


class Book_Copy_Info(models.Model):

    id = models.UUIDField(primary_key=True, default = uuid.uuid4,help_text = "Unique ID for this book")
    book = models.ForeignKey('Book', on_delete = models.RESTRICT, null =True)
    imprint = models.CharField(max_length = 200)
    due_back = models.DateField(null =True, blank =True)
    borrower = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)



    @property
    def is_overdue(self):
        """Determines if the book is overdue based on due date and current date."""
        return bool(self.due_back and date.today() > self.due_back)



    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )
    status = models.CharField(max_length = 1, choices = LOAN_STATUS, blank= True, default = 'm', help_text = 'Choose book availability status',)
    
    class Meta:
        ordering = ['due_back']
        permissions = (('can_mark_returned', 'Set Book as Returned'),)

    def __str__(self):
      return f"({self.book.title}) {self.status} {self.due_back} {self.id}"
      
class Author(models.Model):
  first_name = models.CharField(max_length = 100)
  last_name = models.CharField(max_length =100)
  date_of_birth = models.DateField(null = True, blank = True)
  date_of_death = models.DateField('Died', null = True, blank =True)

  class Meta :
    ordering = ['last_name','first_name']
     
  def __str__(self) :
      return f"{self.last_name}, {self.first_name}"

  def get_absolute_url(self):
    return reverse('author-detail', args = [str(self.id)])  

class Genre(models.Model):
  name = models.CharField(max_length = 200, unique=True , help_text = "Enter this book's genre" )
   
  def __str__(self):
    return f"{self.name}"

  def get_absolute_url(self):
    return reverse('genre-detail', args = [str(self.id)])

class Language(models.Model):
  SELECT_LANGUAGE = (
    ('e','English'),
    ('h','Hindi'),
    ('u','Urdu'),
    ('f','Farsi'),
         )
  language_name = models.CharField(max_length =200, choices =SELECT_LANGUAGE ,
  blank=True)

  def __str__(self):
    return f"{self.language_name}"

  def get_absolute_url(self):
    return reverse('language-detail', args =[str(self.id)])