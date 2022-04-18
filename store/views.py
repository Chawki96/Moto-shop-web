from django.shortcuts import get_object_or_404, render

from django.http import HttpResponse

from store.models import Product
# Create your views here.
def index(request):
    products=Product.objects.all()
    return render(request,'index.html',context={"products":products})

def product_detail(request, slug):
    product = get_object_or_404(Product,slug=slug)
    return render(request,'detail.html',context={"product":product})