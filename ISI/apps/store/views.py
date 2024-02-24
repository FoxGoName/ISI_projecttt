from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from .models import Product, Category
# Create your views here.
def product_detail(request, category_slug, slug):
    product = get_object_or_404(Product, slug=slug)

    context = {
        'product':product
    }

    return render(request, 'product_detail.html', context)

def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = category.products.all()

    context = {
        'category': category,
        'products': products
    }

    return render(request, 'category_detail.html', context)

class productCreateView(CreateView):
    model = Product
    template_name = "add_product.html"
    fields = '__all__'

    def get_success_url(self):
        return reverse("frontpage")

class editProductView(UpdateView):
    model = Product
    template_name = "edit_product.html"
    fields = '__all__'

    def get_success_url(self):
        product = self.object  # 获取正在编辑的产品对象
        return reverse("product_detail", kwargs={'category_slug': product.category.slug, 'slug': product.slug})

class deleteProductView(DeleteView):
    model = Product
    template_name = "delete_product.html"
    success_url = reverse_lazy('frontpage')