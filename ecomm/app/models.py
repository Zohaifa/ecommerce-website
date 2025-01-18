from django.db import models
from django.contrib.auth.forms import User

# Create your models here.
CATEGORY_CHOICES=(
('QR', 'Quran'),
('SH', 'Sihah Sittah'),
('HH', 'Hadith Books'),
('DU', 'Dua Compilation'),
)
STATE_CHOICES=(
    ('Chittagong', 'Chittagong'),
    ('Dhaka', 'Dhaka'),
    ('Sylhet', 'Sylhet'),
    ('Barisal', 'Barisal'),
    ('Khulna', 'Khulna'),
    ('Rajshahi', 'Rajshahi'),
    ('Rangpur', 'Rangpur')
)
class Product(models.Model):
    title= models.CharField(max_length=100)
    selling_price = models.FloatField() 
    discounted_price = models.FloatField() 
    description= models.TextField()
    composition = models.TextField(default='')
    prodapp = models.TextField(default='')
    category =models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    product_image = models.ImageField(upload_to='product')
    
    def _str_(self):
        return self.title
    

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    mobile = models.IntegerField(default=0)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES, max_length=108)
    
    def _str_(self):
        return self.name
    
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey (Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price

STATUS_CHOICES = (
    ('Paid', 'Paid'),
    ('Accepted', 'Accepted'),
    ('Packed', 'Packed'),
    ('On The Way', 'On The Way'),
    ('Delivered', 'Delivered'),
    ('Cancel', 'Cancel'),
    ('Pending', 'Pending'),
)

class OrderPlaced(models.Model):
    user = models.ForeignKey (User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending')
    payment_status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')

    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price
    
class BillingAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=40, blank=True, null=True)
    country=models.CharField(max_length=100, blank=True, null=True)
    address1 = models.CharField(max_length=200, blank=True, null=True)
    address2 = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    zipcode = models.CharField(max_length=15, blank=True, null=True)
    phone_number = models.CharField(max_length=16, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s billing address."
    
    def is_fully_fileld(self):
        field_names = {f.name_ for f in self._meta.get_fields()}
        for field_name in field_names:
            value = getattr(self.field_name)
            if value is None or value == "":
                return False
        return True