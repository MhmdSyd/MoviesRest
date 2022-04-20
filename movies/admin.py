from django.contrib import admin
from .models import MoviesRest
# Register your models here.
class MoviesAdmin(admin.ModelAdmin):
    list_display = ['show_id', 'title', 'year', 'rating']

admin.site.register(MoviesRest, MoviesAdmin)