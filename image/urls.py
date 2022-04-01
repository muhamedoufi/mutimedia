from django.urls import path
from . import views

app_name='image'

urlpatterns = [
    path('images', views.showImages, name ="images")
]