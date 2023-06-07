from django.contrib import admin
from form.models import form
class formAdmin(admin.ModelAdmin):
    list_display=('Name','Email','Subject','Message')

admin.site.register(form,formAdmin)

# Register your models here.
