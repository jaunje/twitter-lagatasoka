#!/usr/bin/env python
#coding: utf-8

# Twithief 
# Agradecimientos a www.geekytheory.com y @luisvallik

# Importamos las librerias necesarias: 
# Twython: necesaria para creacion/autenticacion con Twitter
#     y asi poder actualizar el estado de nuestra
#     cuenta con un mensaje e imagen.

import os
import sys
import time
import random
from twython import Twython, TwythonError

# Creacion de las variables necesarias para conectarnos
# con la apliacion creada en  nuestra cuenta de desarrollador.

CONSUMER_KEY = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
CONSUMER_SECRET = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
ACCESS_KEY = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
ACCESS_SECRET = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

print "Se ha detectado la captura de un intruso, puede ser soka."


print "Abriendo imagen generada..."

photo = open('/home/pi/projects/twithief/photo_thief.jpg', 'rb')

print "Actualizando el estado de la cuenta Twitter con la imagen capturada"
#creamos unos textos
texto = ['La ciudad es mía','Mi dueño me da de comer sardinas',
    'Un ordenador me manda el tuit con la foto :3',
    'Luna lunera, que no es la hora, espera...',
    'Miauuuuuu',
    'Algún día conquistaré el mundo',
    'Miauuu',
    'Miauuuuuuuuuuuu',
    'Un ordenador me manda el tuit',
    'Miauuuu Miaau',
    'Miau Mateo que te veo']

#sacamos la hora
hora = time.strftime("%H")
print hora
if hora >= "09" and hora < "19":
    print "dentro del tiempo permitido para mandar el tuit"
    api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)
    api.update_status_with_media(status=random.choice(texto), media=photo)
    print "tuit enviado enviado a las "+time.strftime("%H:%M")

else:
    print "fuera de hora porque son las "+time.strftime("%H:%M")+ "pero empezamos a favear"
    api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)
    naughty_words = [" -RT", "SEX", "sexo", "muerto"]
    good_words = [" gato ", "miauu", " gatos ", "LaGataSoka", "@lagatasoka", "gatito", "gatitos"]
    filter = " OR ".join(good_words)
    blacklist = " -".join(naughty_words)
    keywords = filter + blacklist

    search_results = api.search(q=keywords, count=30)
    print "resultados"+str(search_results)
    for tweet in search_results["statuses"]:
        print tweet["id_str"]
        #twitter.retweet(id = tweet["id_str"])
        api.create_favorite(id = tweet["id_str"])

print "Bye, Bye...."
sys.exit()
