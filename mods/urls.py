from django.urls import path

from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('mod_signal',views.mod_signal,name='mod_signal'),
    path('about',views.about,name='about'),
    
]
