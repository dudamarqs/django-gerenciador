from rest_framework import viewsets, serializers
from .models import Produto

# Serializer - tranforma objetos em JSON e vice-versa
class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'

# ViewSet - cria os endpoits CRUD automaticamente
class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

