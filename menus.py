from datetime import datetime

def pintarMenuPrincipal():
    menu = "Seleccione la opcion de menu:\n"
    menu +="1. Registrar Cliente\n"
    menu +="2. Registrar Instructor\n"
    menu +="3. Registrar vehiculo\n"
    menu +="4. Programar cita\n"
    menu +="5. Consultar citas\n"
    menu +="6. Confirmacion de  cita\n"
    menu +="7. Consultar historial por cliente\n"
    menu +="0. Salir\n"
    
    opcion = int(input(menu))
    return opcion

def pintaraMenuRegistrarInstructor():
    nitInstr = input("Digite el nit del instructor\n")
    nombreInstr = input("Digite el nombre del instructor\n")
    apellidoInstr = input("Digite el apellido del instructor\n")
    idEspcialidad = input("Digite la especialidad del instructor: 1.Moto , 2. Carro\n")
    return nitInstr,nombreInstr,apellidoInstr,idEspcialidad

def pintaraMenuRegistrarCliente():
    nitCli = input("Digite el nit del Cliente\n")
    nombreCli = input("Digite el nombre del Cliente\n")
    apellidoCli = input("Digite el apellido del Cliente\n")
    return nitCli,nombreCli,apellidoCli

def pintaraMenuRegistrarVehiculo():
    idTipoVehiculo= input("Digite el tipo vehiculo 1.Moto , 2 Carro\n")
    placaVehiculo = input("Digite placa vehiculo\n")
    dispoVehiculo = input("Digite disponibilidad\n")
    return idTipoVehiculo,placaVehiculo,dispoVehiculo

def pintaraMenuProgramarCita():
    try:
        nitClit= input("Digite la cedula del cliente\n")
        nitInstr = input("Digite la cedula del instructor\n")
        placa = input("Digite la placa del vehiculo\n")
        strFecha = input("Digite la fecha en formato yyyy-MM-dd\n")
        fechaTemp = datetime.strptime(strFecha, "%Y-%m-%d")
        strHora = input("Digite la hora en horario militar\n")
        strDuracion = input("Digite la duracion en horas\n")
        return nitClit,nitInstr,placa,strFecha,strHora,strDuracion
    except Exception:
        print("Digite un formato valido de fecha yyyy-MM-dd")
        return None,None,None,None,None,None
    

def pintarMenuConsultarCitas():
    menuConsulCitas = "Digite la opcion\n"
    menuConsulCitas += "1. Consultar TODAS\n"
    menuConsulCitas += "2. Consultar Por fecha\n"
    menuConsulCitas += "3. Consultar Por Cliente\n"
    opt = int(input(menuConsulCitas))
    return opt

def pintarMenuFechaIniFinal():
    strFechaInicial = input("Digite la fecha inicial en formato yyyy-MM-dd\n")
    strFechaFinal = input("Digite la fecha final en formato yyyy-MM-dd\n")
    return strFechaInicial,strFechaFinal

def pintarMenuNitCliente():
    nitCliente = input("Digite el nit del cliente\n")
    return nitCliente

def pintarMenuObserAsis():
    idCita = int(input("Digite el id de la cita\n"))
    obser = input("Digite la observacion\n")
    asistencia = input("Digite asistencia 1.Si , 2.No\n")
    return idCita,obser,asistencia

