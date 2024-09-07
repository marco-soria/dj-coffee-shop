from django.urls import reverse_lazy
from django.views import generic
from rest_framework.views import APIView
from rest_framework.response import Response

from products.models import Product
from .forms import ProductForm


# Create your views here.
class ProductFormView(generic.FormView):
    template_name = "add_product.html"
    form_class = ProductForm
    success_url = reverse_lazy("add_product")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)