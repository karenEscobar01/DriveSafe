import json

def crearVehiculo(tipo,placa,disponibilidad):
    dtoVehiculo = {"placa":placa,"tipo":tipo,"disponibilidad":disponibilidad}
    listadoVehiculos = getListaVehiculos()
    dtoVehiculo["id"] = getId()
    listadoVehiculos.append(dtoVehiculo)
    with open("vehiculos.json","w") as archivoVehiculos:
        archivoVehiculos = json.dump(listadoVehiculos,archivoVehiculos,indent=4)

def getListaVehiculos():
    listaVehiculos = []
    try:
        with open("vehiculos.json","r") as archivoVehiculos:
            listaVehiculos = json.load(archivoVehiculos)
    except FileNotFoundError as e:
        print("No se ha creado el archivo vehiculos.json")
    return listaVehiculos

def getId():
    listadoVehiculos = getListaVehiculos()
    idGenerate = 1
    if len(listadoVehiculos)>0:
        vehiculo = max(listadoVehiculos,key=lambda vehiculo:vehiculo["id"])
        idGenerate = vehiculo["id"]+1
    return idGenerate

def getIdByPlaca(placa):
    listadoVehiculos = getListaVehiculos()
    idVehiculo = -1
    for vehiculo in listadoVehiculos:
        if vehiculo["placa"] == placa:
            idVehiculo = vehiculo["id"] 
    return idVehiculo
