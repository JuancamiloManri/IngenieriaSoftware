from pymongo import MongoClient
import certifi
import pymongo

MONOG_URI = "mongodb://localhost:27017/myDatabase"
ca = certifi.where()

def dbConnection():
    try:
        client = pymongo.MongoClient("mongodb://localhost:27017")
        db = client["db_Dsitribuidos"]
    except ConnectionError:
        print("Error en la conexion")
    return db