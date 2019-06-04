from django.contrib import admin
from psqlapp.models import Actor

class Actoradmin(admin.ModelAdmin):
    list_display = ['Name','address','date','age','image_tag']


admin.site.register(Actor,Actoradmin)