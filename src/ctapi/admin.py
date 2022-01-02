# app/movies/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin

from .models import Foster, Cat, Vet, Medication, VetVisit, Prescription


# Register your models here. 
  
admin.site.register(Cat)
admin.site.register(Vet)
admin.site.register(Foster)
admin.site.register(Medication)
admin.site.register(VetVisit)
admin.site.register(Prescription)

# @admin.register(CustomUser)
# class UserAdmin(DefaultUserAdmin):
#     pass


# @admin.register(Foster)
# class FosterAdmin(admin.ModelAdmin):
#     fields = (
#         "first_name", "last_name", "phone_num", "email",
#         "address", "city", "state", "zip_code"
#     )
#     list_display = (
#         "first_name", "last_name", "phone_num", "email",
#         "address", "city", "state", "zip_code"
#     )
