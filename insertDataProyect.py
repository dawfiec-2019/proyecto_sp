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
for record in cursor:
    id = record['_id']
    print(record['_id'])
    print(id)
    break

# #data = list(csv.reader(open("historico.txt", "r",encoding="UTF-8"), delimiter='|'))[1:]
# titulos=[]
# autores_lista=[]
#
#
# num_line = 0
# for line in open("historico.txt",encoding="UTF-8"):
#     #print(line)
#     line = line.replace("\n","")
#     if num_line!=0:
#         #print(line)
#         titulo,autores,isbn,rate = line.split("|")
#         #print(autores)
#
#         autores = autores.split("-")
#
#         if titulo not in titulos:
#             titulos.append((titulo,isbn))
#
#
#         #print(len(autores))
#         #requests.post(url="http://localhost:8000/api/v1.0/libro/",data={'title':titulo,'isbn':isbn})
#         for autor in autores:
#             if autor not in autores_lista:
#                 autores_lista.append(autor)
#             #requests.post(url="http://localhost:8000/api/v1.0/autor/", data={'nombre':autor,'apellido':autor})
#             #print(autor)
#         # requests.post(url="http://localhost:8000/api/v1.0/autor_libro/",data={'title':titulo,'isbn':isbn})
#
#         #requests.post(url="http://localhost:8000/api/v1.0/libro/",data={'title':titulo,'isbn':isbn})
#
#
#         #break
#     num_line+=1
#
#
#
#
# print(len(autores_lista))
