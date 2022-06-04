from django.urls import path
from . import views

app_name='image'

urlpatterns = [
    path('images/', views.showImages, name ="images"),
    path('imageform/', views.imageform, name ="imageform"),
    path('updateImage/<str:pk>',views.updateImage ,name='updateImage'),
    path('deleteImage/<str:pk>',views.deleteImage,name='deleteImage'),
]