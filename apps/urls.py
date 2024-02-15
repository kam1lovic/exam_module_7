from django.urls import path

from apps.views import ProductListView, ProductDeleteView

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('delete/<int:pk>', ProductDeleteView.as_view(), name='delete_product'),

]
