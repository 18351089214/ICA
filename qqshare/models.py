from django.db import models
from django.utils.html import format_html


# Create your models here.
class QQShare(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    create_time = models.CharField(max_length=25)
    filename = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    modify_time = models.CharField(max_length=25)
    owner_nick = models.CharField(max_length=255)
    owner_uin = models.CharField(max_length=25)
    upload_nick = models.CharField(max_length=255)
    upload_uin = models.CharField(max_length=25)
    filepath = models.CharField(max_length=255)
    gc = models.CharField(max_length=25)

    def __str__(self):
        return self.filename

    class Meta:
        db_table = 'qqshare'
        verbose_name = '群空间'
        verbose_name_plural = '群空间'

    def colored_type(self):
        color_code = 'red'
        return format_html(
            '<span style="color: {};">{}</span>',
            color_code,
            self.filename
        )

    colored_type.short_description = 'filename'
