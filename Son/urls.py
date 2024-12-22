from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('linux-cheat-sheet/', views.linux_cheat_sheet, name='linux_cheat_sheet'),
    path('useful-links/', views.useful_links, name='useful_links'),
]
