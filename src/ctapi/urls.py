from django.urls import path, include
from rest_framework import routers
from .views import FosterViewSet, CatViewSet, VetViewSet, MedicationViewSet, PrescriptionViewSet, VetVisitViewSet

# Routers defined
router = routers.DefaultRouter()
router.register(r'fosters', FosterViewSet)
router.register(r'cats', CatViewSet)
router.register(r'vets', VetViewSet)
router.register(r'medications', MedicationViewSet)
router.register(r'prescriptions', PrescriptionViewSet)
router.register(r'vetvisits', VetVisitViewSet)


# URL patterns defined
urlpatterns = [
    path('api/', include(router.urls)),
    path('', include(router.urls)),  
]






















# # app/ctapi/urls.py
# from django.urls import path, include
# from rest_framework import routers

# from .views import FosterList, FosterDetail


# urlpatterns = [
#     path("api/fosters/", FosterList.as_view()),
#     path("api/fosters/<int:pk>/", FosterDetail.as_view()),
# ]