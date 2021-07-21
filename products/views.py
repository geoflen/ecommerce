from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Product


def index(request):
    products = Product.objects.all()
    product_paginator = Paginator(products, 6)
    page_number = request.GET.get('page')
    page = product_paginator.page(page_number)
    # Todo if more than 5 pages, display median page numbers
    pages_list = [num for num in range(1, product_paginator.num_pages + 1)]
    active = "active"
    context = {
        'page': page,
        'page_list': pages_list,
        'active': active,
    }

    return render(request, 'index.html', context)
