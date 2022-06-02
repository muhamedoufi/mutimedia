from . import views
from django.urls import path
app_name='patient'
urlpatterns = [
    path('', views.home, name ="home"),
    path('patientform',views.patientform ,name='patientform'),
    path('listPatient',views.listPatient ,name='listPatient'),
    path('consultation',views.consultation,name='consultation'),
    path('listConsultation',views.listConsultation,name='listConsultation'),
    path('rendevous',views.rendevous,name='rendevous'),
    path('listRendevous',views.listRendevous,name='listRendevous'),
    path('contact',views.contact ,name='contact'),
    path('imprimer_Rendevous/<int:id>',views.imprimer_Rendevous,name='imprimer_Rendevous'),
]