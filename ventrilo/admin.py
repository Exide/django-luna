from django.contrib import admin
from luna.ventrilo.models import Server, Channel, Client

class ServerAdmin(admin.ModelAdmin):    pass

admin.site.register(Server, ServerAdmin)