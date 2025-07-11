from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.name

class Helmet(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    brand = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    is_cleaned = models.BooleanField(default=False)
    is_picked_up = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.brand} - {self.color}"

class Transaction(models.Model):
    PAYMENT_METHOD_CHOICES = [
        ('cash', 'Cash'),
        ('transfer', 'Transfer'),
    ]

    helmet = models.ForeignKey(Helmet, on_delete=models.CASCADE)
    service_type = models.CharField(max_length=20, choices=[('penitipan', 'Penitipan'), ('laundry', 'Laundry')])
    price = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=10, choices=PAYMENT_METHOD_CHOICES)
    transaction_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.service_type} - {self.helmet}"
