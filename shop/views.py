from django.shortcuts import render

def shop_list(request):
    return render(request, 'shop/shop-grid-left.html')

def product_desc(request):
    return render(request, 'shop/shop-product-full.html')