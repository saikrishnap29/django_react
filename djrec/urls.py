from django.urls import path
from.import views
from rest_framework import routers
from.api import LeadViewset
router = routers.DefaultRouter()
router.register('api/leads',LeadViewset,'leads')
urlpatterns = router.urls