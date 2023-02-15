from django.shortcuts import render
from rest_framework.generics import ListAPIView
from django_filters import rest_framework as filters

from api.serializers import PostListSerializer
from news.models import Post
from api.filters import PostFilters


class PostListView(ListAPIView):
    serializer_class = PostListSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = PostFilters

    def get_queryset(self):
        if getattr(self, "swagger_fake_view", False):  # fake view for swagger-ui
            return Post.objects.none()
        qs = Post.objects.all()
        return qs
