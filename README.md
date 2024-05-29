# Guida generale per l'esame di laboratorio di IoT 2024 del corso di ITID

**IMPORTANTE:** Si assume che abbiate già effettuato il collegamento SSH tra Raspberry e MobaXterm.

## Set up della raspberry
La Raspberry dovrebbe essere già munita di python al suo interno. 
Per verificarlo:
```bash
python3 -V
```
In caso contrario è possibile installarlo, come mostrato [qui](https://projects.raspberrypi.org/en/projects/generic-python-install-python3), eseguendo i seguenti comandi:
```bash
sudo update
sudo apt install python3 idle3
```
La Raspberry potrebbe non avere installato pip.
Per verificarlo:
```bash
pip --version
```
In caso contrario è possibile installarlo, come mostrato [qui](https://pimylifeup.com/raspberry-pi-pip/), eseguendo i seguenti comandi:
```bash
sudo update
sudo upgrade
sudo apt install python3-pip
```
**ATTENZIONE:** sudo update e sudo upgrade potrebbero richiedere un po' di tempo per terminare le loro procedure.


Per poter svolgere l'esame sono necessarie due librerie: [RPi.GPIO](https://pypi.org/project/RPi.GPIO/) e [paho-mqtt](https://pypi.org/project/paho-mqtt/), per verificare se sono già installate: 
```bash
pip list
```
Altrimenti:
```bash
pip install RPi.GPIO
```
```bash
pip install paho-mqtt
```

## Documentazione utile

[Qui](https://sourceforge.net/p/raspberry-gpio-python/wiki/Examples/) potete trovare una serie di esempi per configurare GPIO all'interno di Visual Studio.

[Qui](https://eclipse.dev/paho/files/paho.mqtt.python/html/client.html) potete trovare la documentazione completa per paho-mqtt.

Inoltre potrebbe essere comodo avere sotto mano il [getting-started](https://github.com/eclipse/paho.mqtt.python?tab=readme-ov-file#getting-started) di paho-mqtt.




