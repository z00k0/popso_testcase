from django_filters import rest_framework as filters

from news.models import Post


class ChannelFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class PostFilters(filters.FilterSet):
    date = filters.DateFilter(field_name="posted_at__date", lookup_expr="exact")
    channel = ChannelFilter(field_name="channel_id__name", lookup_expr="in")

    class Meta:
        model = Post
        fields = ["date", "channel"]
