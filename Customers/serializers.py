from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User, Parcel, DeliveryProof

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            role=validated_data['role']
        )
        return user

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(
        max_length=128,
        write_only=True
    )

    def validate(self, attrs):
        username = attrs.get('username', '')
        password = attrs.get('password', '')

        if username and password:
            user = User.objects.filter(username=username).first()

            if user and user.check_password(password):
                refresh = RefreshToken.for_user(user)
                return {
                    'username': user.username,
                    'email': user.email,
                    'role': user.role,
                    'tokens': {
                        'refresh': str(refresh),
                        'access': str(refresh.access_token),
                    }
                }
            else:
                raise serializers.ValidationError('Invalid username or password.')
        else:
            raise serializers.ValidationError('Both username and password are required.')

class ParcelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parcel
        exclude = ['sender']
        # fields = '__all__'


class CourierSerializer(serializers.ModelSerializer):
    parcel_title = serializers.CharField(source='parcel.title', read_only=True)

    class Meta:
        model = DeliveryProof
        fields = ['id', 'status',  'timestamp', 'parcel', 'parcel_title']