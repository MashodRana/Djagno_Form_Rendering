from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .forms import SimpleForm, CustomForm, CustomFormBootstrap

def simple_form_view(request):
    if request.method == 'POST':
        form = SimpleForm(request.POST)
        if form.is_valid():
            pass  # does nothing, just trigger the validation
    else:
        form = SimpleForm()
    return render(request, 'simple_form.html', {'form': form})

def custom_form_view(request):
    if request.method == 'POST':
        form = CustomForm(request.POST)
        if form.is_valid():
            pass  # does nothing, just trigger the validation
    else:
        form = CustomForm()
    return render(request, 'custom_form.html', {'form': form})

def cf_bootstrap_view(request):
    if request.method == 'POST':
        form = CustomFormBootstrap(request.POST)
        if form.is_valid():
            pass  # does nothing, just trigger the validation
    else:
        form = CustomFormBootstrap()
    return render(request, 'cf_bootstrap.html', {'form': form})