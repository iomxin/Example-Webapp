from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('delete/<itemID>',views.delete,name='delete'),
    path('crossout/<itemID>',views.crossout,name='crossout'),
    path('uncross/<itemID>',views.uncross,name='uncross')
    ]
