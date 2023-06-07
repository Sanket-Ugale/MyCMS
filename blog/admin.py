from django.contrib import admin
from blog.models import blog
class blogAdmin(admin.ModelAdmin):
    list_display=('Title','date','author','category','description','url','banner','content')

admin.site.register(blog,blogAdmin)

# Register your models here.
