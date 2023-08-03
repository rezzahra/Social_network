from django.contrib import admin
from .models import Post, Comments
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('user','title','created_date')
    search_fields = ('slug',)
    list_filter = ('updated_date',)
    prepopulated_fields = {'slug':('body',)}

class CommentAdmin(admin.ModelAdmin):
    list_display = ('user','post','created_date', 'is_reply')
    search_fields = ('user',)
    raw_id_fields = ('user', 'post', 'reply')


admin.site.register(Post, PostAdmin)
admin.site.register(Comments, CommentAdmin)
