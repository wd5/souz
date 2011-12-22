# Create your views here.
from django.conf import settings
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.views.generic import simple
from production.models import Production
import datetime

def ProductionView(request):
    kung = Production.objects.all()
    ctx = {
        'kung': kung,
    }
    return render_to_response('article.html', RequestContext(request, ctx))

