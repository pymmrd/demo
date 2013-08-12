# Create your views here.
from django.template import RequestContext
from django.shortcuts import render_to_response 

def show_creation(request, name):
	tmpl = '%s.html' % name
	return render_to_response(tmpl, context_instance=RequestContext(request))
