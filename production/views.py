# Create your views here.
from django.conf import settings
from settings import MEDIA_URL
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from production.models import Production
import datetime

def ProductionViewMitsubishi(request):
    global roo_bar_i_m, roo_bar_i_d, roo_bar_i_chm, roo_bar_i_t, roo_bar_i_cht, roo_bar_i_th
    roo_bar = Production.objects.filter(ch_models="mitsubishi", ch_tuning="roo_bar").values("id", "add_date", "name_mod", "ch_models", "ch_tuning", "image_all", "long_desc")
    car_thresholds = Production.objects.filter(ch_models="mitsubishi", ch_tuning="car_thresholds")
    auto_body_kit = Production.objects.filter(ch_models="mitsubishi", ch_tuning="auto_body_kit")
    internal_thresholds = Production.objects.filter(ch_models="mitsubishi", ch_tuning="internal_thresholds")
    for item in roo_bar:
        roo_bar_i_m = item["name_mod"]
        roo_bar_i_chm = item["ch_models"]
        roo_bar_i_cht = item["ch_tuning"]
        roo_bar_i_t = item["image_all"]
        roo_bar_i_d = item["long_desc"]

    roo_bar_i_th = roo_bar_i_t[:-3]+"thumbnail.jpe"

    ctx = {
        'roo_bar_i_m': roo_bar_i_m,
        'roo_bar_i_d': roo_bar_i_d,
        'roo_bar_i_chm': roo_bar_i_chm,
        'roo_bar_i_t': roo_bar_i_t,
        'roo_bar_i_th': roo_bar_i_th,
        'car_thresholds': car_thresholds,
        'auto_body_kit': auto_body_kit,
        'internal_thresholds': internal_thresholds,
    }

    return render_to_response('mitsubishi.html', RequestContext(request, ctx))

