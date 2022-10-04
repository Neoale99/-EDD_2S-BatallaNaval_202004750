import requests
import json

url_base = "http://localhost:5000"


def cargar(nombre,contrasena,monedas,edad):
    data = {"usuario": nombre, "clave": contrasena , "monedas": monedas, "edad": edad}
    x = requests.get(f"{url_base}/guardar_users",json=data)
    res = x.json()
    return res


def loguear(nombre,contrasena):
    data = {"usuario": nombre, "clave": contrasena}
    x = requests.get(f"{url_base}/login",json=data)
    res = x.json()
    return res


