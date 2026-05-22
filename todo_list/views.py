from django.shortcuts import render, redirect
from works.models import Deals
from works.models import Dealer


# Create your views here.
def index(request):
    todo = Deals.objects.order_by('priority')

    return render(request, 'todo_list/home.html', {'todo': todo})



    





def delete_todo(request, id):
    todo = Deals.objects.get(id=id).delete()
    return redirect('home')


def about(request):
    return render(request, 'todo_list/about.html')


def contacts(request):
    return render(request, 'todo_list/contacts.html')