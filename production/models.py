# coding: utf-8
#from django.db import models
#import sys, time
#import os
#from django import forms
from django.utils.translation import ugettext_lazy as _
#from os.path import basename
from django.db import models
#from tinymce import models as tinymce

MODELS = (
    ('mitsubishi', 'Mitsubishi'),
    ('ford', 'Ford'),
    )

TUNING = (
    ('roo_bar', u'Кенгурятник'),
    ('grille', 'Grille'),
    )

class Production(models.Model):
    add_date = models.DateField(auto_now_add=True)
    name_mod = models.CharField(_("Name_Mod"), max_length=50)
    ch_models = models.CharField(max_length=32, choices=MODELS)
    ch_tuning = models.CharField(max_length=32, choices=TUNING)
    image = models.ImageField(_("Image"), upload_to="photo")
    long_desc = models.TextField(_("Description"))

    def __unicode__(self):
        return '%s %s %s %s' % (self.ch_models, self.ch_tuning, self.add_date, self.name_mod)

# Create your models here.
