from django.db import models
from django.contrib.auth.models import User
from bson.objectid import ObjectId

# Create your models here.
STATE_CHOICES = (
    ('Andhra Pradesh', 'Andhra Pradesh'),
    ('Arunachal Pradesh', 'Arunachal Pradesh'),
    ('Assam', 'Assam'),
    ('Bihar', 'Bihar'),
    ('Chhattisgarh', 'Chhattisgarh'),
    ('Goa', 'Goa'),
    ('Gujarat', 'Gujarat'),
    ('Haryana', 'Haryana'),
    ('Himachal Pradesh', 'Himachal Pradesh'),
    ('Jharkhand', 'Jharkhand'),
    ('Karnataka', 'Karnataka'),
    ('Kerala', 'Kerala'),
    ('Madhya Pradesh', 'Madhya Pradesh'),
    ('Maharashtra', 'Maharashtra'),
    ('Manipur', 'Manipur'),
    ('Meghalaya', 'Meghalaya'),
    ('Mizoram', 'Mizoram'),
    ('Nagaland', 'Nagaland'),
    ('Odisha', 'Odisha'),
    ('Punjab', 'Punjab'),
    ('Rajasthan', 'Rajasthan'),
    ('Sikkim', 'Sikkim'),
    ('Tamil Nadu', 'Tamil Nadu'),
    ('Telangana', 'Telangana'),
    ('Tripura', 'Tripura'),
    ('Uttar Pradesh', 'Uttar Pradesh'),
    ('Uttarakhand', 'Uttarakhand'),
    ('West Bengal', 'West Bengal')
)

CATEGORY_CHOICES=(

('MU', 'Makeup Products'),

('SC', 'Skincare Products'),

('HC', 'HairCare Products'),

('BC', 'BodyCare Products'),

('FG', 'Fragrances'),

)


class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models. FloatField()
    discounted_price= models.FloatField()
    description = models.TextField()
    composition = models. TextField(default='')
    shade_color = models.TextField(default='')
    key_features = models.TextField(default='')
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2, default='UN')

    product_image = models. ImageField(upload_to='product')
    def __str__(self):
        return self.title
    

class Customer(models.Model):
    id = models.CharField(primary_key=True, max_length=24, default=str(ObjectId()),editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200) 
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    mobile = models.IntegerField(default=0)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES, max_length=100)
    def __str__(self):
        return self.name
    

class Cart(models. Model):
    user = models.ForeignKey (User, on_delete=models.CASCADE)
    product = models.ForeignKey (Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price 
    
STATUS_CHOICES = (
('Accepted', 'Accepted'),
('Packed', 'Packed'),
('On The Way', 'On The Way'),
('Delivered', 'Delivered'),
('Cancel', 'Cancel'),
('Pending', 'Pending'),
)

class Payment(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    amount =models.FloatField()
    razorpay_order_id = models.CharField(max_length=100, blank=True, null=True)
    razorpay_payment_status = models. CharField(max_length=100, blank=True, null=True)
    razorpay_payment_id= models. CharField(max_length=100, blank=True, null=True)
    paid= models.BooleanField(default=False)

    

class OrderPlaced(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50,choices=STATUS_CHOICES,default='Pending')
    #payment = models.ForeignKey(Payment,on_delete=models.CASCADE,default="")
    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price
    


class Wishlist(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)


class ReviewRating(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100,blank=True)
    review = models.TextField(max_length=506, blank=True)
    rating = models.FloatField()
    ip = models.CharField(max_length=20, blank=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def _str_(self):
        return self.subject