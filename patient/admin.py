from django.contrib import admin

from patient.models import Patient,Consultation,Rendevous
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from django.contrib.auth.models import User

# class usr_fields(admin.ModelAdmin):
#     class Meta:
#         model = User

#     list_display = ('get_groups')

#     def get_groups(self, obj):
#         return obj.groups.values_list('name',flat=True)
# # Re-register UserAdmin
#     get_groups.short_description = 'Groups'

class UserAdminWithGroup(UserAdmin):
    def group_name(self, obj):
        queryset = obj.groups.values_list('name',flat=True)
        groups = []
        for group in queryset:
            groups.append(group)
        
        return ' '.join(groups)

    list_display = UserAdmin.list_display + ('group_name',)

admin.site.unregister(User)
admin.site.register(User, UserAdminWithGroup)
# admin.site.unregister(User)
# admin.site.register(User, usr_fields)
admin.site.site_header = "Image medical Admin Panel"
admin.site.site_title = "Image medical Admin Panel"

class  PatientAdmin(admin.ModelAdmin):
    fields = ['nom','prenom','sexe','dateNaissance','lieuNaissance','lieuResidance','NumTel1','NumTel2','Assurance']
    list_display = ['secretaire','nom','prenom','sexe','dateNaissance','lieuNaissance','lieuResidance','NumTel1','NumTel2','Assurance']
    list_display_links = ['secretaire']
    list_editable = ['nom','prenom','sexe','dateNaissance','lieuNaissance','lieuResidance','NumTel1','NumTel2','Assurance']
    list_filter = ['nom','prenom','sexe','dateNaissance','lieuNaissance','lieuResidance','NumTel1','NumTel2']
    search_fields = ['nom','prenom','sexe','dateNaissance','lieuNaissance','lieuResidance','NumTel1','NumTel2']

class ConsultationAdmin(admin.ModelAdmin):
    fields = ['medecin','patient','dateConsultation','resultatConsultation']
    list_display = ['medecin','patient','dateConsultation','resultatConsultation']
    list_display_links = ['medecin']
    list_editable = ['patient','dateConsultation','resultatConsultation']
    list_filter = ['medecin','patient','dateConsultation']
    search_fields = ['medecin','patient','dateConsultation']

class RendevousAdmin(admin.ModelAdmin):
    fields = ['medecin_technicien','patient','dateRendevou','Status_Patient']
    list_display = ['medecin_technicien','patient','dateRendevou','Status_Patient']
    list_display_links = ['medecin_technicien']
    list_editable = ['patient','dateRendevou','Status_Patient']
    list_filter = ['medecin_technicien','patient','dateRendevou']
    search_fields = ['medecin_technicien','patient','dateRendevou']

admin.site.register(Patient,PatientAdmin)
admin.site.register(Consultation,ConsultationAdmin)
admin.site.register(Rendevous,RendevousAdmin)