from . import views
from django.urls import path
app_name='patient'
urlpatterns = [
    path('', views.home, name ="home"),
    path('patientform',views.patientform ,name='patientform'),
    path('listPatient',views.listPatient ,name='listPatient'),
    path('contact',views.contact ,name='contact'),
]