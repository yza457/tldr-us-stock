from rest_framework import serializers
from tldr.models import Tldr

class TldrSerializer(serializers.ModelSerializer):
  class Meta:
    model = Tldr
    fields = '__all__'