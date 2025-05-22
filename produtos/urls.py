from django.urls import path, include
from rest_framework import routers
from . import views
from .api import ProdutoViewSet

router = routers.DefaultRouter()
router.register(r'api/produtos', ProdutoViewSet)

urlpatterns = [
    # rotas da itnerface web
    path('', views.listar_produtos, name='lista_produtos'),
    path('novo/', views.criar_produto, name='criar_produto'),
    path('editar/<int:id>/', views.editar_produto, name='editar_produto'),
    path('excluir/<int:id>/', views.excluir_produto, name='excluir_produto'),

    #rotas da api
    path('', include(router.urls)),
]