from django.contrib import admin

from patient.models import Patient

# Register your models here.

admin.site.site_header = "Image medical Admin Panel"
admin.site.site_title = "Image medical Admin Panel"

class  PatientAdmin(admin.ModelAdmin):
    fields = ['nom','prenom','sexe','dateNaissance','lieuNaissance','lieuResidance','NumTel1','NumTel2','Assurance']
    list_display = ['secretaire','nom','prenom','sexe','dateNaissance','lieuNaissance','lieuResidance','NumTel1','NumTel2','Assurance']
    list_display_links = ['secretaire']
    list_editable = ['nom','prenom','sexe','dateNaissance','lieuNaissance','lieuResidance','NumTel1','NumTel2','Assurance']
    list_filter = ['nom','prenom','sexe','dateNaissance','lieuNaissance','lieuResidance','NumTel1','NumTel2']
    search_fields = ['nom','prenom','sexe','dateNaissance','lieuNaissance','lieuResidance','NumTel1','NumTel2']

admin.site.register(Patient,PatientAdmin)