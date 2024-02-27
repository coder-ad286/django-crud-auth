from django.urls import path
from .views import apiOverview,FetchProductsView,FetchProductView,CreateProductView,UpdateProductView,DeleteProductView

urlpatterns=[
    path("",apiOverview,name="api-overview"),
    path('fetch-products/',FetchProductsView.as_view(),name="fetch-products"),
    path('fetch-product/<int:id>',FetchProductView.as_view(),name="fetch-products"),
    path('create-product/',CreateProductView.as_view(),name="create-product"),
    path('update-product/<int:id>',UpdateProductView.as_view(),name="update-product"),
    path('delete-product/<int:id>',DeleteProductView.as_view(),name="delete-product")
]