from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    address = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Driver(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    license_number = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Project(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='projects')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.title} ({self.customer.name})"

class Delivery(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='deliveries')
    driver = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True, blank=True, related_name='deliveries')
    delivery_date = models.DateField()
    status = models.CharField(max_length=50, choices=[
        ('scheduled', 'Scheduled'),
        ('in_transit', 'In Transit'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    ])
    remarks = models.TextField(blank=True)

    def __str__(self):
        return f"Delivery on {self.delivery_date} for {self.project.title}"