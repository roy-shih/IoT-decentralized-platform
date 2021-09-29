from .models import *  # Device, Sensor, scene  # light, fan, AirConditioner, other
from django.contrib import admin

admin.site.site_header = 'Smart Home Kit'  # 设置header
admin.site.site_title = 'Smart Home Kit'   # 设置title
admin.site.index_title = 'mart Home Kit'


# Register your models here.
admin.site.register(Device)
# admin.site.register(AirConditioner)
# admin.site.register(fan)
# admin.site.register(other)
admin.site.register(Sensor)
admin.site.register(scene)
admin.site.register(automation)
admin.site.register(timer)
