from django.shortcuts import render
from .models import Employes,ThingCounts , News ,Message,VideoMessageNews,AboutUs  
from django.contrib import messages
from django.template import RequestContext

# Create your views here.
# Home render
def Home(request):
    countsAll = ThingCounts.objects.all()[0]
    employesAll = Employes.objects.all()
    if len(News.objects.all()) >=3:
        newsAll = News.objects.all()[len(News.objects.all())-3::]
    if len(VideoMessageNews.objects.all()) >= 2:
        videoMessageNews = VideoMessageNews.objects.all()[len(VideoMessageNews.objects.all())-2::]
    AllData = {
        'Employes':employesAll,
        'counts':countsAll,
        'news':newsAll,
        'video_1':videoMessageNews[0],
        'video_2':videoMessageNews[1]
    }
    return render(request,'index.html',AllData)
# About render
def about(request):
    data = AboutUs.objects.all()[0]
    return render(request,'about.html',{'data':data})
# News render
def news(request):
    newNewsFull_1 = News.objects.all()
    return render(request,'news.html',{'news':newNewsFull_1})
# contact render        
def search(request):
    if request.method == 'POST':
        notFound = {'flag':True,'data':'Xech narsa Topilmadi iltimos qaytadan urinib ko\'ring'}
        searchKey = request.POST['search']
        if searchKey:
            newNewsFull_1 = News.objects.filter(title__contains = searchKey)
        else:
            newNewsFull_1 = News.objects.all()
            # print(searchKey)
        notFound['flag'] = False if newNewsFull_1 else True
    return render(request,'news.html',{'news':newNewsFull_1,'message':notFound})
def contact(request):
    return render(request,'contact.html')
def send(request):
    if request.method == 'POST':
        email = request.POST['email']
        name = request.POST['name']
        text = request.POST['text']
        saveMessage = Message(
            email=email,
            name=name,
            text=text
        )
        saveMessage.save()
    return render(request,'contact.html')

#############################################
# post news
def post(request,pk):
    newResponse = News.objects.get(id=pk)
    threeNewsalls = list(News.objects.all())
    if len(threeNewsalls) >=3:
        threeNewsalls.pop(pk-1)
        threeNewsalls = threeNewsalls[::3]
    return render(request,'post.html',{'new':newResponse,'threeNewsalls':threeNewsalls})
##################################################################################
# 404 
def handler404(request,*args,**argv):
    return render(request,'404.html')
def handler500(request,*args,**argv):
    return render(request,'500.html',status=500)
def handler400(request,*args,**argv):
    return render(request,'400.html')