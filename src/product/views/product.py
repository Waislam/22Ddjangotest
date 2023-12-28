from django.views import generic
from django.views.generic.list import ListView
from django.core.paginator import Paginator

from product.models import Variant, Product, Variant, ProductVariant, ProductVariantPrice


class CreateProductView(generic.TemplateView):
    template_name = 'products/create.html'

    def get_context_data(self, **kwargs):
        context = super(CreateProductView, self).get_context_data(**kwargs)
        variants = Variant.objects.filter(active=True).values('id', 'title')
        context['product'] = True
        context['variants'] = list(variants.all())
        return context


class ProductListView(ListView):
    model = Product
    template_name = 'products/list.html'
    context_object_name =  'products'
    paginate_by = 2


    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["variant_price"] = ProductVariantPrice.objects.all()
        return  context


