from django.db import models
from django.utils.html import format_html


# Create your models here.
class Pojie(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    keyword = models.CharField(max_length=255)
    source = models.CharField(max_length=50)
    title = models.CharField(max_length=510)
    user_name = models.CharField(max_length=255)
    user_homepage = models.CharField(max_length=255)
    post_on = models.CharField(max_length=255)
    content = models.TextField()
    url = models.CharField(max_length=255)

    def __str__(self):
        return self.source

    class Meta:
        db_table = 'pojie'
        verbose_name = '吾爱破解'
        verbose_name_plural = '吾爱破解'

    def colored_type(self):
        color_code = 'red'
        return format_html(
            '<span style="color: {};">{}</span>',
            color_code,
            self.title
        )

    colored_type.short_description = 'title'
