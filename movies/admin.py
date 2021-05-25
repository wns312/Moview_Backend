from django.contrib import admin
from .models import Movie, Genre, Prefer

class GenreAdmin(admin.ModelAdmin):
    filter_horizontal = ('movie',)
admin.site.register(Movie)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Prefer)
