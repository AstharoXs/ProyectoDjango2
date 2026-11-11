from django.contrib import admin
from .models import Tarea

admin.site.register(Tarea)
class TareaAdmin(admin.ModelAdmin):
    list_display = ("id", "tarea")
    search_fields = ("tarea",)
    
# Register your models here.
