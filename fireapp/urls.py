from django.urls import path
from fireapp.views import GoodsView, LinksView, PricesView, FoldersView


urlpatterns = [
    path('api/goods/', GoodsView.as_view(), name='goods'),
    path('api/links/', LinksView.as_view(), name='links'),
    path('api/prices/', PricesView.as_view(), name='prices'),
    path('api/folders/', FoldersView.as_view(), name='folders'),
]