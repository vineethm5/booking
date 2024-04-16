from django.shortcuts import render
from .models import *
from django.http import JsonResponse

# Create your views here.
def home(req):
    return render(req,"home.html")


def get_hotel(req):
    try:
        queryset=booking.objects.all()
        if req.GET.get("sort_by"):
            sortbyval=req.GET.get("sort_by")
            if sortbyval == 'asc':
                queryset=queryset.order_by('sortbyval')
            elif sortbyval == 'desc':
                queryset=queryset.order_by('-sortbyval')

            if req.GET.get("amount"):
                amm=req.GET.get("amount")
                queryset=queryset.filter(hprice=amm)


            payload=[]
            for query in queryset:
                payload.append({'name':query.hname,'price':query.hprice,'description':query.description})
            return JsonResponse(payload,safe=False)
    except Exception as e:
        print(e)
        