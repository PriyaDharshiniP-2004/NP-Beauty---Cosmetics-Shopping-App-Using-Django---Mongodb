from django.contrib import admin

# Register your models here.
from . models import Product, Customer, Cart, Payment, OrderPlaced, Wishlist, ReviewRating

#Register your models here.

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin): 
    list_display = ['id', 'title', 'selling_price','discounted_price', 'description','composition','shade_color','key_features','category', 'product_image']


@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin): 
    list_display = ['id', 'user', 'locality','city', 'state','zipcode']


@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','product','quantity']


@admin.register(Payment)
class PaymentModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','amount','razorpay_order_id','razorpay_payment_status','razorpay_payment_id','paid']

    
@admin.register(OrderPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','customer','product','quantity','ordered_date','status']

@admin.register(Wishlist)
class WishlistModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','product']

@admin.register(ReviewRating)
class ReviewRatingModelAdmin(admin.ModelAdmin):
    list_display=['id','product','user','created_at','updated_at']
