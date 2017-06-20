import datetime

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone

# Create your models here.
@python_2_unicode_compatible  # only if you need to support Python 2
class Patient(models.Model):
    """ Patient Record """
    name = models.CharField('姓名', max_length=32)
    #age = models.CharField('年龄', max_length=32, validators=(str.isdigit,))
    age = models.IntegerField('年龄')
    sex = models.CharField('性别', max_length=2, choices=(('男', '男'), ('女', '女')), default='男')
    address = models.CharField('住址', max_length=200)
    profession = models.CharField('职业', max_length=32, blank=True, null=True)
    phone = models.CharField('电话', max_length=32, blank=True, null=True)
    anaphylaxis = models.CharField('药物过敏史', max_length=200, blank=True, null=True)
    first_visit_date = models.DateField('初诊日期', default=datetime.date.today)
    symptom = models.CharField('症状', max_length=200, blank=True, null=True)
    diagnosis = models.CharField('诊断', max_length=200, blank=True, null=True)

    class Meta:
        verbose_name = "患者"
        verbose_name_plural = "患者"

    def __str__(self):
        return self.name
    
    def visited_recently(self):
        """ Visited recently"""
        now = timezone.now()
        return now.date() - datetime.timedelta(days=7) <= self.first_visit_date <= now.date()
    visited_recently.admin_order_field = 'first_visit_date'
    visited_recently.boolean = True
    visited_recently.short_description = '最近一周内?'
