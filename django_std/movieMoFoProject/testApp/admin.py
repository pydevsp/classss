from django.contrib import admin
from testApp.models import Movie
# Register your models here.

class MovieAdmin(admin.ModelAdmin):
    movie_list = ["Rdate","MovieName","Rating"]

admin.site.register(Movie,MovieAdmin)

