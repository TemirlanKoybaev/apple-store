from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render

from .models import Product, Category


def product_list(request, category_slug=None):
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    selected_category = None

    # фильтр по категории
    if category_slug:
        selected_category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=selected_category)

    # поиск
    query = request.GET.get("q", "").strip()
    if query:
        products = products.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )

    # сортировка
    sort = request.GET.get("sort", "default")
    if sort == "price_asc":
        products = products.order_by("price")
    elif sort == "price_desc":
        products = products.order_by("-price")
    else:
        products = products.order_by("id")  # стабильный порядок по умолчанию

    # пагинация
    paginator = Paginator(products, 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "categories": categories,
        "selected_category": selected_category,
        "products": page_obj,
        "page_obj": page_obj,
        "query": query,
        "sort": sort,
    }
    return render(request, "product_list.html", context)

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, available=True)
    return render(request, "product_detail.html", {"product": product})

def cart_add_stub(request, product_id):
    return HttpResponse(f"Cart stub: add product_id={product_id}")


def contact_page(request):
    return render(request, "contact.html")

