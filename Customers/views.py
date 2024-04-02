from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .models import User, Parcel, DeliveryProof
from .serializers import UserSerializer, ParcelSerializer, CourierSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import IsOwnerOrAdmin, CustomerPermissions, CourierPermissions, AdminPermissions, ParcelPermissions
from .filters import ParcelFilter, SenderFilter
from django_filters.rest_framework import DjangoFilterBackend

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [CustomerPermissions | IsOwnerOrAdmin]

class ParcelViewSet(viewsets.ModelViewSet):
    queryset = Parcel.objects.all()
    serializer_class = ParcelSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [ParcelPermissions | AdminPermissions]
    filter_backends = [DjangoFilterBackend]
    filterset_class = SenderFilter

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)


class CourierViewSet(viewsets.ModelViewSet):
    serializer_class = CourierSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [CourierPermissions | AdminPermissions]
    filter_backends = [DjangoFilterBackend]
    filterset_class = ParcelFilter

    def get_queryset(self):
        queryset = DeliveryProof.objects.all()
        courier_id = self.request.user.id

        if courier_id:
            queryset = queryset.filter(parcel__courier_id=courier_id)

        return queryset

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        try:
            serializer.save()
            return Response(serializer.data)
        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)
