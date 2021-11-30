from django.contrib import admin

# Register your models here.

from .models import Blog, Tag,Author



class BlogAdminSection(admin.AdminSite):
    site_header = 'MY BLOGS'

blog =BlogAdminSection(name='BLOG APP')


@admin.register(Blog)
class BAdmin(admin.ModelAdmin):
    # fields = ('name', 'color' )
    list_display = ('heading', )
    search_fields = ('color', )

    fieldsets = (
        ('Part 1', {
           'classes': ('wide', 'extrapretty'),
            'fields': ('heading', 'desc' , 'blog_tags' ,'is_active')
        }),
        ('Part Color', {
            'fields': ('color', )
        }), 
    )

# admin.site.register(Blog, BAdmin)
# admin.site.register(Blog)
admin.site.register(Tag)
admin.site.register(Author)

# blog.register(Blog)