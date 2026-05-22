from django.shortcuts import render, redirect
from .models import Deals
from .models import Dealer
from .forms import DealsForm, DealerForm

# Create your views here.
def create_todo(request):
    error = ''
    if request.method == 'POST':
        form = DealsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'error'
    form = DealsForm


    data = {
        'form': form,
        'error': error

    }
    
    return render(request, 'works/create_todo.html', data)



