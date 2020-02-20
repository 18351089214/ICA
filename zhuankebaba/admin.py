from django.contrib import admin

from .models import *

# 修改title和header
admin.site.site_title = 'ICA后台管理'
admin.site.site_header = 'ICA'


# Register your models here.
class ZhuankebabaAdmin(admin.ModelAdmin):
    # 设置模型字段，用于Admin后台数据的表头设置
    list_display = ['keyword', 'colored_type', 'post_on', 'category', 'contact', 'content', 'url']
    # 设置可搜索的字段并在Admin后台数据生成搜索框，如有外键，应使用双下划线连接两个模型的字段
    search_fields = ['content']
    # 设置过滤器，在后台数据的右侧生成导航栏，如有外键，应使用双下划线连接两个模型的字段
    list_filter = ['post_on']
    # 设置排序方式，['create_time']为升序，['-create_time']为降序
    ordering = ['-post_on']
    # 设置时间选择器， 字段中有时间格式才可以使用
    # date_hierarchy = ['modify_time']


admin.site.register(zhuankebaba, ZhuankebabaAdmin)
