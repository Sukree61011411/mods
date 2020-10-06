from django.shortcuts import render
import django
import numpy as np
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
# Create your views here.

def index(request):
    return render(request,'frontend/index.html')

def mod_signal(request):
    return render(request,'frontend/modulate.html')

def about(request):
    return render(request,'frontend/about.html')
