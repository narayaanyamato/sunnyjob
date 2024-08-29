from django.contrib import admin
from sunnyapp.models import Jobs
class JobsAdmin(admin.ModelAdmin):
    list_display=['jid','jpdate','jtitle','cname','edu','loc','email','phone','caddress']
admin.site.register(Jobs,JobsAdmin)