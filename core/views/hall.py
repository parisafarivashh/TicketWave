from rest_framework import viewsets

from ..models import Hall
from ..serializers.hall import HallSerializer


class HallViewSet(viewsets.ModelViewSet):
    queryset = Hall.objects.all()
    serializer_class = HallSerializer

