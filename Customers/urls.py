from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import CustomerViewSet, ParcelViewSet, CourierViewSet

# router = DefaultRouter()
# router.register(r'users', CustomerViewSet)
# router.register(r'api/parcel', ParcelViewSet, basename='parcel')
# router.register(r'api/courier', CourierViewSet, basename='courier')


urlpatterns = [
    # path('', include(router.urls)),
    path('api/users/',CustomerViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('api/users/<int:pk>/', CustomerViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('api/parcel/', ParcelViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('api/parcel/<int:pk>/', ParcelViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('api/courier/', CourierViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('api/courier/<int:pk>/', CourierViewSet.as_view({'get': 'retrieve', 'put': 'update'})),
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
]
