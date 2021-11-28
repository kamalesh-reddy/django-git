from django.urls import path
from basicapp import views

app_name = 'basic_app'

urlpatterns = [
    path('', views.index),
    path('other/', views.other, name = 'other'),
    path('relative/', views.relative, name = 'relative'),
]
