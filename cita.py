import json
import cliente
from datetime import datetime

def crearCita(idCliente,idInstructor,idVehiculo,fecha,hora,duracion):
    dtoCita = {"idCliente":idCliente,"idInstructor":idInstructor,
               "idVehiculo":idVehiculo,"fecha":fecha,"hora":hora,"duracion":duracion,
               "observacion":"",
                "asistencia":""}
    dtoCita["id"] = getId()
    listaCitas = getListaCitas()
    listaCitas.append(dtoCita)
    with open("citas.json","w") as archivoCitas:
        archivoCitas = json.dump(listaCitas,archivoCitas,indent=4)

def getListaCitas():
    listasCitas = []
    try:
        with open("citas.json","r") as archivoCitas:
            listasCitas = json.load(archivoCitas)
    except FileNotFoundError as e:
        print("No se ha creado el archivo citas.json")
    return listasCitas


def getId():
    listadoCitas = getListaCitas()
    idGenerate = 1
    if len(listadoCitas)>0:
        cita = max(listadoCitas,key=lambda cita:cita["id"])
        idGenerate = cita["id"]+1
    return idGenerate

def actualizarCita(idCita,obser,asist):
    listadoCitas = getListaCitas()
    citaAux = None
    for cita in listadoCitas:
        if cita["id"] == idCita:
            citaAux = cita
            break

    citaAux["observacion"] = obser
    citaAux["asistencia"] = asist

    with open("citas.json","w") as archivoCitas:
        archivoCitas = json.dump(listadoCitas,archivoCitas,indent=4)

def obtenerHistorialByCliente(nit):
    idCliente = cliente.getIdByNit(nit)
    listadoCitas = getListaCitas()

    listadoCitasRetornar = []

    for cita_b in listadoCitas:
        strFechaCita = cita_b["fecha"]+" "+cita_b["hora"]
        fechaCita = datetime.strptime(strFechaCita, "%Y-%m-%d %H:%M")
        if fechaCita<datetime.now() and cita_b["idCliente"]==idCliente:
            listadoCitasRetornar.append(cita_b)
    
    return listadoCitasRetornar
        

