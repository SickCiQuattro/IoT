import paho.mqtt.client as mqtt
import time
import RPi.GPIO as GPIO
import json
from multiprocessing import Queue

# Topic sul quale la raspberry pubblica
MQTT_PUB_TOPIC = "path/del/topic"
# Topic sul quale la raspberry si sottoscrive
MQTT_SUB_TOPIC = "path/del/topic"

# Modalità GPIO
GPIO.setmode(GPIO.board)

# Creazione della coda multiprocesso per la gestione dei messaggi
queue = Queue()

# Cosa succede quando ci si connette al server broker: il client si sottoscrive ad un topic 
def on_connect(client, userdata, flags, reason_code, properties):
    print(f"Connected with result code {reason_code}")
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    
    # Topic al quale la raspberry si sottoscrive
    client.subscribe(MQTT_SUB_TOPIC)

# Cosa succede quando si riceve un messaggio
def on_message(client, userdata, msg):
    # Se si vuole inserire sia il topic che il payload nella coda
    # queue.put(msg.topic+" "+str(msg.payload))

    # Se si vuole inserire solo il payload come stringa
    queue.put(str(msg.payload, 'utf-8'))

    # Se si vuole stampare il topic e il payload
    # print(msg.topic+" "+str(msg.payload))


# FACOLTATIVA: funzione per la logica di controllo 
def control_logic():
    pass

# Creazione del client e definizione delle sue due funzioni
mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqttc.on_connect = on_connect
mqttc.on_message = on_message

# Creazione dell connessione SSH con il server broker di ELUX
mqttc.tls_set(ca_certs = 'intermediate_ca.pem')
mqttc.username_pw_set(username = 'itidiot', password = 'ITid24!')
mqttc.connect("lab-elux.unibs.it", 50009, 60)

# Immagini iniziali degli ingressi
##LED1
GPIO.setup(12, GPIO.OUT, initial=GPIO.LOW) # Inizialmente spento
##LED2
GPIO.setup(16, GPIO.OUT, initial=GPIO.LOW) # Inizialmente spento
##LED3
GPIO.setup(18, GPIO.OUT, initial=GPIO.LOW) # Inizialmente spento
##P1
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_UP) 

led_list = (12, 16, 18)

# Se raspberry deve pubblicare un messaggio iniziale
MQTT_PUB_MESSAGE = json.dumps({"led1": 0, "led2": 0, "led3": 0, "p1": 0})

# Pubblicazione del messaggio iniziale sul topic
mqttc.publish(topic=MQTT_PUB_TOPIC, payload=MQTT_PUB_MESSAGE)

# Ciclo infinito

mqttc.loop_start()

time.sleep(5)

try:
    while True:
        message = queue.get()
        print(f"Received message: {message}")

        # Decodifica del messaggio
        message = json.loads(message)

        # Controllo della logica (solo se implementata, altrimenti mettere tutto nel loop)
        control_logic()

        time.sleep(1)

# Gestione dell'eccezione quando si preme CTRL+C
except KeyboardInterrupt:
    print("Exiting...")
    
    # Libera i pin della raspberry
    GPIO.cleanup()

    # Ferma il loop del client
    mqttc.loop_stop()

    # Disconnette il client
    mqttc.disconnect()
