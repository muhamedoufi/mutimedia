from . import views
from django.urls import path
app_name='patient'
urlpatterns = [
    path('', views.home, name ="home")
]