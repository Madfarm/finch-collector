from django.shortcuts import render

# Create your views here.
def finches_index(request):
    return render(request, 'finches/index.html')