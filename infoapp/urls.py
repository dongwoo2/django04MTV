from django.urls import path
from .import views

app_name = 'infoapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('detail/', views.detail1, name = 'detail1'),
    path('detail/<int:id>/', views.detail2, name = 'detail2'),
    path('edit/<int:id>/', views.edit, name = 'edit'),
    path('remove/<int:id>/', views.remove, name = 'remove'),
]

