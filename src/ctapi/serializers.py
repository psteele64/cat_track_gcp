from rest_framework import serializers
from .models import Foster, Cat, Vet, Medication, VetVisit, Prescription
# Serializers
        
class FosterSerializer(serializers.ModelSerializer):
    cats = serializers.StringRelatedField(many=True)
    class Meta:
        model = Foster
        fields = ('id', 'first_name', 'last_name', 'phone_num', 'email', 'address', 'city', 'state', 'zip_code', 'cats')
        
class CatSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cat
        fields = ('id', 'name', 'location', 'room_num', 'foster')
                   
class VetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vet
        fields = ('id', 'vet_name', 'practice_name', 'phone_num', 'email', 'address', 'city', 'state', 'zip_code')
        
class PrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prescription
        fields = ('id', 'cat', 'vet', 'med', 'date_prescribed', 'prescription_num', 'dosage', 'frequency', 'instructions')
        
class MedicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medication
        fields = ('id', 'name', 'prescribed_to', 'prescribed_by')
        
class VetVisitSerializer(serializers.ModelSerializer):
           
    class Meta:
        model = VetVisit
        fields = ('id', 'date_visited', 'next_appt_date', 'problem', 'cat', 'vet')









# # app/movies/serializers.py

# from rest_framework import serializers

# from .models import Foster

# class FosterSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Foster
#         fields = ('id', 'first_name', 'last_name', 'phone_num', 'email', 'address', 'city', 'state', 'zip_code')