from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Fish, Decoration
from .forms import FeedingForm



def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def fish_index(request):
    fish = Fish.objects.all()
    return render(request, 'fish/index.html', { 'fish': fish })

def fish_detail(request, f_id):
    fish = Fish.objects.get(id=f_id)
    id_list = fish.decorations.all().values_list('id')
    decorations_fish_doesnt_have = Decoration.objects.exclude(id__in=id_list)
    feeding_form = FeedingForm()
    return render(request, 'fish/detail.html', { 'fish': fish, 'feeding_form': feeding_form, 'decorations': decorations_fish_doesnt_have })

def add_feeding(request, f_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.fish_id = f_id
        new_feeding.save()
    return redirect('detail', f_id=f_id)

def assoc_decoration(request, f_id, decoration_id):
    Fish.objects.get(id=f_id).decorations.add(decoration_id)
    return redirect('detail', f_id=f_id)

class FishCreate(CreateView):
    model = Fish
    fields = '__all__'

class FishUpdate(UpdateView):
    model = Fish
    fields = ['species', 'color', 'water_type']

class FishDelete(DeleteView):
    model = Fish
    success_url = '/fish'

class DecorationList(ListView):
    model = Decoration

class DecorationDetail(DetailView):
    model = Decoration

class DecorationCreate(CreateView):
  model = Decoration
  fields = '__all__'

class DecorationUpdate(UpdateView):
  model = Decoration
  fields = ['item', 'color']

class DecorationDelete(DeleteView):
  model = Decoration
  success_url = '/decorations'