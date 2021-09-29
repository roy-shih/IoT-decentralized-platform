from django.contrib.auth.models import User
from django.http import response, HttpResponse, JsonResponse
from django.shortcuts import render
from .models import *  # Device, Sensor, scene  # light, fan, AirConditioner, other
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

import json
import os


def autoindex(request):
    autodata = automation.objects.all()
    timerdata = timer.objects.all()
    return render(request, 'auto.html', { 'autodata': autodata, 'timerdata': timerdata})

def postbot(request):
    return render(request, 'postbot.html')

def get_io_state(request, device_id):
    if request.method == 'GET':
        try:
            choose = Device.objects.get(Device_ID=device_id)
        except:
            response = json.dumps(
                [{'Error': 'No device with that ID'}])
            return HttpResponse(response, content_type='text/json')
        response = json.dumps(
            [{'Device_ID': choose.Device_ID, 'state': choose.state}])
    return JsonResponse({'Device_ID': choose.Device_ID, 'state': choose.state}, safe=False)

@csrf_exempt
def add_data_from_iot_device(request):
    if request.method == 'POST':
        try:
            payload = json.loads(request.body)
            print(payload)
            DEVICEID = payload['DEVICE_ID']
            VALUE = float(payload['VALUE'])
            print(DEVICEID, VALUE)
        except:
            DEVICEID = str(request.POST.get('DEVICE_ID'))
            VALUE = float(request.POST.get('VALUE'))
            print(DEVICEID, VALUE)
        try:
            choose = Sensor.objects.get(Device_ID=DEVICEID)
        except:
            response = json.dumps([{'Error': 'Data could not be added!'}])
            return HttpResponse(response, content_type='text/json')
        # print(choose)
        # print("old", choose.value)
        choose.value = VALUE
        choose.save()
        # print("new", choose.value)
        # response = json.dumps([{'Success': 'Data added successfully!'}])
    return JsonResponse({'DEVICE_ID': DEVICEID, 'VALUE': VALUE}, safe=False)

def get_sensor_state(request, device_id):
    if request.method == 'GET':
        try:
            choose = Sensor.objects.get(Device_ID=device_id)
        except:
            response = json.dumps(
                [{'Error': 'No device with that ID'}])
            return HttpResponse(response, content_type='text/json')
    return JsonResponse({'Device_ID': choose.Device_ID, 'value': choose.value}, safe=False)


def index(request):
    lightdata = Device.objects.order_by('name')[:]
    scenedata = scene.objects.all()
    autodata = automation.objects.all()
    timerdata = timer.objects.all()

    return render(request, 'his.html', {"lightdata": lightdata,  'scenedata': scenedata, 'autodata': autodata, 'timerdata': timerdata})


def envindex(request):
    sensordata = Sensor.objects.order_by('name')[:]
    # fandata = fan.objects.all()
    # AirConditionerdata = AirConditioner.objects.all()
    # otherdata = other.objects.all()
    # scenedata = scene.objects.all()

    return render(request, 'env.html', {"sensordata": sensordata})


def realtimechange(request):
    lightdata = Device.objects.all()
    # fandata = fan.objects.all()
    # AirConditionerdata = AirConditioner.objects.all()
    # otherdata = other.objects.all()
    return HttpResponse({"lightdata": lightdata})


def change_io_state(request):
    if request.POST.get('action') == 'post':
        DEVICEID = request.POST.get('DEVICE_ID')
        STATUS = request.POST.get('STATUS')
        DES = "關閉"
        if STATUS == 'false':
            STATUS = bool("")
            DES = "關閉"
        else:
            STATUS = bool("1")
            DES = "開啟"
        try:
            choose = Device.objects.get(Device_ID=DEVICEID)
        except:
            return JsonResponse({'Status': "尚未註冊此物件"}, safe=False)
            # try:
            #     choose = fan.objects.get(Device_ID=DEVICEID)
            # except:
            #     try:
            #         choose = AirConditioner.objects.get(
            #             Device_ID=DEVICEID)
            #     except:
            #         try:
            #             choose = other.objects.get(
            #                 Device_ID=DEVICEID)

        print(choose)
        # test1 = light.objects.get(id=DEVICEID)
        print("old", choose.state)
        choose.state = STATUS
        choose.descriptuin = DES
        choose.save()
        print("new", choose.state)
        return JsonResponse({'Status': STATUS}, safe=False)

# def 