#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 04:54:09 2018

@author: ashraya
"""

#import ast
import json
import logging
import os
from logging.handlers import RotatingFileHandler

from flask import Flask, render_template, request

from emulator.InclExcl import generate_exclusion_report, generate_inclusion_report, generate_trigger_report
import emulator.paho.mqtt.publish, emulator.paho.mqtt.subscribe
from Subscription import stub_subscribe

# App config.

hostname = "localhost"
port = 5000
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = os.urandom(12)
app.config['ENV'] = 'development'

def get_devices():
    devices = ['switch', 'alarm', 'light', 'dimmer', 'flood', 'multi', 'lock', 'plus']
    return devices

def Log(info):
    if (DEBUG == True):
        filename = "log.log"
        if os.path.exists(filename):
            append_write = 'a' # append if already exists
        else:
            append_write = 'w' # make a new file if not

        fp= open(filename, append_write)
        fp.write(info + '\n')
        fp.close()
        app.logger.debug(info)

devices_file = 'selected_devices.json'
devices = []

@app.route("/")
def init():
    return render_template('front.html')

@app.after_request
def add_header(r):
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate, public, max-age=0"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    return r

def get_devices_from_jsonfiles():
    devices = []
    filepath = "emulator/static/prop_files/"
    Log("get_devices_from_jsonfiles : " + str(filepath))
    if os.path.exists(filepath):
        files = os.listdir(filepath)
        Log("get_devices_from_jsonfiles : " + str(files))

        for d in files:
            if (d.find("json") > -1):
                devices.append(d[:d.find('.')])
        Log("get_devices_from_jsonfiles : " + str(devices))
    return devices

@app.route('/init_onload', methods = ['POST'])
def init_onload():
    selected_devices = []
    if os.path.exists(devices_file):
        selected_devices = json.load(open(devices_file))
        Log("init_onload : " + str(selected_devices))

        #stub_subscribe()

    return json.dumps(selected_devices)

@app.route('/init2_onload', methods = ['POST'])
def init2_onload():
        devices = get_devices_from_jsonfiles()
        #devices = get_devices()

        Log("init2_onload: " + str(devices))
        return json.dumps(devices)

def update_selected_devices(selected_devices, req, device_id):
    Log("update_selected_devices")
#    dejsonified_prop = json.loads(req)
    dejsonified_prop = req
    Log("update_selected_devices : dejsonified_prop" + str(type(dejsonified_prop)) + ":" + str(dejsonified_prop))
    found = False

    if (len(selected_devices) > 0):
        for i in range(len(selected_devices)):
            try:
                if (device_id == selected_devices[i].get("id")):
                    Log("update_selected_devices: Popping device : " + str(selected_devices[i]))
                    selected_devices.pop(i)
                    Log("update_selected_devices: Adding device : " + str(type(dejsonified_prop)))
                    selected_devices.append(dejsonified_prop)
                    found = True
                    break
            except KeyError:
                Log("update_slected_devices : KeyError! : " + str(device_id))

    if ((found == False) or (len(selected_devices) <= 0)):
        selected_devices.append(dejsonified_prop)

    Log("update_selected_devices : selected_devices : " + str(selected_devices))

    with open(devices_file, 'w+') as jsonfile:
        json.dump(selected_devices, jsonfile)
        Log('update_selected_devices: Json file updated')
    jsonfile.close()

    return selected_devices

@app.route('/remove_device', methods = ['POST'])
def remove_device():
    data = request.data
    data1 = data

    Log("remove_device : " + str(data1))

    selected_devices = json.load(open(devices_file))

    for device in range(len(selected_devices)):
#       dict_data = ast.literal_eval(selected_devices[device])
        bdata1 = data1.decode('utf-8')
        ddata1 = selected_devices[device].get("id")
        Log("bdata1: " + bdata1)
        Log("ddata1: " + ddata1)

        if (str(bdata1) == str(ddata1)):
            selected_devices.pop(device)

            with open(devices_file, 'w+') as jsonfile:
                json.dump(selected_devices, jsonfile)
                Log('properties: Json file updated')
            jsonfile.close()

            topic, report = generate_exclusion_report(str(bdata1))
            Log("remove_device : topic : "+ topic)
            Log("remove_device : report : "+ str(report))

            emulator.paho.mqtt.publish.single(topic, json.dumps(report), hostname=hostname)

            break

    return json.dumps(selected_devices)

@app.route('/get_properties', methods = ['POST'])
def get_properties():
    Log("get_properties")
    if request.method == 'POST':
        data = request.data
        data1 = data

        Log("get_properties : data1 : " + str(data1))

        selected_devices = json.load(open(devices_file))
        Log("get_properties : type(selected_devices) : " + str(type(selected_devices)))
        for device in range(len(selected_devices)):
            Log("get_properties : type(selected_devices[i]) : " + str(type(selected_devices[device])))
            bdata1 = data1.decode('utf-8')
            try:
                ddata1 = selected_devices[device].get("id")
            except KeyError:
                Log("get_properties : KeyError! : " + str(bdata1))

            Log("get_properties : bdata1 : " + str(bdata1))
            Log("get_properties : ddata1 : " + str(ddata1))

            if (str(bdata1) == str(ddata1)):
                Log("get_properties : selected device properties : " + str(selected_devices[device]))
                return json.dumps(selected_devices[device])

    Log("get_properties : Error! ")
    return "Error"

def update_services(req):
    svs_dict = {}
    for key in req:
        if (key.find("services") > -1) or (key.find("sensor_") == 0):
            key_status = False
            if (req[key] != ""):
                key_status = True

            svs_dict[key[key.find('_')+1:]] = key_status

    Log("update_services: services_dict : " + str(svs_dict))
    return svs_dict

@app.route('/properties', methods = ['POST'])
def properties():
    if request.method == 'POST':
        selected_devices = []

        if os.path.exists(devices_file):
            selected_devices = json.load(open(devices_file))

        Log("properties : " + str(selected_devices))

        req = request.json
        req1 = json.loads(req)
        Log("properties : req : " + str(req))
        Log("properties : device_id : " + str(req1["id"]))
        device_id = req1["id"]
        Log("properties : device_id : " + str(device_id))

        selected_devices = update_selected_devices(selected_devices, req1, device_id)

        Log("properties : devices")

        modify_svs = update_services(req1)
        Log("properties : update_services : modify_svcs : " + str(modify_svs))
        devices = get_devices_from_jsonfiles()
        #devices = get_devices()

        device = ""
        for d in devices:
            if (device_id.find(d) > -1):
                device = d
                break

        skey = ""
        for key in req1:
            topic = ""
            report = ""

            Log("properties : key : "+ key)
            Log("properties : key[key.find('_')+1] : "+ key[key.find('_')+1:])
            Log("properties : status : " + key + " : " + req1[key])

            try:
                if (key.find("services") > -1):
                    Log("properties : services found! : " + key) 
                    if (req1[key] == 'true'):
                        Log("properties : services found is true! Generating trigger report!")
                        topic, report = generate_trigger_report(key[key.find('_')+1:], device_id, device, modify_svs[key[key.find('_')+1:]])
                elif (key.find("sensor_") == 0):
                    Log("properties : sensor found! : key : " + key)
                    if req1[key] == "true" :
                        skey = key[key.find('_')+1:]
                    Log("properties : skey : " + skey)
                    continue
                elif ((key.find("value_sensor") > -1) or (key.find("value_meter") > -1)):
                    if (req1[key] == ""):
                        continue
                    Log("properties : sensor is found! Generating trigger report! : " + str(key))
                    Log("properties : skey : " + skey)
                    Log("properties : skey[skey.find('_')+1:] : " + skey[skey.find('_')+1:])
                    Log("properties : modify_svs[skey[skey.find('_')+1:]] : " + str(modify_svs[skey[skey.find('_')+1:]]))
                    Log("properties : req1[key] : " + str(req1[key]))
                    topic, report = generate_trigger_report(skey, device_id, device, True, str(req1[key]))
                    skey = ""
                else:
                    Log("properties : Nothing found yet!")
                    continue

                if topic == "":
                    Log("properties : Topic is empty!")
                    continue
                else:
                    Log("properties : topic : "+ topic)
                    Log("properties : report : "+ str(report))
                    emulator.paho.mqtt.publish.single(topic, json.dumps(report), hostname=hostname)
            except KeyError:
                Log("properties : KeyError! : " + str(key) + " : " + str(req1[key]))
        Log("properties : selected_devices : " + json.dumps(selected_devices))
        return json.dumps(selected_devices)

    return "Error"

@app.route('/add_device', methods = ['POST'])
def add_device():
    if request.method == 'POST':
        Log("add_device")

        selected_devices = []
        if os.path.exists(devices_file):
            selected_devices = json.load(open(devices_file))

        req1 = ""
        data = request.data
        data1 = data

        Log("add_device: " + str(data1))

        data1 = str(data1.decode('utf-8'))
        devices = get_devices_from_jsonfiles()
        #devices = get_devices()

        for d in devices:
            Log("add_device : devices : "+ d)
            if (data1.find(d) > -1):
                Log("add_device: Device found!")
                file_path = "emulator/static/prop_files/" + d + ".json"
                Log("add_device: " + str(file_path))

                if os.path.exists(file_path):
                    Log("add_device: path exists!")
                    req1 = json.load(open(file_path))
                    Log("add_device : req1 : "+ str(req1))

                    Log("add_device: req[device_id] : " + str(req1["val"]["device_id"]))
                    topic, report = generate_inclusion_report(req1, data1)
                    Log("add_device : topic : "+ topic)
                    report["val"]["status"] = "false"
                    Log("test: req[status] : " + str(report["val"]["status"]))
                    report["val"]["id"] = data1
                    Log("add_device : report : "+ str(report)+" : " + str(type(report)))

                    selected_devices = update_selected_devices(selected_devices, report["val"], data1)
                    Log("add_device: selected_devices list : " + str(selected_devices))

                    emulator.paho.mqtt.publish.single(topic, json.dumps(report), hostname=hostname)
                    return json.dumps(selected_devices)

    return "Error"

def main():
    formatter = logging.Formatter("[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s")
    handler = RotatingFileHandler('log.log', maxBytes=10000, backupCount=1)
    handler.setLevel(logging.DEBUG)
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)

    app.run(debug=False, port=port)
