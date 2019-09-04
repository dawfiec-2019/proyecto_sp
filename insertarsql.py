import csv
import requests
from urllib import parse
from json import load
from pymongo import MongoClient, DESCENDING
import ssl


import json
from pymongo import MongoClient


mongoClient = MongoClient('localhost',27017)

db = mongoClient.proyec_segundo_parcial

collection = db.laws

#ids = []

#
# with open('laws.json',encoding="UTF-8") as json_file:
#     data = json.load(json_file)
#     #ids = []
#     #ids = list(data.keys())
#     for clave,valor in data.items():
#         #print(clave)
#         #print(valor)
#         #print('\n')
#         item1 ={'name':valor['name'],'description':valor['description'],'pub_date':valor['pub_date'],'summary':valor['summary'],'details':valor['details']}
#         #print(item1)
#         rec_id1 = collection.insert_one(item1)
#         #break
#     #print(data["8173569207278814857"])
#

cursor = collection.find()

c=0

lista_asambleistas=[]
id_asam=1

diccionario={}

diccionario_ley={}

for record in cursor:
    #print(record)
    id = record['_id']
    id = str(id)
    #print(type(record['name']))
    #diccionario_ley[id]={'name':record['name'],'fecha':record['pub_date'],'descripcion':record['description']}
    #
    requests.post(url="http://localhost:8000/api/v1.0/ley/",data={'id_ley': id, 'nombre_oficial': record['name'],'nombre_publico':record['name'],'fecha': record['pub_date'],'descripcion':record['name']})
    # #name = record['details']
    # #print(name)
    for clave,valor in record['details'].items():
        #print(clave)

        for asambleista in valor:
            if asambleista not in lista_asambleistas:
                diccionario[str(asambleista)]=id_asam
                requests.post(url="http://localhost:8000/api/v1.0/asambleista/",data={'nombre':asambleista,'apellido':asambleista,'partido':"NA"})
                lista_asambleistas.append(asambleista)
                id_asam+=1
            requests.post(url="http://localhost:8000/api/v1.0/voto/", data={'voto':clave,'id_ley':id,'id_asambleista':diccionario[asambleista]})

    #
    #
    #


    #
    # for asambleista in record['details']['AUSENTE']:
    #     if asambleista not in lista_asambleistas:
    #         lista_asambleistas.append(asambleista)
    #         #print(asambleista)
    # for asambleista in record['details']['SI']:
    #     if asambleista not in lista_asambleistas:
    #         lista_asambleistas.append(asambleista)
    #         # print(asambleista)
    # for asambleista in record['details']['NO']:
    #     if asambleista not in lista_asambleistas:
    #         lista_asambleistas.append(asambleista)
    #         # print(asambleista)
    # for asambleista in record['details']['ABSTENCION']:
    #     if asambleista not in lista_asambleistas:
    #         lista_asambleistas.append(asambleista)
    #         # print(asambleista)

    #mas = str(id) +'ola'


print(len(lista_asambleistas))
print(diccionario_ley)

for clave, valor in diccionario_ley.items():
    requests.post(url="http://localhost:8000/api/v1.0/ley/",data={'id_ley': clave, 'nombre_oficial': valor['name'],'nombre_publico':valor['name'],'fecha': valor['fecha'],'descripcion':valor['name']})
