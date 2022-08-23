from django.urls import path
from fireapp.views import GoodsView, LinksView


urlpatterns = [
    path('api/goods/', GoodsView.as_view(), name='goods'),
    path('api/links/', LinksView.as_view(), name='links'),
]