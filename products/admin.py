import site
from django.contrib import admin
from .models import Banner,Trandy,Product,Offer,Arrived,Brand

class BannerAdmin(admin.ModelAdmin):
    list_display = ('img','offer_word','heading','btn')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('img','name')

class TrandyAdmin(admin.ModelAdmin):
    list_display = ('img','name','amount','offer','offer_amt')

class OfferAdmin(admin.ModelAdmin):
    list_display = ('img','offer_word','heading','btn')
class ArrivedAdmin(admin.ModelAdmin):
    list_display = ('img','name','amount','offer','offer_amt')


admin.site.register(Banner,BannerAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Trandy,TrandyAdmin)
admin.site.register(Offer,OfferAdmin)
admin.site.register(Arrived,ArrivedAdmin)
admin.site.register(Brand)

# Register your models here.
