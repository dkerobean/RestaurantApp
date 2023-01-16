from django.forms import ModelForm
from .models import Contact, Reservation



class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        
        def __init__(self, *args, **kwargs):
            super(ContactForm, self).__init__(*args, **kwargs)

            for name, field in self.fields.items():
                field.widget.attrs.update(
                    {'class': 'form-control '})

                self.fields["name"].widget.attrs.update(
                    {'class': 'form-control'})
                
                
                
                
class ReservationForm(ModelForm):
    class Meta:
        model = Reservation
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})

            self.field["Date time"].widget.attrs.update(
                {'class': 'datepicker-here sb-datepicker'})
