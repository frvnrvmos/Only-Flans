from django.shortcuts import render
from django.http import HttpResponseRedirect 
from django.contrib.auth.decorators import login_required
from .models import Flan, ContactForm
from .forms import ContactFormModelForm   

def index(request):
    flanes_publicos = Flan.objects.filter(is_private=False)
    return render(request, 'web/index.html', {'flanes': flanes_publicos})

def about(request):
    return render(request, 'web/about.html')

@login_required
def welcome(request):
    flanes_privados = Flan.objects.filter(is_private=True)
    context = {
        'flanes': flanes_privados
    }
    return render(request, 'web/welcome.html', context)
def contact(request):
    if request.method == 'POST':
        form = ContactFormModelForm(request.POST)
        if form.is_valid():  
            form.save()

            return HttpResponseRedirect('/exito')
    else:
        form = ContactFormModelForm()        
    return render(request, 'web/contact.html', {'form': form})

def contact_success(request):
    return render(request, 'web/contact_success.html')

def faqs_view(request):
    return render(request, 'web/faqs.html')


