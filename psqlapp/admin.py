from django.contrib import admin
from psqlapp.models import Actor

class Actoradmin(admin.ModelAdmin):
    list_display = ['Name','address','date','age']


admin.site.register(Actor,Actoradmin)