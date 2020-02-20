from django.db import models
from django.utils.html import format_html


# Create your models here.
class Weibo(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    keyword = models.CharField(max_length=255)
    source = models.CharField(max_length=50)
    comment = models.TextField()
    title = models.TextField()
    url = models.CharField(max_length=255)
    crawl_date = models.CharField(max_length=255)

    def __str__(self):
        return self.source

    class Meta:
        db_table = 'weibo'
        verbose_name = '微博'
        verbose_name_plural = '微博'

    def colored_type(self):
        color_code = 'red'
        return format_html(
            '<span style="color: {};">{}</span>',
            color_code,
            self.title
        )

    colored_type.short_description = 'title'
