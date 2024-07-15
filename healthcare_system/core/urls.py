from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import PatientViewSet, AppointmentViewSet, MedicalRecordViewSet, BillingViewSet, InsuranceClaimViewSet

router = DefaultRouter()
router.register(r'patients', PatientViewSet)
router.register(r'appointments', AppointmentViewSet)
router.register(r'medical-records', MedicalRecordViewSet)
router.register(r'billings', BillingViewSet)
router.register(r'insurance-claims', InsuranceClaimViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
