from django.forms import ModelForm
from catalog.models import Book_Copy_Info

class BookRenewForm(ModelForm):
    data = self.cleaned_data['due_back']

    if data < datetime.date.today():
           raise ValidationError(_('book cannot be due int the past, Please enter a valid date'))
    if data > datetime.date.today() + datetime.timedelta(weeks =3 ):
        raise ValidationError(_('Please enter a date between today and 3 weeks'))

    return data


    class Meta:
        model = Book_Copy_Info
        fields = ['due_back']
        