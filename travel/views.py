from .models import Travel
from .serializers import TravelSerializer
from rest_framework.viewsets import ModelViewSet, GenericViewSet


class TravelViewSet(ModelViewSet):
    queryset = Travel.objects.all()
    serializer_class = TravelSerializer
