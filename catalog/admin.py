from django.contrib import admin
from .models import Author,Language,Book_Copy_Info,Book,Genre

# Register your models here.
class Books_Inline(admin.TabularInline):
    model = Book
    extra = 1

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display =('last_name','first_name','date_of_birth','date_of_death')
    fields = [('first_name','last_name'),('date_of_birth','date_of_death')]
    inlines = [Books_Inline]

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    pass

@admin.register(Book_Copy_Info)
class Book_Copy_InfoAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')
    fieldsets = (
        ('Details', {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back','borrower')
        }),
    )


class Book_Copy_Info_Inline(admin.TabularInline):
    model = Book_Copy_Info
    extra = 0

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
  list_display = ('title','author','display_genre')
  inlines = [Book_Copy_Info_Inline]

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass
