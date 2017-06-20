from __future__ import unicode_literals

from collections import OrderedDict

from django.contrib import admin

from import_export.resources import ModelResource
from import_export.admin import ImportExportModelAdmin, ExportActionModelAdmin
# Register your models here.
from .models import Patient

class PatientResource(ModelResource):
    class Meta:
        model = Patient
        widgets = {
            'first_visit_date': {'format': '%Y-%m-%d'},
            }
    
    def before_import(self, dataset, using_transactions, dry_run, **kwargs):
        self.count = Patient.objects.count()

    def before_import_row(self, row, **kwargs):
        rid = name = age = sex = address = first_visit_date = None
        profession = phone = anaphylaxis = symptom = diagnosis = None
        for k, v in row.items():
            if isinstance(v, str):
                row[k] = v.strip('\' \"')
            if k.endswith('id') or k.endswith('序号'): # sometimes UTF8 starts with \xff\xff\xffid
                rid = row[k]
            if k.endswith('name') or k.endswith('姓名'):
                name = row[k]
            if k.endswith('age') or k.endswith('年龄'):
                age = row[k]
            if k.endswith('sex') or k.endswith('性别'):
                sex = row[k]
            if k.endswith('address') or k.endswith('住址'):
                address = row[k]
            if k.endswith('profession') or k.endswith('职业'):
                profession = row[k]
            if k.endswith('phone') or k.endswith('电话'):
                phone = row[k]
            if k.endswith('anaphylaxis') or k.endswith('药物过敏史'):
                anaphylaxis = row[k]
            if k.endswith('first_visit_date') or k.endswith('初诊日期'):
                first_visit_date = row[k]
            if k.endswith('symptom') or k.endswith('症状'):
                symptom = row[k]
            if k.endswith('diagnosis') or k.endswith('诊断'):
                diagnosis = row[k]
        row['id'] = str(int(rid) + self.count) # always append at the end
        row['name'] = name
        row['age'] = age
        row['sex'] = sex
        row['address'] = address
        row['profession'] = profession
        row['phone'] = phone
        row['anaphylaxis'] = anaphylaxis
        row['first_visit_date'] = first_visit_date
        row['symptom'] = symptom
        row['diagnosis'] = diagnosis

class PatientAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': [('name', 'age', 'sex'), ('address', 'first_visit_date')]}),
        ('详细信息', {'fields': [('profession', 'phone'), ('anaphylaxis', 'symptom'), 'diagnosis']
                    })
    ]
    radio_fields = {"sex": admin.HORIZONTAL}
    list_display = ('name', 'age', 'sex', 'first_visit_date', 'visited_recently')
    list_filter = ['first_visit_date']
    date_hierarchy = 'first_visit_date'
    search_fields = ['^name', '=age', '=sex', 'address', 'profession', 'anaphylaxis', 'symptom', 'diagnosis']
    resource_class = PatientResource

admin.site.register(Patient, PatientAdmin)