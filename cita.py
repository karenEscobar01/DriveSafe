import json
import cliente
from datetime import datetime,timedelta

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

def getListaCitasVehiculo(idVehiculo):
    listadoCitas = getListaCitas()
    listadoCitasVehiculo = []
    for cita_b in listadoCitas:
        if cita_b["idVehiculo"] == idVehiculo:
            listadoCitasVehiculo.append(cita_b)
    return listadoCitasVehiculo

def getListaCitasCliente(idCliente):
    listadoCitas = getListaCitas()
    listadoCitasCliente = []
    for cita_b in listadoCitas:
        if cita_b["idCliente"] == idCliente:
            listadoCitasCliente.append(cita_b)
    return listadoCitasCliente

def getListaCitasInstructor(idInstructor):
    listadoCitas = getListaCitas()
    listadoCitasInstructor = []
    for cita_b in listadoCitas:
        if cita_b["idInstructor"] == idInstructor:
            listadoCitasInstructor.append(cita_b)
    return listadoCitasInstructor

def validacionDisponibilidadCitas(listadoCitas,strFechIniPet,hora,duracionPeticion):
    strFechIniPet = strFechIniPet + " "+hora
    fechIncialPet = datetime.strptime(strFechIniPet, "%Y-%m-%d %H:%M")
    horasSumarPet = int(duracionPeticion)
    timeHorasSumarPet = timedelta(hours=horasSumarPet)
    fechaFinalPet = fechIncialPet+timeHorasSumarPet

    print(f"fechIncialPeticion {fechIncialPet} - fechFinalCitaPeticion {fechaFinalPet}")

    esDisponible = True
    for cita_b in listadoCitas:
        strFechaInicialCita = cita_b["fecha"]+" "+cita_b["hora"]
        fechIncialCita = datetime.strptime(strFechaInicialCita, "%Y-%m-%d %H:%M")
        horasSumarCita = int(cita_b["duracion"])
        timeHorasSumarCita = timedelta(hours=horasSumarCita)
        fechaFinalCita = fechIncialCita+timeHorasSumarCita
        print(f"fechIncialCita {fechIncialCita} - fechFinalCita {fechaFinalCita}")

        if (fechIncialPet>=fechIncialCita and fechIncialPet<fechaFinalCita):
            esDisponible = False
            break
        if(fechaFinalPet>fechIncialCita and fechaFinalPet<=fechaFinalCita):
            esDisponible = False
            break
        if(fechIncialPet<fechIncialCita and fechaFinalPet>fechaFinalCita):
            esDisponible = False
            break
    return esDisponible


        




        

