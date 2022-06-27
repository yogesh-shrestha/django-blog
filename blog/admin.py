from django.contrib import admin, messages
from .models import Post, Category, Comment, Profile
from tags.models import Tag
from core.models import User
from tags.models import TaggedItem

admin.site.site_header = 'My First Dnango Blog'
admin.site.index_title = 'Admin'


class PostAdmin(admin.ModelAdmin):
    search_fields =  ['title__istartswith', 'title__istartswith']
    list_display = ['title','category', 'approved']
    list_filter = ['category']
    actions = ['approve']

    @admin.action(description='Approve Posts')
    def approve(self, request, querset):
        querset.update(approved=True)
        self.message_user(
            request,
            f'Post were approved successfully',
            messages.ERROR
        )

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'id']


class TagAdmin(admin.ModelAdmin):
    list_display = ['label', 'id']

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment)
admin.site.register(Profile)
admin.site.register(Tag, TagAdmin)
admin.site.register(User)
admin.site.register(TaggedItem)


