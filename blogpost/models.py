from django.db import models


class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    writer_name = models.CharField(max_length=255)
    published_date = models.DateTimeField(auto_now_add=True)
    article_text = models.TextField(default='none')
    article_text_short = models.TextField(null=True, blank=True)
    active = models.BooleanField(default=True)
    article_image_name = models.ImageField(
        upload_to='articles/', null=True, blank=True
    )
