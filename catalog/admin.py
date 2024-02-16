from django.contrib import admin
from .models import Author,Language,Book_Copy_Info,Book,Genre

# Register your models here.
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display =('last_name','first_name','date_of_birth','date_of_death')

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    pass

@admin.register(Book_Copy_Info)
class Book_Copy_InfoAdmin(admin.ModelAdmin):
    pass

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass
