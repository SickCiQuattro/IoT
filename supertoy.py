import paho.mqtt.client as mqtt
import time
import RPi.GPIO as GPIO
import json
from multiprocessing import Queue

MQTT_PUB_TOPIC = "supertoy/model/tecnobot/serial/ele25/stato"

GPIO.setmode(GPIO.BOARD)


# Creazione della coda multiprocesso per la gestione dei messaggi
queue = Queue()

# Cosa succede quando ci si connette al server broker: il client si sottoscrive ad un topic 
def on_connect(client, userdata, flags, reason_code, properties):
    print(f"Connected with result code {reason_code}")
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe('supertoy/model/tecnobot/serial/ele25/incarico')

# Cosa succede quando si riceve un messaggio
def on_message(client, userdata, msg):
    # queue.put(msg.topic+" "+str(msg.payload))
    queue.put(str(msg.payload, 'utf-8'))
    # print(msg.topic+" "+str(msg.payload))

# Logica di controllo dei led
def control_leds(num_azioni, led_list):
    if num_azioni == 0:
        return

    for i in range(num_azioni):
        GPIO.output(led_list[i], GPIO.HIGH)

    time.sleep(5)

    GPIO.output(led_list[num_azioni - 1], GPIO.LOW)
    
    return control_leds(num_azioni - 1, led_list)


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
GPIO.setup(12, GPIO.OUT, initial=GPIO.LOW)
##LED2
GPIO.setup(16, GPIO.OUT, initial=GPIO.LOW)
##LED3
GPIO.setup(18, GPIO.OUT, initial=GPIO.LOW)

led_list = (12, 16, 18)

# Creazione del JSON con le informazioni di TecnoBot
MQTT_PUB_MESSAGE = json.dumps({
    "Stato" : "ready",
    "Temperatura" : 20,
    "Batteria" : 80,
    "Velocita" : 0
});


mqttc.publish(topic=MQTT_PUB_TOPIC, payload=MQTT_PUB_MESSAGE)

# Inizio del loop
mqttc.loop_start()

# Attesa di 5 secondi per sincronizzazione con NodeRed
time.sleep(5)

try:
    while True:
        msg = queue.get()
        message = json.loads(msg)
        print(message)
        num_azioni = 0
        for azione in message:
            num_azioni += message[azione]
        control_leds(num_azioni, led_list)
        time.sleep(1)

# Gestione dell'eccezione quando si preme CTRL+C da tastiera
except KeyboardInterrupt:
    print("Uscita in corso...")
    
    # Libera tutti i pin della raspberry
    GPIO.cleanup()

    # Interruzione del loop
    mqttc.loop_stop()

