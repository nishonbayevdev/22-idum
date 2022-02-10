from django.conf.urls import handler404, handler500,handler400
from django.urls import path ,include
from django.contrib import admin
urlpatterns = [
    path('admin/', admin.site.urls , name='logo' ),
    path('',include('pub.urls'))
]
handler404 = 'pub.views.handler404' 
handler500 = 'pub.views.handler500'
handler400 = 'pub.views.handler400'