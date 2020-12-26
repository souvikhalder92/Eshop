from typing import Dict, Any

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from shop.forms import SearchForm

from shop.models import Setting, ContactMessage,ContactForm
from Product.models import Product,Images,Category,Comment
from Orderapp.models import  ShopCart



def home(request):
     current_user=request.user
     cart_product = ShopCart.objects.filter(user_id=current_user.id)
     total_amount = 0
     for p in cart_product:
         total_amount += p.product.new_price * p.quantity
     category=Category.objects.all()
     setting=Setting.objects.get(id=3)
     sliding_images = Product.objects.all().order_by('id')[:3]
     lastest_products=Product.objects.all().order_by('id')[33:]
     products = Product.objects.all().order_by('id')[4:]
     jt_y = Product.objects.all().order_by('id')[8:16]
     flash = Product.objects.all().order_by('id')[18:27]
     tr = Product.objects.all().order_by('id')[27:37]
     mr = Product.objects.all().order_by('id')[36:43]
     total_quan = 0
     for p in cart_product:
         total_quan += p.quantity

     context={'category':category,'setting':setting,'sliding_images':sliding_images,'jt_y': jt_y,'flash':flash,
              'lastest_products' : lastest_products,'products':products,'tr':tr,'mr': mr,
              'cart_product':cart_product,'total_amount': total_amount}
     return  render(request,'home.html',context)
def about(request):
     category = Category.objects.all()
     setting = Setting.objects.get(id=3)
     context = {'category':category,'setting': setting}
     return render(request,'about.html',context)



def product_single(request,id):
     category = Category.objects.all()
     setting = Setting.objects.get(id=3)
     single_product=Product.objects.get(id=id)
     images = Images.objects.filter( product_id=id)
     products = Product.objects.all().order_by('id')[10:]
     comment_show = Comment.objects.filter(product_id=id,status='True')
     context={'category':category,'setting':setting,'single_product': single_product,
              'images': images,
              'products':products,
              'comment_show':comment_show
              }
     return render(request,'product-single.html', context)

def category_product(request,id,slug):
     sliding_images = Product.objects.all().order_by('id')[:3]
     setting = Setting.objects.get(id=3)
     category = Category.objects.all()
     product_cat=Product.objects.filter(category_id=id)
     context={'setting':setting,'category': category,
              'product_cat':product_cat,'sliding_images':sliding_images}
     return render(request,'category_product.html',context)
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = ContactMessage()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()


            return HttpResponseRedirect(reverse('contact_dat'))
    setting=Setting.objects.get(id=3)
    category = Category.objects.all()
    form = ContactForm

    context = {
         ' setting': setting,
         'category':category,
           'form': form,
    }
    return render(request,'contact_form.html', context)

def SearchView(request):
    if request.method == 'POST':
        form =SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            cat_id = form.cleaned_data['cat_id']
            if cat_id == 0:
                products = Product.objects.filter(title__icontains=query)
            else:
                products = Product.objects.filter(
                    title__icontains=query,category_id=cat_id)
            category = Category.objects.all()
            sliding_images = Product.objects.all().order_by('id')[:3]
            setting = Setting.objects.get(id=3)

            context = {
                'category': category,
                'query': query,
                'product_cat': products,
                'sliding_images': sliding_images,
                'setting': setting,
            }
            return render(request,'category_product.html', context)
        return HttpResponseRedirect('category_product')