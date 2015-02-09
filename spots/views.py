# -*- coding: utf-8 -*-
from django.shortcuts import render  
import random
from spots.models import Book ,Totalspots , Cities

def cities():

    cities_ch = ('基隆市','台北市','新北市','桃園縣','新竹市','新竹縣','苗栗縣','台中市','彰化縣',
                '南投縣','雲林縣','嘉義市','嘉義縣','台南市','高雄市','屏東縣','宜蘭縣','花蓮縣',
                '台東縣','澎湖縣','金門縣','連江縣')

    return cities_ch

def choosecity(request,city_name):

    cite_temp = Cities.objects.filter(cities=city_name)

    return render(request,"citylist.html",{'contents':cite_temp,'title':city_name,'cities':cities()})

def index(request):

    recommend_temp = random.sample(Totalspots.objects.all(),10)

    return render(request,"index.html",{'cities':cities(),'recommend_temp':recommend_temp,'navbar_id':'home'})

def aboutinfo(request):

    return render(request,"about.html",{'cities':cities(),'navbar_id':'about'})

def contactinfo(request):

    return render(request,"contact.html",{'cities':cities(),'navbar_id':'contact'})

def citydetails(request,city_name,zone_name):

    cite_temp = Totalspots.objects.filter(city=zone_name,cities=city_name)

    return render(request,"details.html",{'contents':cite_temp,'title':city_name,'title_zone':zone_name,'cities':cities()})

def spotsearch(request):

    if 'spot_search' in request.GET and request.GET['spot_search']:
        q = request.GET['spot_search']
        cite_temp = Totalspots.objects.filter(name__icontains=q)
        return render(request,"search.html",{'contents':cite_temp,'cities':cities()})
