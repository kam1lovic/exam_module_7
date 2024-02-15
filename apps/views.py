from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView

from apps.models import ProductModel


class ProductListView(ListView):
    template_name = 'apps/index.html'
    model = ProductModel
    context_object_name = 'products'
    paginate_by = 4


class ProductDeleteView(DeleteView):
    template_name = 'apps/delete_product.html'
    model = ProductModel
    queryset = ProductModel.objects.all()
    success_url = reverse_lazy('index')
