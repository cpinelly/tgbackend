# Create your views here.

from django.template import RequestContext
from django.shortcuts import render_to_response, redirect, get_object_or_404

def inicio(request):
	return render_to_response('index.html', {}, context_instance=RequestContext(request))
