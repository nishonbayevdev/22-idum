from django.urls import path
from .views import Home, send
from .views import about
from .views import news
from .views import contact
from .views import post
from .views import search
from .views import Message
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('' , Home , name='home'),
    path('about/' , about, name='about'),
    path('news/' , news , name='news'),
    path('search/' , search , name='search'),
    path('contact/' , contact , name='contact'),
    path('send/',send),
    path('post/<int:pk>',post,name='post')
] 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)