from django.shortcuts import render
from . models import Product,Banner,Brand,Trandy,Offer,Arrived



def index(request):
    products = Product.objects.all()
    banner = Banner.objects.all()
    brand =Brand.objects.all()
    trandy = Trandy.objects.all()
    offer = Offer.objects.all()
    arrived = Arrived.objects.all()

    return render(request,'index.html',{'products':products,'banners':banner,'brands':brand,'trandys':trandy,'offers':offer,'arriveds':arrived})
# Create your views here.
