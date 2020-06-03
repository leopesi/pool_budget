from django.urls import path
from . import views

urlpatterns = [
    path('produto',views.ProdutoListView.as_view(), name='produto'),
    path('produto/create/', views.add_produto, name='produto_create'),
    path('produto/<int:pk>', views.ProdutoDetailView.as_view(), name='produto-id'),
    path('produto/<int:pk>/update/', views.ProdutoUpdateView.as_view(), name='produto_update'),
    path('produto/<int:pk>/delete/', views.ProdutoDeleteView.as_view(), name='produto_delete'),
   ]

