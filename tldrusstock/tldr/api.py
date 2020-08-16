from tldr.models import Tldr
from rest_framework import viewsets, permissions
from .serializers import TldrSerializer

# Viewset
# class TldrViewSet(viewsets.ModelViewSet):
#   queryset = Tldr.objects.all()
#   permission_classes = [
#     permissions.AllowAny
#   ]
#   serializer_class = TldrSerializer