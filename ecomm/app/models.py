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