from rest_framework import viewsets

# from .models import Foster
# from .serializers import FosterSerializer


from .models import Foster, Cat, Vet, Medication, VetVisit, Prescription
from .serializers import FosterSerializer, CatSerializer,VetSerializer, MedicationSerializer, VetVisitSerializer, PrescriptionSerializer 

class FosterViewSet(viewsets.ModelViewSet):
    
    queryset = Foster.objects.all()
    serializer_class = FosterSerializer
    
class CatViewSet(viewsets.ModelViewSet):
    
    queryset = Cat.objects.all()
    serializer_class = CatSerializer

class VetViewSet(viewsets.ModelViewSet):
    
    queryset = Vet.objects.all()
    serializer_class = VetSerializer
    
class MedicationViewSet(viewsets.ModelViewSet):
    
    queryset = Medication.objects.all()
    serializer_class = MedicationSerializer
    
class PrescriptionViewSet(viewsets.ModelViewSet):
    
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer
    
class VetVisitViewSet(viewsets.ModelViewSet):
    
    queryset = VetVisit.objects.all()
    serializer_class = VetVisitSerializer














# from django.shortcuts import render
# # app/Fosters/views.py

# from django.http import Http404
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status

# from .models import Foster
# from .serializers import FosterSerializer


# class FosterList(APIView):
#     def post(self, request, format=None):
#         serializer = FosterSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# class FosterDetail(APIView):
#     def get_object(self, pk):
#         try:
#             return Foster.objects.get(pk=pk)
#         except Foster.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         Foster = self.get_object(pk)
#         serializer = FosterSerializer(Foster)
#         return Response(serializer.data)