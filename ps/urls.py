from django.urls import include, path
from rest_framework import routers
from ps.positions import views

router = routers.DefaultRouter()
router.register(r'ships', views.ShipViewSet)
router.register(r'positions', views.PositionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]