# Guida generale per l'esame di laboratorio di IoT 2024 del corso di ITID

*“Se la vostra raspberry è stata toccata da Filippo di recente allora è sicuramente tutto aggiornato e non dovete fare nulla perché lui è malato e deve avere tutto all’ultima versione” - Filippo*

# DISCLAMIER
 In questo brach viene trattata la libreria GPIO Zero per avere una visione completa di tutto il necessario. Solo fattoria.py è stato modificato per l'uso di GPIO Zero perchè sono pigro e devo finire sistemi di elaborazione.


## Table of contents
- [Installazione python automatica](#Installazione-python-automatica)
- [Collegamento SSH con MobaXterm](#collegamento-ssh-con-mobaxterm)
- [Collegamento SSH con NodeRED](#collegamento-ssh-con-broker-elux-su-nodered)
- [Set up della Raspberry](#set-up-della-raspberry)
- [Eseguire un programma su Raspberry](#eseguire-un-programma-su-raspberry)
- [Documentazione utile](#documentazione-utile)
- [File in questa repository](#file-in-questa-repository)
- [Collegamenti esterni](#collegamenti-esterni)

## Installazione python automatica
Installazione python e librerie automatica (evitare se ti chiami umberto)

rendere lo script **backup.sh** eseguibile:
```bash
chmod +x backup.sh
```

eseguirlo:
```bash
./backup.sh
```

## Collegamento SSH con MobaXterm
1. Creare una nuova sessione SSH
2. Inserire come UID:
   ```bash
    pi
   ```
3. Inserire come PSWD:
   ```bash
    raspberry
   ```
**ATTENZIONE:** La password non viene visualizzata a schermo.

## Collegamento SSH con broker ELUX su NodeRED

### Connection
Server: 
```bash
lab-elux.unibs.it
```
Porta: 
```bash
50009
```
### TLS configuration
Caricare il certificato come mostrato in figura:

![ProprietàTLS](https://github.com/scrapanzano/IoT/blob/master/Images/PropietaTLS.png)

### Security
UID:
```bash
itidiot
```
PSWD: 
```bash
ITid24!
```
La schermata principale sarà così a questo punto:

![ProprietàGenerali](https://github.com/scrapanzano/IoT/blob/master/Images/PropietaGenerali.png)


## Set up della Raspberry
La Raspberry dovrebbe essere già munita di python al suo interno. 
Per verificarlo:
```bash
python3 -V
```
In caso contrario è possibile installarlo, come mostrato [qui](https://projects.raspberrypi.org/en/projects/generic-python-install-python3), eseguendo i seguenti comandi:
```bash
sudo update
```
```bash
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
```
```bash
sudo upgrade
```
```bash
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

Per leggere la fotoresistenza è abbastanza un casino e non sono sicuro possa farsi con python. 
Per abilitare modulo I2C [Solo per veri nerd](http://www.emcu.it/RaspBerryPi/RaspBerryPi.html#Abilitare%20I2C%20bus)
Testare i pin 3 e 5.

## Eseguire un programma su Raspberry
1. Trascinare il programma all'interno della cartella in MobaXterm
2. Verificare di trovarsi nella stessa cartella dello script:
   Da linea di comando eseguire:
   ```bash
    dir
   ```
   Se vi trovate nella stessa cartella dello script dovreste vederlo elencato. Altrimenti bisogna spostarsi nella cartella.

   Da linea di comando eseguire:
   ```bash
    cd percorso/del/file
   ```
4. A questo punto si può eseguire il programma con:
   ```bash
    python3 nomescript.py
   ```   
## Documentazione utile

[Qui](https://sourceforge.net/p/raspberry-gpio-python/wiki/Examples/) potete trovare una serie di esempi per configurare GPIO all'interno di Visual Studio.

[Qui](https://eclipse.dev/paho/files/paho.mqtt.python/html/client.html) potete trovare la documentazione completa per paho-mqtt.

Inoltre potrebbe essere comodo avere sotto mano il [getting-started](https://github.com/eclipse/paho.mqtt.python?tab=readme-ov-file#getting-started) di paho-mqtt.

## File in questa repository

- [Certificato](https://github.com/scrapanzano/IoT/blob/master/intermediate_ca.pem) per stabilire la sessione SSH con il laboratorio
  
**NOTA:** il certificato deve essere all'interno della stessa cartella dello script python nella Raspberry
- [Template](https://github.com/scrapanzano/IoT/blob/master/ScriptsDLFC/template.py) da poter riempire
- [Esempio](https://github.com/scrapanzano/IoT/blob/master/ScriptsDLFC/supertoy.py) di risoluzione di un tema esame
- [Esempio](https://github.com/scrapanzano/IoT/blob/master/ScriptsDLFC/fattoria.py) di un programma che utilizza una coda non bloccante
- [Script](https://github.com/scrapanzano/IoT/tree/master/ScriptsNAST) realizzati dagli altri Umberti

## Installazione automatica python e librerie

rendere lo script **install.sh** eseguibile:
```bash
chmod +x install.sh
```

eseguirlo:
```bash
./install.sh
```
