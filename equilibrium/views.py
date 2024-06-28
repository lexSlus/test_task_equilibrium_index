from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from utils import equilibrium
from .forms import ArrayForm
from .models import Page



def index(request):
    page = Page.objects.first()
    form = ArrayForm()
    result = None

    if request.method == 'POST':
        form = ArrayForm(request.POST)
        if form.is_valid():
            arr = form.cleaned_data['array']
            result_index = equilibrium(arr)
            if result_index == -1:
                result = "Equilibrium index not found."
            else:
                result = f"Equilibrium index of array: {result_index}"

    context = {
        'page': page,
        'form': form,
        'result': result
    }
    return render(request, 'index.html', context)