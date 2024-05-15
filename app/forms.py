from django import forms
from .models import Contacto

class TextInputWidget(forms.TextInput):
    def __init__(self, *args, **kwargs):
        kwargs['attrs'] = {'type': 'text'}
        super().__init__(*args, **kwargs)

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['cliente_nombre','cliente_email','cliente_telefono', 'cliente_direccion' ,'message','check_box']
        widgets = {
            'customer_email': TextInputWidget(),  # Usa el widget personalizado
        }