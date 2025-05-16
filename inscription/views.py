from django.http import HttpResponse
from django.shortcuts import render

from .forms import InscriptionForm


# Create your views here.
def inscription(request):

    if request.method == 'POST':
        form = InscriptionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('Inscription reussie')
    else:
        form = InscriptionForm()

    context = {
        'form': form
    }

    return render(request, 'inscription.html', context)