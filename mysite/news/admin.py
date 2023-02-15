from django.contrib import admin
from news.models import Channel, Post


class ChannelAdmin(admin.ModelAdmin):
    pass


class PostAdmin(admin.ModelAdmin):
    pass


admin.site.register(Channel, ChannelAdmin)
admin.site.register(Post, PostAdmin)
