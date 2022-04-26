from django.contrib import admin

from image.models import Image

# Register your models here.
class  ImageAdmin(admin.ModelAdmin):
    fields = ['img','type','description','patient']
    list_display = ['img','type','description','technicien','patient']
    list_display_links = ['technicien']
    list_editable = ['img','type','description','patient']
    list_filter = ['type','description','technicien','patient']
    search_fields = ['type','description','technicien','patient']

admin.site.register(Image,ImageAdmin)