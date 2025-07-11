from rest_framework import viewsets
from .models import Customer, Helmet, Transaction
from .serializers import CustomerSerializer, HelmetSerializer, TransactionSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class HelmetViewSet(viewsets.ModelViewSet):
    queryset = Helmet.objects.all()
    serializer_class = HelmetSerializer

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer




