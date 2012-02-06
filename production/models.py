# coding: utf-8
from django.utils.translation import ugettext_lazy as _
from django.db import models
from stdimage import StdImageField
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from settings import MEDIA_URL

fs = FileSystemStorage(location=settings.MEDIA_ROOT)

MODELS = (
    ('mitsubishi', 'Mitsubishi'),
    ('ford', 'Ford'),
    )

TUNING = (
    ('roo_bar', u'Кенгурятники'),
    ('car_thresholds', u'Пороги(труба, лист)'),
    ('auto_body_kit', u'Готовые комплекты обвесов'),
    ('internal_thresholds', u'Накладки на внутренние пороги'),
    ('hitch', u'Фаркопы'),
    ('mufflers', u'Глушители'),
    ('glass_fiber', u'Стекловолокно(бампера, решетки, споллера)'),
    ('optics', u'Оптика'),
    ('others', u'Разное'),
    )

class Production(models.Model):
    add_date = models.DateField(auto_now_add=True)
    name_mod = models.CharField(_(u"Модель"), max_length=50)
    ch_models = models.CharField(_(u"Марка авто"),max_length=32, choices=MODELS)
    ch_tuning = models.CharField(_(u"Тюнинг"), max_length=32, choices=TUNING)
    #cost = models.DecimalField(max_digits=10,decimal_places=2,blank=True, null=True)
    image = StdImageField(_(u"Фотография"), storage = fs, upload_to="photo", blank=True)
    image_th = StdImageField(_(u"Миниатюра"), storage = fs, upload_to="photo", size=(170, 127))
    long_desc = models.TextField(_(u"Описание"))

    def __unicode__(self):
        return u'%s | %s | %s | %s' % (self.ch_models, self.ch_tuning, self.add_date, self.name_mod)

    class Meta:
        ordering = ('name_mod',)

# Create your models here.
