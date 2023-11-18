from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Pool
from .serializers import PoolSerializer

class PoolViewSet(viewsets.ModelViewSet):
    queryset = Pool.objects.all()
    serializer_class = PoolSerializer

    @action(detail=False, methods=['POST'])
    def create_pool(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['GET'])
    def get_pool(self, request, pk=None):
        pool = self.get_object()
        serializer = self.get_serializer(pool)
        return Response(serializer.data)

    @action(detail=True, methods=['PUT', 'PATCH'])
    def update_pool(self, request, pk=None):
        pool = self.get_object()
        serializer = self.get_serializer(pool, data=request.data, partial=True)  # partial=True allows partial updates
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['DELETE'])
    def delete_pool(self, request, pk=None):
        pool = self.get_object()
        pool.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)