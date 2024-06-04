# Guida generale per l'esame di laboratorio di IoT 2024 del corso di ITID

*“Se la vostra raspberry è stata toccata da Filippo di recente allora è sicuramente tutto aggiornato e non dovete fare nulla perché lui è malato e deve avere tutto all’ultima versione” - Filippo*

# DISCLAMIER
 In questo brach viene trattata la libreria GPIO Zero per avere una visione completa di tutto il necessario. Solo fattoria.py è stato modificato per l'uso di GPIO Zero perchè sono pigro e devo finire sistemi di elaborazione.


## Effettuare collegamento SSH con broker ELUX  (Se non comunicate all'esame)

![ProprietàGenerali](https://github.com/scrapanzano/IoT/blob/master/PropietaGenerali.png)
![ProprietàTLS](https://github.com/scrapanzano/IoT/blob/master/PropietaTLS.png)

Connessione:
```bash
iot24/<banco>/
Server: lab-elux.unibs.it: 50009
```
Security Config:
```bash
UID: itidiot
PSWD: ITid24!
```

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


Per poter svolgere l'esame sono necessarie due librerie: [GPIO Zero](https://gpiozero.readthedocs.io/en/latest/index.html) e [paho-mqtt](https://pypi.org/project/paho-mqtt/), per verificare se sono già installate: 
```bash
pip list
```
Altrimenti:
```bash
pip install gpiozero
```
```bash
pip install paho-mqtt
```

Per abilitare modulo I2C [Solo per veri nerd](http://www.emcu.it/RaspBerryPi/RaspBerryPi.html#Abilitare%20I2C%20bus)

## Documentazione utile

[Qui](https://sourceforge.net/p/raspberry-gpio-python/wiki/Examples/) potete trovare una serie di esempi per configurare GPIO all'interno di Visual Studio.

[Qui](https://eclipse.dev/paho/files/paho.mqtt.python/html/client.html) potete trovare la documentazione completa per paho-mqtt.

Inoltre potrebbe essere comodo avere sotto mano il [getting-started](https://github.com/eclipse/paho.mqtt.python?tab=readme-ov-file#getting-started) di paho-mqtt.

## File in questa repository

- [Certificato](https://github.com/scrapanzano/IoT/blob/master/intermediate_ca.pem) per stabilire la sessione SSH con il laboratorio
  
**NOTA:** il certificato deve essere all'interno della stessa cartella dello script python nella Raspberry (es. /home/pi/scripts/)
- [Esempio](https://github.com/scrapanzano/IoT/blob/master/supertoy.py) di risoluzione di un tema esame
- [Template](https://github.com/scrapanzano/IoT/blob/master/template.py) da poter riempire

## Installazione automatica python e librerie

rendere lo script **install.sh** eseguibile:
```bash
chmod +x install.sh
```

eseguirlo:
```bash
./install.sh
```
