from django.shortcuts import render_to_response
from django.template import RequestContext
from luna.ventrilo.models import Server

def index(request):
    response = {'servers': Server.objects.all }
    return render_to_response('ventrilo/index.html', response,
                              context_instance=RequestContext(request))

def status(request, server_id):
    response = {'server': Server.objects.get(pk=server_id) }
    return render_to_response('ventrilo/status.html', response,
                              context_instance=RequestContext(request))