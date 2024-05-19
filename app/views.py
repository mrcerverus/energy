from django.shortcuts import redirect, render
from app.forms import ContactoForm


# Create your views here.

def index(request):
    return render(request,'index.html', {})

def contacto_view(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ContactoForm()
    return render(request, 'contacto_form.html', {'form': form})