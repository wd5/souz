# coding: utf-8
from django.utils.translation import ugettext_lazy as _
from django.db import models
from stdimage import StdImageField
from django.core.files.storage import FileSystemStorage
from django.conf import settings

fs = FileSystemStorage(location=settings.MEDIA_ROOT)

MODELS = (
    ('mitsubishi', 'Mitsubishi'),
    ('ford', 'Ford'),
    )

TUNING = (
    ('roo_bar', u'Кенгурятник'),
    ('car_thresholds', u'Пороги'),
    ('a_xenon', u'Авто Ксенон')
    )

class Production(models.Model):
    add_date = models.DateField(auto_now_add=True)
    name_mod = models.CharField(_(u"Модель"), max_length=50)
    ch_models = models.CharField(_(u"Марка авто"),max_length=32, choices=MODELS)
    ch_tuning = models.CharField(_(u"Тюнинг"), max_length=32, choices=TUNING)
#    image = models.ImageField(_(u"Фотография"), upload_to="photo")
    image = StdImageField(_(u"Фотография"), storage = fs, upload_to="photo", size=(170, 127))
    long_desc = models.TextField(_(u"Описание"))

    def __unicode__(self):
        return u'%s | %s | %s | %s' % (self.ch_models, self.ch_tuning, self.add_date, self.name_mod)

# Create your models here.
