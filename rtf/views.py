from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render, get_object_or_404
from rtf.models import Protest
from geopy import geocoders
from django.contrib.admin.views.decorators import staff_member_required
from time import sleep
from django.utils import simplejson
from django.core import serializers

def protests(request):
	protest_list = Protest.objects.all().order_by('city')
	context = {'protest_list' : protest_list}
	return render(request, 'protests/protests.html', context)

def protest(request, protest_id):
	protest = get_object_or_404(Protest, pk=protest_id)
	context = {'protest' : protest }
	return render(request, 'protests/protest.html', context)

def protestsjson(request):
	protest_list = Protest.objects.all()
	data = serializers.serialize('json', protest_list)
	print("hit this")
	return HttpResponse(data, mimetype="application/json")

@staff_member_required
def recalclatlong(request):
	protests = Protest.objects.all()
	for protest in protests:
		protest.generateLatLong()
		protest.save()
	context = {'protest_list' : protests}
	return render(request, 'protests/protests.html', context)
