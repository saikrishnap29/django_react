from rest_framework import serializers
from.models import lead

# Lead Serializer
class LeadSerializer(serializers.ModelSerializer):
  class Meta:
    model = lead
    fields = '__all__'