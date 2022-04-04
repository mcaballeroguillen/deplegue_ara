from django.forms import ModelForm, DateInput
from calendarapp.models import Event, EventMember
from calendarapp.models.linea_presupuesto import Cronogram
from django import forms


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'start_time', 'end_time', 'linea_p', 'Presupuesto']
        # datetime-local is a HTML5 input type
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Escriba el título del evento'
            }),
            'description': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Escriba la descripción del evento'
            }),
            'start_time': DateInput(
                attrs={'type': 'datetime-local', 'class': 'form-control'},
                format='%Y-%m-%dT%H:%M'
            ),
            'end_time': DateInput(
                attrs={'type': 'datetime-local', 'class': 'form-control'},
                format='%Y-%m-%dT%H:%M'
            ),
            'Prespuesto':forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Presupuesto'}
            ),

        }
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        # input_formats to parse HTML5 datetime-local input to datetime field
        self.fields['start_time'].input_formats = ('%Y-%m-%dT%H:%M',)
        self.fields['end_time'].input_formats = ('%Y-%m-%dT%H:%M',)


class AddMemberForm(forms.ModelForm):
    class Meta:
        model = EventMember
        fields = ['user']

class excel_form(forms.ModelForm):
    class Meta:
        model= Cronogram
        fields = ["Proyecto", "Archivo_excel"]

#form