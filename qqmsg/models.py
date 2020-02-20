from django.db import models
from django.utils.html import format_html


# Create your models here.
class QqMsg(models.Model):
    id = models.CharField(primary_key=True, max_length=50, null=False)
    source = models.CharField(max_length=50, null=False)
    msg_id = models.CharField(max_length=50)
    type = models.CharField(max_length=25, null=False)
    qq = models.CharField(max_length=25, null=False)
    gc = models.CharField(max_length=25)
    gn = models.CharField(max_length=255)
    owner = models.CharField(max_length=25)
    nick = models.CharField(max_length=255)
    l_nick = models.TextField()
    phone = models.CharField(max_length=25)
    city = models.CharField(max_length=25)
    occupation = models.CharField(max_length=25)
    avatar = models.CharField(max_length=255)
    email = models.CharField(max_length=50)
    mobile = models.CharField(max_length=25)
    image = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.source

    class Meta:
        db_table = 'qqmsg'
        verbose_name = 'QQ消息'
        verbose_name_plural = 'QQ消息'

    def colored_type(self):
        color_code = 'red'
        return format_html(
            '<span style="color: {};">{}</span>',
            color_code,
            self.gn
        )

    colored_type.short_description = 'gn'
