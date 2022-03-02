from django.shortcuts import render, HttpResponse, redirect
from .models import Movie, Series, SeriesVideo
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .forms import OrderForm, CreateUserForm
# from .filters import OrderFilter
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.



# register page
def registerPage(request):
    form = CreateUserForm()

    if(request.method == "POST"):
        form = CreateUserForm(request.POST)
        if(form.is_valid()):
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account created successfully for '+user)
            return redirect('login')

    context = {'form': form}
    return render(request, '../templates/register/register.html', context)


# login page
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, '../templates/login/login.html', context)
# logout page
def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def home(request):
    movies = Movie.objects.all().order_by('-uploaded')
    return render(request, 'movies/home.html', {'movies': movies})


@login_required(login_url='login')
def moviePage(request, slug):
    movie = Movie.objects.get(id=slug)
    return render(request, 'movies/viewpage.html', {'movie': movie})


@login_required(login_url='login')
def seriesHome(request):
    series = Series.objects.all().order_by('-uploaded')
    return render(request, 'series/series.html', {'series': series})


@login_required(login_url='login')
def seriesPage(request, slug):
    serie = Series.objects.get(id=slug)
    videos = SeriesVideo.objects.filter(series=serie)
    return render(request, 'series/seriesPage.html', {'videos': videos, 'serie': serie})


@login_required(login_url='login')
def search(request):

    if(request.method == "GET"):
        query = request.GET.get("search")
        movies = Movie.objects.filter(name__contains=query)
        seriesList = Series.objects.filter(name__contains=query)
        if(not movies):
            items = query.split()
            for item in items:
                films = Movie.objects.filter(name__contains=item)
                movies = movies.union(films)

        if(not seriesList):
            items = query.split()
            for item in items:
                ser = Series.objects.filter(name__contains=item)
                seriesList = seriesList.union(ser)

    return render(request, 'search/search.html', {'movies': movies, 'series': seriesList})
