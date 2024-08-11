from django.shortcuts import render, get_object_or_404
from cart.forms import CartAddProductForm
from .models import Category, Product

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)

    # Lógica de búsqueda
    query = request.GET.get('q')  # Obtén el término de búsqueda
    if query:  # Si hay un término de búsqueda
        products = products.filter(name__icontains=query)  # Filtra los productos por nombre

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    return render(request,
                  'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products,
                   'query': query})  # Pasa la consulta al contexto

def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    return render(request,
                  'shop/product/detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form})
