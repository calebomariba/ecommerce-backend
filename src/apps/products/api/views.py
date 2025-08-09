from rest_framework import viewsets
from rest_framework.filters import OrderingFilter, SearchFilter
from django.shortcuts import render
from ..models import Category, Product

from .serializers import CategorySerializer, ProductSerializer


def index(request):
    return render(request, "test/base.html")

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    # permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = ProductSerializer
    lookup_field = "slug"

    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["category__name", "name", "description"]
