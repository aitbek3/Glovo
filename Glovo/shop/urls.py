from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'userprofile', UserProfileViewSets, basename='userprofile')
router.register(r'category', CategoryViewSets, basename='category')
router.register(r'food', FoodViewSets, basename='food')
router.register(r'courier', CourierViewSets, basename='courier')
router.register(r'order', OrderViewSets, basename='order')
router.register(r'delivery', DeliveryViewSets, basename='delivery')
router.register(r'rating', RatingViewSets, basename='rating')
router.register(r'review', ReviewViewSets, basename='review')

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', include(router.urls)),
]



