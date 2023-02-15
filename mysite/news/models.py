from django.db import models


class Channel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"


class Post(models.Model):
    tg_id = models.BigIntegerField()
    channel_id = models.ForeignKey(
        Channel, on_delete=models.SET_NULL, null=True, related_name="posts"
    )
    text = models.TextField()
    image = models.ImageField(upload_to="news/images", null=True, blank=True)
    posted_at = models.DateTimeField()
    models.UniqueConstraint("tg_id", "channel", name="unique_id")

    def __str__(self) -> str:
        return f"{self.channel_id.name} - {self.tg_id} - {self.text:50.50}..."
