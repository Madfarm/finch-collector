from django.shortcuts import render

finches =  [
    {'species': 'Common Chaffinch', 'mass': 0.73, 'sexually_dimorphic': True},
    {'species': 'House Finch', 'mass': 0.72, 'sexually_dimorphic': True},
]

# Create your views here.
def finches_index(request):
    return render(request, 'finches/index.html', {
        'finches': finches
    })

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')