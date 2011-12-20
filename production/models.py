from django.db import models
import sys, time
import os
from django import forms
from django.utils.translation import ugettext_lazy as _
from os.path import basename
from django.db import models
from tinymce import models as tinymce

MODELS = (
    ('mitsubishi', 'Mitsubishi'),
    ('ford', 'Ford'),
    )

TUNING = (
    ('kung', 'Kung'),
    ('grille', 'Grille'),
    )

class Production(models.Model):
    add_date = models.DateField(auto_now_add=True)
    name_mod = models.CharField(_("Name_Mod"), max_length=50)
    ch_models = models.CharField(max_length=32, choices=MODELS)
    ch_tuning = models.CharField(max_length=32, choices=TUNING)
    image = models.ImageField(_("Image"), upload_to="photo")
    longdesc = tinymce.HTMLField((_("Description")))

    def __unicode__(self):
        return self.name_mod

# Create your models here.
