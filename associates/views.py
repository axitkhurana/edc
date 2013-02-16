# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from constants import *
from associates.models import Sponsor

def sponsors(request):
#       sponsors = Sponsor.objects.filter(event = event)
    sponsors = Sponsor.objects.all()
    print "you are an asshole"
    return render_to_response('associates/index.html',{'name':'Sponsors','list':create_events_menu(event),'sponsors':sponsors},context_instance=RequestContext(request))
