from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Product
from category.models import Category


def store(request, category_slug=None):
    if category_slug != None:
        category = get_object_or_404(Category, slug =category_slug)
        products = Product.objects.filter(category=category, is_available=True)
        product_count = products.count()
        page = request.GET.get('page')  # requested page number
        paginator = Paginator(products, 1)  # prepare to set pages(each have 3 records):
        paged_products = paginator.get_page(page)
    else:
        products = Product.objects.filter(is_available=True).order_by('id')
        product_count = products.count()
        page = request.GET.get('page')  # requested page number
        paginator = Paginator(products, 3)  # prepare to set pages(each have 3 records):
        paged_products = paginator.get_page(page)
    context = {'products': paged_products, 'product_count': product_count}
    return render(request, 'store/store.html', context)


def product_detail(request, category_slug, product_slug):
    try:
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
    except Exception as e:
        raise e
    context = {'single_product': single_product}
    return render(request, 'store/product_detail.html', context)
