from django import forms
from .models import Contacto
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = [
            'cliente_nombre', 
            'cliente_email', 
            'cliente_telefono', 
            'cliente_direccion', 
            'message', 
            'check_box'
        ]

    def __init__(self, *args, **kwargs):
        super(ContactoForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Enviar'))
