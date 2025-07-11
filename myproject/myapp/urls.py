from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .controller import CustomerViewSet, HelmetViewSet, TransactionViewSet
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register('customers', CustomerViewSet)
router.register('helmets', HelmetViewSet)
router.register('transactions', TransactionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('token/', obtain_auth_token, name='api_token_auth'),
]
