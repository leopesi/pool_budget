from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('orcamento', views.OrcamentoListView.as_view(), name='orcamento'),
    path('orcamento/<int:pk>', views.OrcamentoDetailView.as_view(), name='orcamento-id'),
    path('orcamento/<int:pk>/update/', views.OrcamentoUpdateView.as_view(), name='orcamento_update'),
    path('orcamento/<int:pk>/delete/', views.OrcamentoDeleteView.as_view(), name='orcamento_delete'),

    path('cliente', views.ClienteListView.as_view(), name='cliente'),
    path('cliente/create/', views.ClienteCreateView.as_view(), name='cliente_create'),
    path('cliente/<int:pk>', views.ClienteDetailView.as_view(), name='cliente-id'),
    path('cliente/<int:pk>/update/', views.ClienteUpdateView.as_view(), name='cliente_update'),
    path('cliente/<int:pk>/delete/', views.ClienteDeleteView.as_view(), name='cliente_delete'),
    path('dimensao_bulk', views.DimensaoBulk.as_view(), name='dimensao_bulk'),
]

