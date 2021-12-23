from django.contrib import admin
from .models import Employes , ThingCounts , News , Message ,VideoMessageNews ,AboutUs
# Register your models here.

class MessageAdmin(admin.ModelAdmin):
    list_display = ('email' , 'name' , 'text')
admin.site.register(Message , MessageAdmin)

class NewsAdmin(admin.ModelAdmin):
    list_display = ( 'title' , 'description')
admin.site.register(News , NewsAdmin)

class EmployesAdmin(admin.ModelAdmin):
    list_display = ('fullName','proffession','telegram','instagram','facebook')
admin.site.register(Employes,EmployesAdmin)

class ThingCountsAdmin(admin.ModelAdmin):
    list_display = ('students','teachers','rooms')
admin.site.register(ThingCounts,ThingCountsAdmin)
class VideoMessageNewsAdmin(admin.ModelAdmin):
    list_display = ('shortDescription','description','video')
admin.site.register(VideoMessageNews)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('title','description')
admin.site.register(AboutUs)