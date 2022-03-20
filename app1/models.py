from django.db import models

# Create your models here.

# class Company_data(models.Model):
class User_data(models.Model):
    com_name = models.CharField(default="",max_length=200)
    com_em = models.EmailField(default="",max_length=200)
    com_cno = models.PositiveIntegerField(default=0)
    com_add = models.TextField(default="")
    join_date = models.DateField(auto_now=True,blank=True,null=True)
    profile = models.ImageField(upload_to="Comp_Profile/",default="",max_length=300,blank=True,null=True)
    com_pass = models.CharField(default="",max_length=200)

# class Products(models.Model):
#     name = models.CharField(max_length=60)
#     price = models.IntegerField(default=0)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
#     description = models.CharField(
#         max_length=250, default='', blank=True, null=True)
#     image = models.ImageField(upload_to='uploads/products/')
  
#     @staticmethod
#     def get_products_by_id(ids):
#         return Products.objects.filter(id__in=ids)
  
#     @staticmethod
#     def get_all_products():
#         return Products.objects.all()
  
#     @staticmethod
#     def get_all_products_by_categoryid(category_id):
#         if category_id:
#             return Products.objects.filter(category=category_id)
#         else:
#             return Products.get_all_products()


# class CheckOut(View):
#     def post(self, request):
#         address = request.POST.get('address')
#         phone = request.POST.get('phone')
#         customer = request.session.get('customer')
#         cart = request.session.get('cart')
#         products = Products.get_products_by_id(list(cart.keys()))
#         print(address, phone, customer, cart, products)
  
#         for product in products:
#             print(cart.get(str(product.id)))
#             order = Order(customer=Customer(id=customer),
#                           product=product,
#                           price=product.price,
#                           address=address,
#                           phone=phone,
#                           quantity=cart.get(str(product.id)))
#             order.save()
#         request.session['cart'] = {}
  
#         return redirect('cart')
