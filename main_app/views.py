from django.shortcuts import render, redirect
from .models import Finch
from .forms import SightingForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.
def finches_index(request):
    finches = Finch.objects.all()
    return render(request, 'finches/index.html', {
        'finches': finches
    })

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_details(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    return render(request, 'finches/details.html', {
        'finch': finch
    })

def add_feeding(request, finch_id):
    form = SightingForm(request.POST)

    if form.is_valid():
        new_sighting = form.save(commit=False)
        new_sighting.finch_id = finch_id
        new_sighting.save()

    return redirect('details', finch_id=finch_id)


class FinchCreate(CreateView):
    model = Finch
    fields = '__all__'

class FinchDelete(DeleteView):
    model = Finch
    success_url = '/finches'

class FinchUpdate(UpdateView):
    model = Finch
    fields = '__all__'


