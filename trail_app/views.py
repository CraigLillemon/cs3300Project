from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import TrailForm
# Create your views here.
def index(request):
# Render the HTML template index.html with the data in the context variable.
   states = State.objects.all()
   return render( request, 'trail_app/index.html', {'states':states})

def state_list(request):
# Render the HTML template index.html with the data in the context variable.
   states = State.objects.all()
   return render( request, 'trail_app/state_list.html', {'states':states})

def state_detail(request, pk):
   state = State.objects.get(id=pk)
   trails = Trail.objects.all().filter(state_id=pk).filter(is_active = True)
   return render(request, 'trail_app/state_detail.html', {'state': state, 'trails': trails})

def createTrail(request, pk):
    state = State.objects.get(pk=pk)
    
    if request.method == 'POST':
        form = TrailForm(request.POST, request.FILES)
        if form.is_valid():
            trail = form.save(commit=False)  
            trail.state = state
            trail.save()  
            return redirect('state-detail', pk=pk)
    else:
        form = TrailForm()  
    
    context = {'form': form}
    return render(request, 'trail_app/createTrail.html', context)

def trail_detail(request, pk):
   #portfolios = Portfolio.objects.get(id = pk)
   trail = Trail.objects.get(id = pk)
   return render(request, 'trail_app/trail_detail.html', {'trail': trail})
