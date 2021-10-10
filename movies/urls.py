from django.urls import path
from . import views
urlpatterns = [
    path("",views.home,name="home"),
    path("movie/<slug>",views.moviePage,name="moviepage"),
    path("series/",views.seriesHome,name='seriesHome'),
    path("series/<slug>",views.seriesPage,name='seriesHome'),
    path("search",views.search,name="search"),
]
