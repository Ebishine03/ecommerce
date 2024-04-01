from django.shortcuts import render
from .models import Products
from django.core.paginator import Paginator
# Create your views here.
def index(request):


    page_fr=1
    page_lt=1
    if request.GET:
        page_fr=request.GET.get('page_fr',1)
        page_lt=request.GET.get('page_lt',1)
    f_product_list=Products.objects.order_by('priority')[:8]
    l_products=Products.objects.order_by('-id')[:8]

    f_page_list=Paginator(f_product_list,4)
    l_page_list=Paginator(l_products,4)
    f_product_list=f_page_list.get_page(page_fr)
    l_products=l_page_list.get_page(page_lt)

    return render(request,'index.html',{'products_fr':f_product_list,'products_lt':l_products})
   


def list_products(request):
   
    page=1
    if request.GET:
        page=request.GET.get('page',1)
    product_list=Products.objects.all()
    page_list=Paginator(product_list,4)
    product_list=page_list.get_page(page)


    return render(request,'products.html',{'products':product_list})

def product_details(request,pk):
    product=Products.objects.get(pk=pk)


    return render(request,'product_details.html',{'products':product})
