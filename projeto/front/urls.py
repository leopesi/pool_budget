from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('orcamento', views.OrcamentoListView.as_view(), name='orcamento'),
    path('orcamento/<int:pk>', views.OrcamentoDetailView.as_view(), name='orcamento-detalhado'),
    path('orcamento/create/', views.OrcamentoCreateView.as_view(), name='orcamento_create'),

    path('orcamento/<int:pk>/revest-update/', views.OrcamentoUpdateView.as_view(), name='orcamento_update'),

    path('cliente', views.ClienteListView.as_view(), name='cliente'),
    path('cliente/<int:pk>', views.ClienteDetailView.as_view(), name='cliente-detalhado'),
    path('cliente/<int:pk>/update/', views.ClienteUpdateView.as_view(), name='cliente_update'),
    ]
