from django.contrib import admin

# Register your models here.
from .models import Marvel

class CustomMarvelAdmin(admin.ModelAdmin):
    model = Marvel
    list_display=('character','description','name')
    list_filter=('character','description')
    
    search_fields=('character','description')
    fieldsets=(('Owner',{'fields':('name',)}),('marvel info',{'fields':('character','description',)}),)

admin.site.register(Marvel,CustomMarvelAdmin)
