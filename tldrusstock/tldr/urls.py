from django.urls import path
from . import views
# from .api import TldrViewSet
# from rest_framework import routers

# router = routers.DefaultRouter()
# router.register('', TldrViewSet, 'tldr')

# urlpatterns = router.urls
urlpatterns = [
  path('tldr/submit', views.submit, name='submit')
]