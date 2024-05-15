from django.shortcuts import redirect, render, get_object_or_404

from app.forms import ContactForm


# Create your views here.

def index(request):
    return render(request,'index.html', {})

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contacto_exitoso')
    else:
        form = ContactForm()
    return render(request, 'contact_form.html', {'form': form})

def contact_view_exito(request):
    return render(request, 'contacto_exitoso.html', {})