from django.contrib import admin
from blogging.models import Post, Category

# store your ModelAdmin classes in here

class PostInline(admin.TabularInline):
    model = Category.posts.through
    extra = 1


class PostAdmin(admin.ModelAdmin):
    inlines = [
        PostInline,
    ]
    exclude = ["posts"]


class CategoryAdmin(admin.ModelAdmin):
    exclude = ["posts"]



# Register your models here.


admin.site.register(Category, PostAdmin)
admin.site.register(Post, PostAdmin)

