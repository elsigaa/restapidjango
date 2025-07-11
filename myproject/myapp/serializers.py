from rest_framework import serializers
from .models import Customer, Helmet, Transaction

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class HelmetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Helmet
        fields = '__all__'

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'
