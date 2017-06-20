import datetime, json

from django.core import serializers
from django.shortcuts import render
from django.utils import timezone

from django.http import HttpResponse
from .models import Patient

def index(request):
    return render(request, 'mypats/index.html', {'duration': ''})

def index_duration(request, duration):
    return render(request, 'mypats/index.html', {'duration': duration})

def api(request, duration):
    dur = timezone.now().date() - datetime.timedelta(days = int(duration))
    latest_patient_list = Patient.objects.filter(first_visit_date__gte=dur)    
    return HttpResponse(serializers.serialize("json", latest_patient_list))

def api_all(request):
    all_patient_list = Patient.objects.all()
    return HttpResponse(serializers.serialize('json', all_patient_list))

def stats(request):
    return render(request, 'mypats/stats.html', {})

def stats_sex(request):
    male_count = Patient.objects.filter(sex='男').count()
    female_count = Patient.objects.filter(sex='女').count()
    sex_data = [male_count, female_count]
    return HttpResponse(json.dumps(sex_data))

def stats_age(request):
    total = Patient.objects.count()
    age_data = []
    for i in range(0,100,10):
        cnt = Patient.objects.filter(age__gte=i).filter(age__lt=i+10).count()
        total = total - cnt
        age_data.append(cnt)
    
    age_data.append(total)
    return HttpResponse(json.dumps(age_data))

def stats_address(request):
    total = Patient.objects.count()
    addrs = ['新城','碑林','莲湖','雁塔','未央','灞桥','阎良','临潼','长安','周至','蓝田','高陵','户县','西咸']
    address_data = []
    for addr in addrs:
        cnt = Patient.objects.filter(address__contains=addr).count()
        total = total - cnt
        address_data.append(cnt)
    
    addrs.append('其它')
    address_data.append(total)
    return HttpResponse(json.dumps(address_data))

def stats_date(request):
    date = timezone.now().date()
    year = date.year
    month = date.month
    if month == 12:
        date_data = [str(year+1) + '-01']
    else:
        date_data = [str(year) + '-' + str(month+1)]
    date_data.append(str(year) + '-' + str(month))

    for i in range(11):
        if month - 1 > 0:
            date_data.append(str(year) + '-' + str(month - 1))
        else:
            date_data.append(str(year-1) + '-' + str(month - 1 + 12))
        month = month - 1

    month_data = []
    for nextmonth, month in list(zip(date_data, date_data[1:])):
        month_data.append(Patient.objects.filter(first_visit_date__gte=month+'-01').filter(first_visit_date__lt=nextmonth+'-01').count())
    
    month_data.reverse()
    return HttpResponse(json.dumps(month_data))