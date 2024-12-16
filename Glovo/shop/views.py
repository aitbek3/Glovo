from rest_framework import viewsets, generics, status
from rest_framework.filters import SearchFilter
from .serialazers import *
from .models import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView, token_blacklist
from rest_framework_simplejwt.tokens import RefreshToken
from django.http import HttpResponseRedirect


class RegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CustomLoginView(TokenObtainPairView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception:
            return Response({'detail': 'Невреные учетные данные'}, status=status.HTTP_401_UNAUTHORIZED)

        user = serializer.validated_data
        return Response(serializer.data, status=status.HTTP_200_OK)


class LogoutView(generics.GenericAPIView):
    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data['refresh']
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class UserProfileViewSets(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializers


class CategoryViewSets(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers


class FoodViewSets(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializers
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['category', 'resto_name', 'price']
    search_fields = ['resto_name']


class CourierViewSets(viewsets.ModelViewSet):
    queryset = Courier.objects.all()
    serializer_class = CourierSerializers


class OrderViewSets(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializers


class DeliveryViewSets(viewsets.ModelViewSet):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializers


class RatingViewSets(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializers


class ReviewViewSets(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializers

