from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render, get_object_or_404
from rtf.models import Protest

def protests(request):
	protest_list = Protest.objects.all().order_by('city')
	context = {'protest_list' : protest_list}
	return render(request, 'protests/protests.html', context)

def protest(request, protest_id):
	protest = get_object_or_404(Protest, pk=protest_id)
	context = {'protest' : protest }
	return render(request, 'protests/protest.html', context)
