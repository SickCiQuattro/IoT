#!/bin/bash

# Verifica se Python 3 è installato
if ! command -v python3 &> /dev/null
then
    echo "Python 3 non è installato. Installazione in corso..."
    sudo apt-get update
    sudo apt-get install -y python3
else
    echo "Python 3 è già installato."
fi

# Verifica se pip3 è installato
if ! command -v pip3 &> /dev/null
then
    echo "pip3 non è installato. Installazione in corso..."
    sudo apt-get install -y python3-pip
else
    echo "pip3 è già installato."
fi

# Installa le librerie richieste
pip3 install gpiozero RPi.GPIO paho-mqtt