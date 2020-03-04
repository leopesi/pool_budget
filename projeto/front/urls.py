from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('orcamento', views.OrcamentoListView.as_view(), name='orcamento'),
    path('orcamento/<int:pk>', views.OrcamentoDetailView.as_view(), name='orcamento-detalhado'),
    ]
