from django.urls import path
from . import views

app_name = 'device'

urlpatterns = [
    path('', views.index, name='device'),
    path('envir/', views.envindex, name='device'),
    path('post/', views.postbot, name='device'),
    path('auto/', views.autoindex, name='device'),
    path('api/', views.change_io_state, name='submit_prediction'),
    # path('autoapi/', views.change_io_state, name='submit_prediction'),
    path('sensorapi/', views.add_data_from_iot_device, name='update'),
    path('io/<str:device_id>', views.get_io_state, name='state'),
    path('envir/sensor/<str:device_id>', views.get_sensor_state, name='sensor'),
]
