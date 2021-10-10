from django.shortcuts import render,HttpResponse
from .models import Movie,Series,SeriesVideo
# Create your views here.
def home(request):
    movies = Movie.objects.all().order_by('-uploaded')
    return render(request,'movies/home.html',{'movies':movies})

def moviePage(request,slug):
    movie = Movie.objects.get(id=slug)
    return render(request,'movies/viewpage.html',{'movie':movie})

def seriesHome(request):
    series = Series.objects.all().order_by('-uploaded')
    return render(request,'series/series.html',{'series':series})
    
def seriesPage(request,slug):
    serie = Series.objects.get(id = slug)
    videos = SeriesVideo.objects.filter(series = serie)
    return render(request,'series/seriesPage.html',{'videos':videos,'serie':serie})


def search(request):
    
    if(request.method == "GET"):
        query = request.GET.get("search")
        movies = Movie.objects.filter(name__contains=query)
        seriesList = Series.objects.filter(name__contains=query)
        if(not movies):
            items = query.split()
            for item in items:
                films = Movie.objects.filter(name__contains = item)
                movies = movies.union(films)

        if(not seriesList):
            items = query.split()
            for item in items:
                ser = Series.objects.filter(name__contains = item)
                seriesList = seriesList.union(ser)

    return render(request,'search/search.html',{'movies':movies,'series':seriesList})
