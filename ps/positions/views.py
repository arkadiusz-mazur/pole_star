from rest_framework import viewsets
from rest_framework import permissions
from ps.positions.serializers import ShipSerializer, PositionSerializer
from ps.positions.models import Ship, Position
from rest_framework.permissions import AllowAny
from rest_framework.decorators import authentication_classes, permission_classes

@permission_classes((AllowAny, ))
class ShipViewSet(viewsets.ModelViewSet):
    queryset = Ship.objects.all()
    serializer_class = ShipSerializer
    permission_classes = [permissions.IsAuthenticated]

@permission_classes((AllowAny, ))
class PositionViewSet(viewsets.ModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Position.objects.all()
        get_imo = self.request.query_params.get('imo')

        if get_imo:
            queryset = queryset.filter(imo=get_imo)
        return queryset