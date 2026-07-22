import json
def crearInstructor(nit,nombre,apellidos,idEspecialidad):
    dtoInstructor = {"nit":nit,"nombre":nombre,"apellidos":apellidos,"especialidad":idEspecialidad}
    listadoInstructores = getListaInstructores()
    dtoInstructor["id"] = getId()
    listadoInstructores.append(dtoInstructor)
    with open("Data/instructores.json","w") as archivoInstructores:
        archivoInstructores = json.dump(listadoInstructores,archivoInstructores,indent=4)

def getListaInstructores():
    listaInstructores = []
    try:
        with open("Data/instructores.json","r") as archivoInstructores:
            listaInstructores = json.load(archivoInstructores)
    except FileNotFoundError as e:
        print("No se ha creado el archivo instructores.json")
    return listaInstructores

def getId():
    listadoInstructores = getListaInstructores()
    idGenerate = 1
    if len(listadoInstructores)>0:
        instructor = max(listadoInstructores,key=lambda instructor:instructor["id"])
        idGenerate = instructor["id"]+1
    return idGenerate

def getIdByNit(nit):
    listadoInstructores = getListaInstructores()
    idInstructor = -1
    for instructor in listadoInstructores:
        if instructor["nit"] == nit:
            idInstructor = instructor["id"]
    return idInstructor

def ValidarInstructor(nit):
    ListaInstructores = getListaInstructores()
    for instructor in ListaInstructores:
        if instructor["nit"] == nit:
            return False
    return True    