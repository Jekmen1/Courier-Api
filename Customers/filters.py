from django_filters import rest_framework as filters
from .models import Parcel, DeliveryProof
class SenderFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr="icontains")
    receiver_address = filters.CharFilter(lookup_expr="icontains")
    courier = filters.CharFilter(lookup_expr="icontains")
    class Meta:
        model = Parcel
        fields = ['title', 'receiver_address', 'courier']
class ParcelFilter(filters.FilterSet):
    parcel = filters.CharFilter(lookup_expr="icontains")
    status = filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = DeliveryProof
        fields = ['parcel', 'status']