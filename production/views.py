# Create your views here.
from django.conf import settings
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.views.generic import simple
from production.models import Production
import datetime

def ProductionViewMitsubishi(request):
    roo_bar = Production.objects.filter(ch_models="mitsubishi", ch_tuning="roo_bar")
    car_thresholds = Production.objects.filter(ch_models="mitsubishi", ch_tuning="car_thresholds")
    auto_body_kit = Production.objects.filter(ch_models="mitsubishi", ch_tuning="auto_body_kit")
    internal_thresholds = Production.objects.filter(ch_models="mitsubishi", ch_tuning="internal_thresholds")
    ctx = {
        'roo_bar': roo_bar,
        'car_thresholds': car_thresholds,
        'auto_body_kit': auto_body_kit,
        'internal_thresholds': internal_thresholds,
    }
    return render_to_response('mitsubishi.html', RequestContext(request, ctx))

