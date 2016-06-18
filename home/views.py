from django.shortcuts import render_to_response
from django.template import RequestContext


def index(request):
    return render_to_response('home/index.html',
                              context_instance=RequestContext(request))


def dingus(request):
    return render_to_response('home/dingus.html',
                              context_instance=RequestContext(request))
