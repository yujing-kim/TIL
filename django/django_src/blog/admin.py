from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'count_text']
    list_display_links =  ['title']

    def count_text(self, obj):
        return '{}글자'.format(len(obj.text))

    count_text.short_description = 'text 글자수' # 설명을 넣음


admin.site.register(Post, PostAdmin)

# Register your models here.
