from django.db import models

# Create your models here.
class Movie(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 50)
    image = models.URLField()
    movie_url = models.URLField()
    uploaded = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

class Series(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    image = models.URLField()
    uploaded = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

class SeriesVideo(models.Model):
    series = models.ForeignKey(Series,on_delete=models.CASCADE)
    season = models.IntegerField()
    episode = models.IntegerField()
    video_url = models.URLField()
    uploaded = models.DateField(auto_now=True)

    def __str__(self):
        return self.series.name + " season "+str(self.season) + " E " + str(self.episode)


class Order(models.Model):
    user = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)
    series = models.ForeignKey(Series,on_delete=models.CASCADE)
    order_date = models.DateField(auto_now=True)
    order_time = models.TimeField(auto_now=True)
    order_status = models.CharField(max_length=50)
    order_price = models.FloatField()
    order_address = models.CharField(max_length=50)
    order_city = models.CharField(max_length=50)
    order_state = models.CharField(max_length=50)
    order_zipcode = models.IntegerField()
    order_phone = models.IntegerField()
    order_email = models.EmailField()

    def __str__(self):
        return self.movie.name + " " + self.series.name
