from django.contrib import admin
from django.urls import path
from . import views   # import our views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('add/', views.add_book, name='add_book'),
    path('delete/', views.delete_book, name='delete_book'),
]

