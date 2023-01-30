from rest_framework.generics import CreateAPIView, GenericAPIView

from product.permissions import IsAuthor
from rating.models import Review
from . import serializers
from rest_framework import mixins, permissions


class UpdateDestroyAPIView(mixins.UpdateModelMixin, mixins.DestroyModelMixin, GenericAPIView):

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class ReviewCreateApiView(CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = serializers.ReviewSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ReviewUpdateDeleteApiView(UpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = serializers.ReviewUpdateSerializer
    permission_classes = (permissions.IsAuthenticated, IsAuthor)




