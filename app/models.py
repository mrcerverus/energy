from django.db import models
from django.utils.text import slugify
from phonenumber_field.modelfields import PhoneNumberField
import uuid

# Create your models here.

#Formulario de contacto
class Contacto(models.Model):
    contact_form_uuid = models.UUIDField(default=uuid.uuid4 , editable=False, unique=True)
    cliente_nombre = models.CharField(max_length=50, blank=False, null=False, verbose_name="Nombre Completo")
    cliente_email = models.EmailField(blank=False, null=False, verbose_name="Correo electronico")
    cliente_telefono = PhoneNumberField(blank=False, null=False, default='',verbose_name="Telefono de contacto")
    cliente_direccion = models.CharField(blank=False, max_length=100, verbose_name="Direccion")
    message = models.TextField(blank=False, null=False, verbose_name="Mensaje")
    check_box = models.BooleanField(default=False)

    def __str__(self):
        return self.cliente_nombre
