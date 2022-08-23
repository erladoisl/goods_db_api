from django.urls import path
from fireapp.views import GoodsView


urlpatterns = [
    path('api/goods/', GoodsView.as_view(), name='goods'),
    path('api/auth/', GoodsView.as_view(), name='goods'),
]