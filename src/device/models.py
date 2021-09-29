from django.db import models
from django.db.models.fields import BooleanField, CharField, FloatField, IntegerField, TimeField
import uuid

# Create your models here.


class Device(models.Model):
    Device_ID = CharField(max_length=100)
    name = CharField(max_length=100)
    state = BooleanField()
    fig = CharField(max_length=300)
    descriptuin = CharField(max_length=100, default='關閉')

    def __str__(self):
        return self.name


# class fan(models.Model):
#     Device_ID = CharField(max_length=100, default=uuid.uuid4())
#     name = CharField(max_length=100)
#     fig = CharField(max_length=300)
#     state = BooleanField(default=0)
#     descriptuin = CharField(max_length=100, default='關閉')

#     def __str__(self):
#         return self.name


# class AirConditioner(models.Model):
#     Device_ID = CharField(max_length=100, default=uuid.uuid4())
#     fig = CharField(max_length=300)
#     name = CharField(max_length=100)
#     state = BooleanField(default=0)
#     temp = FloatField(default=0)
#     humidity = FloatField(default=0)
#     control_temp = IntegerField(default=0)
#     descriptuin = CharField(max_length=100, default='關閉')

#     def __str__(self):
#         return self.name


# class other(models.Model):
#     Device_ID = CharField(max_length=100, default=uuid.uuid4())
#     fig = CharField(max_length=300)
#     name = CharField(max_length=100)
#     state = BooleanField(default=0)
#     descriptuin = CharField(max_length=100, default='關閉')

#     def __str__(self):
#         return self.name

class Sensor(models.Model):
    Device_ID = CharField(max_length=200)
    name = CharField(max_length=100)
    value = FloatField(default=0)
    fig = CharField(max_length=300)

    def __str__(self):
        return self.name


class scene(models.Model):
    SceneName = CharField(max_length=200)
    OpenDevice_ID = CharField(max_length=100)
    closeDevice_ID = CharField(max_length=100)

    def __str__(self):
        return self.SceneName


class automation(models.Model):
    automation_name = CharField(max_length=200)
    sensor_condition = CharField(max_length=200)
    OpenDevice_ID = CharField(max_length=100)
    closeDevice_ID = CharField(max_length=100)
    Enable = BooleanField()

    def __str__(self):
        return self.automation_name


class timer(models.Model):
    timer_name = CharField(max_length=200)
    time = TimeField()
    OpenDevice_ID = CharField(max_length=100)
    closeDevice_ID = CharField(max_length=100)
    Enable = BooleanField()

    def __str__(self):
        return self.timer_name
