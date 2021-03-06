from django.shortcuts import render,get_object_or_404
from .models import Realtor,Flats
from django.http import HttpResponse
from .choices import city_choices,bedroom_choices,price_choices
from django.core.paginator import EmptyPage, PageNotAnInteger,Paginator

def index(request):
    h= Flats.objects.all()
    houses=h[:3]
    return render(request,'index.html',{'houses':houses})

def realtors(request,r_id):
    realtors=get_object_or_404(Realtor, pk=r_id)
    context={
        'r':realtors
    }
    return render(request,'realtor.html',context)

def browse(request):
    
    houses=Flats.objects.order_by('-list_date')
    
    paginator=Paginator(houses,2)
    page=request.GET.get('page')
    paged_houses=paginator.get_page(page)
    

    
    
    
    
    context={
        'houses':paged_houses,
        'city_choices':city_choices,
        'bedroom_choices':bedroom_choices,
        'price_choices':price_choices,

    }
    if request.user.is_authenticated :
        return render(request,'browse.html',context)
    else:
        return HttpResponse("Login first")

def infoh(request, h_id):

    html="<h1><center>Please Log in to view the houses<br>" + '<a href="/">Click to go back to Index</a></center></h1>'
    
    if( not request.user.is_authenticated):
        return HttpResponse(html)

    house=get_object_or_404(Flats, pk=h_id)
    context={
        'h':house
    }
    return render(request,'info.html',context)



   

def search(request):

    houses=Flats.objects.order_by('-list_date')

    if 'keywords' in request.GET :
        keywords=request.GET['keywords']
        if keywords:
            houses=houses.filter(description__icontains=keywords)

    
    if 'area' in request.GET:
        area=request.GET['area']
        if area:
            houses=houses.filter(area__icontains=area)

    if 'city' in request.GET:
        city=request.GET['city']
        if city:
            houses=houses.filter(city__iexact=city)

    if 'bedrooms' in request.GET:
        bedrooms=request.GET['bedrooms']
        if bedrooms:
            houses=houses.filter(bedrooms__lte=bedrooms)


    if 'price' in request.GET:
        price=request.GET['price']
        if price:
            houses=houses.filter(rate__lte=price)
        


    context={
        'houses':houses,
        'city_choices':city_choices,
        'bedroom_choices':bedroom_choices,
        'price_choices':price_choices,
        'values': request.GET

    }
    return render(request,'search.html',context)



def about(request):
    return HttpResponse("<h1>This is Real Estate Site Made BY Apoorva.A</h1><br>About button is just for show <br>Login for more")