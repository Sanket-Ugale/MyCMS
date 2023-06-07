from django.contrib import admin

from comments.models import commentsModel

# Register your models here.
class commentsAdmin(admin.ModelAdmin):
    list_display=('name','email','url','date','message')
# ,'date'
admin.site.register(commentsModel,commentsAdmin)
