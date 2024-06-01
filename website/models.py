from django.db import models
from django.core.validators import MinValueValidator

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Use two decimal places for currency
    description = models.TextField(blank=True)  # Optional product description

    def __str__(self):
        return self.name

class Order(models.Model):

    def get_total_price(self):
        return sum(item.total_price for item in self.items.all())

    customer_name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)  # Optional email for customer contact
    phone_number = models.CharField(max_length=20)  # Allow for international formats
    created_at = models.DateTimeField(auto_now_add=True)
    order_delivery_date = models.DateTimeField()
    payment_status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('paid', 'Paid'),
        ('cancelled', 'Cancelled')
    ], default='pending')
    delivery_status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered')
    ], default='pending')



    def __str__(self):
        return f"Order {self.pk} - {self.customer_name} - Delivery date  {self.order_delivery_date}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)]) 
    unit_price = models.DecimalField(max_digits=10, decimal_places=2) 

    def __str__(self):
        return f"{self.quantity}x {self.product.name} (Order {self.order.pk})"

    def save(self, *args, **kwargs):
        self.unit_price = self.product.price  # Update unit price if product price changes
        self.total_price = self.quantity * self.unit_price
        super().save(*args, **kwargs)
    

