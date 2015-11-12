# -*- coding:utf8 -*-
from django.shortcuts import render
from django.shortcuts import redirect
import random
from spots.models import Book ,Totalspots , Cities
from bs4 import BeautifulSoup
import urllib
from django.core.paginator import Paginator , EmptyPage, PageNotAnInteger

def cities():

    cities_ch = ('基隆市','台北市','新北市','桃園縣','新竹市','新竹縣','苗栗縣','台中市','彰化縣',
                '南投縣','雲林縣','嘉義市','嘉義縣','台南市','高雄市','屏東縣','宜蘭縣','花蓮縣',
                '台東縣','澎湖縣','金門縣','連江縣')

    return cities_ch

def choosecity(request,city_name):

    cite_temp = Cities.objects.filter(cities=city_name)

    cite_temp1 = Totalspots.objects.filter(cities=city_name)

    return render(request,"citylist.html",{'contents1':cite_temp,'contents':cite_temp1,'title':city_name,'cities':cities()})

def index(request):

    recommend_temp = random.sample(Totalspots.objects.all(),5)

    return render(request,"index.html",{'cities':cities(),'contents':recommend_temp,'navbar_id':'home'})

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
        if not cite_temp:
            return render(request,"search.html",{'contents':cite_temp,'cities':cities()})
        else:
            return render(request,"search.html",{'contents':cite_temp,'cities':cities()})
    else:
        recommend_temp = random.sample(Totalspots.objects.all(),5)

        return  render(request, 'index.html',{'cities':cities(),'recommend_temp':recommend_temp,'navbar_id':'home'})

class News:
    def __init__(self,title, cite, link):
        self.title = title
        self.cite = cite
        self.link = link


def newsdetails(request):

    if request.method == 'POST':

        if 'news_link' in request.POST and request.POST['news_link']:

                list_body = []
                content_head = ''
                content_body =''
                news_cite = ''

                news_link = request.POST['news_link']

                website = urllib.urlopen(news_link.encode("utf8"))

                soup = BeautifulSoup(website)

                templatehead = soup.find(id="mediaarticlehead")
                for content in templatehead.find_all("h1"):
                    content_head = content.get_text()

                templatebody = soup.find(id="mediaarticlebody")
                for content in templatebody.find_all("p"):
                    content_body += content.get_text()
                    #list_body.append(content.get_text().encode('utf-8'));

                for temp1 in templatehead.find_all('cite'):
                    news_cite += temp1.get_text()

                return render(request,"newsdetails.html",{'cities':cities(),'info':'OK','contentbody':content_body,'title':content_head,'newscite':news_cite})

    else:
        return render(request,"newsdetails.html",{'cities':cities(),'info':'error'})

    return render(request,"newsdetails.html",{'cities':cities(),'info':'OK'})

def news(request):

    website = urllib.urlopen("https://tw.news.yahoo.com/travel/archive/")

    yahoolink = 'https://tw.news.yahoo.com'

    soup = BeautifulSoup(website)

    template = soup.find(id="MediaStoryList")

    list_link = []
    list_title = []
    list_cite = []

    list_total = []

    for name in template.find_all('h4'):
        list_title.append(name.get_text())
        for temp in name.find_all('a'):
            list_link.append(yahoolink+temp.get('href'))

    for temp1 in template.find_all('cite'):
        list_cite.append(temp1.get_text())

    for x in xrange(1,len(list_title)):
        list_total.append(News(list_title[x],list_cite[x],list_link[x]))

    page = request.GET.get('page')
    list_total_data = pagination(list_total,page,request)

    pagesize = (1,2,3,4,5)

    page = request.GET.get('page')

    return render(request,"news.html",{'cities':cities(),'dataFiled':list_total_data,'pageSize':pagesize,'navbar_id':'news'})

def pagination(list_total,page,request):
    paginator = Paginator(list_total,5);

    try:
        list_total = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        list_total = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        list_total = paginator.page(paginator.num_pages)

    return list_total