from .models import Cctv, Alltimeshop,Lamp , Loadpoint,Securitycenter
from django.contrib import admin

# Register your models here.
admin.site.register(Cctv)
admin.site.register(Alltimeshop)
admin.site.register(Lamp)
admin.site.register(Loadpoint)
admin.site.register(Securitycenter)
