from django.db import models
from django.utils.html import format_html


# Create your models here.
class zhuankebaba(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    keyword = models.CharField(max_length=255)
    source = models.CharField(max_length=50)
    title = models.CharField(max_length=510)
    post_on = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)
    tag = models.CharField(max_length=255)
    content = models.TextField()
    url = models.CharField(max_length=255)

    def __str__(self):
        return self.source

    class Meta:
        db_table = 'zhuankebaba'
        verbose_name = '赚客巴巴'
        verbose_name_plural = '赚客巴巴'

    def colored_type(self):
        color_code = 'red'
        return format_html(
            '<span style="color: {};">{}</span>',
            color_code,
            self.title
        )

    colored_type.short_description = 'title'
