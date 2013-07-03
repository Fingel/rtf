import json
from django.db.models import Q
from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.core import serializers
from django.utils.text import slugify
from rtf.models import Protest
from geopy import geocoders

def protests(request):
  protest_list = Protest.objects.all().order_by('city')
  context = {'protest_list' : protest_list}
  return render(request, 'protests/protests.html', context)

def protests_by_state(request, state=None):
  protests = get_list_or_404(Protest, state_slug=state.lower())
  return render(request, 'protests/protest.html', {'protests': protests})

def protest_by_city(request, state=None, city=None, protest=None):
  if protest is None:
    protest = get_object_or_404(Protest, state_slug=state.lower(), city_slug=city.lower())
  return render(request, 'protests/protest.html', {'protest': protest})

def protest_by_id(request, protest_id=None):
  protest = get_object_or_404(Protest, pk=protest_id)
  return redirect(protest.get_absolute_url(), protest=protest)

def protests_json(request):
  protest_list = Protest.objects.all().exclude(state=None).order_by('-state')
  data = [protest.to_json() for protest in protest_list]
  return HttpResponse(json.dumps(data), mimetype="application/json")

@staff_member_required
def recalclatlong(request):
  protests = Protest.objects.all()
  for protest in protests:
    protest.generateLatLong()
    protest.save()
  context = {'protest_list' : protests}
  return render(request, 'protests/protests.html', context)

def blitzio(request):
  return HttpResponse("42")
