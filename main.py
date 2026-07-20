import menus
import instructor
import cliente
import vehiculo
import cita

from datetime import datetime
print(" BIENVENIDO A DRIVESAFE GIRON ")

opt = menus.pintarMenuPrincipal()
while (opt!=0):
    if opt == 1:
        print(" BIENVENIDO A REGISTRAR CLIENTE ")
        
        nitCli,nombCli,apellCli = menus.pintaraMenuRegistrarCliente()

        esValido  = cliente.validarClienteByNit(nitCli)
        if(esValido):
            cliente.crearCliente(nitCli,nombCli,apellCli)
        else:
            print("EL NIT DIGITADO YA EXISTE")
        
    if(opt == 2):
        print(" BIENVENIDO A REGISTAR INTRUCTOR ")

        nitInst,nombInst,apellInst,idEsp = menus.pintaraMenuRegistrarInstructor()
        esValido = instructor.ValidarInstructor(nitInst)
        if(esValido):
            instructor.crearInstructor(nitInst,nombInst,apellInst,idEsp)
        else:
            print("EL NiT YA EXISTE")
            
    if(opt == 3):
        print(" BIENVENIDO A REGISTAR VEHICULO ")
        idTipVehi,placaVehi,dispoVehiculo = menus.pintaraMenuRegistrarVehiculo()
        esValido = vehiculo.validarVehiculo(placaVehi)
        if(esValido): 
            vehiculo.crearVehiculo(idTipVehi,placaVehi,dispoVehiculo)
        else:
            print("LA PLACA YA EXISTE EN EL SISTEMA")
    if(opt == 4):
        print(" BIENVENIDO A PROGRMAR CITA")

        nitCli,nitInst,placa,strFecha,strHora,strDuracion = menus.pintaraMenuProgramarCita()
        idCliente = cliente.getIdByNit(nitCli)
        idInstructor = instructor.getIdByNit(nitInst)
        idVehiculo = vehiculo.getIdByPlaca(placa)
        listaCitasVehiculo = cita.getListaCitasVehiculo(idVehiculo)
        esValidoVehiculos = cita.validacionDisponibilidadCitas(listaCitasVehiculo,strFecha
                                                      ,strHora,strDuracion)
        
        listaCitasCliente = cita.getListaCitasCliente(idCliente)
        esValidoCliente = cita.validacionDisponibilidadCitas(listaCitasCliente,strFecha
                                                      ,strHora,strDuracion)
        
        listaCitasInstructor = cita.getListaCitasInstructor(idInstructor)
        esValidoInstructor = cita.validacionDisponibilidadCitas(listaCitasInstructor,strFecha
                                                      ,strHora,strDuracion)
        #if esValido:
            #print("SE PUEDE HACER LA CITA")
        #else:
            #print("NO HAY DISPONIBILIDAD")
        #print(f"idCliente:{idCliente} idInstructor:{idInstructor} idVehiculo:{idVehiculo}")
        if nitCli is not None and esValidoVehiculos and esValidoCliente and esValidoInstructor:
            cita.crearCita(idCliente,idInstructor,idVehiculo,strFecha,strHora,strDuracion)
        else:
            if not esValidoVehiculos:
                 print("NO HAY DISPONIBILIDAD DE AUTOMOVIL")
            else:
                if not esValidoCliente:
                    print("NO HAY DISPONIBILIDAD POR CLIENTE")
                else:
                    if not esValidoInstructor:
                        print("NO HAY DISPONIBILIDAD POR INSTRUCTOR")

    if(opt == 5):
        print(" BIENVENIDAD CONSULTAR CITA ")

        optConsultar = menus.pintarMenuConsultarCitas()
        listaCitasMostrar = []
        listCitas = cita.getListaCitas()
        if optConsultar == 1:
            listaCitasMostrar = listCitas
        if optConsultar == 2:
            strFecIni,strFecFin = menus.pintarMenuFechaIniFinal()
            strFecIni = strFecIni+" 00:00"
            strFecFin = strFecFin+ " 23:59"

            fechaInicial = datetime.strptime(strFecIni, "%Y-%m-%d %H:%M")
            fechaFinal = datetime.strptime(strFecFin, "%Y-%m-%d %H:%M")

            for cita_b in listCitas:
                strFechaCita = cita_b["fecha"]+" "+cita_b["hora"]
                fechaCita = datetime.strptime(strFechaCita, "%Y-%m-%d %H:%M")
                if fechaCita>fechaInicial and fechaCita<fechaFinal:
                    listaCitasMostrar.append(cita_b)

        if optConsultar  == 3:
            nitClientCon = menus.pintarMenuNitCliente()
            idCliente = cliente.getIdByNit(nitClientCon)

            for cita_b in listCitas:
                if cita_b["idCliente"] == idCliente:
                    listaCitasMostrar.append(cita_b)


        for cita_b in listaCitasMostrar:
            print(f"id cita:{cita_b['id']} id cliente:{cita_b['idCliente']} fecha:{cita_b['fecha']} hora:{cita_b['hora']} duracion:{cita_b['duracion']}")

        
    if(opt == 6):
        print(" BIENVENIDO A LA CONFIRMACION DE CITAS ")

        idCita,obs,asis = menus.pintarMenuObserAsis()
        cita.actualizarCita(idCita,obs,asis)

    if (opt == 7):
        print(" BIENVENIDO A CONSULTAR HISTORIAL POR CLIENTE")

        nitClientHist = menus.pintarMenuNitCliente()
        listadoCitasHist = cita.obtenerHistorialByCliente(nitClientHist)
        for cita_b in listadoCitasHist:
            idAsist = cita_b["asistencia"]
            strAsist = ""
            if idAsist == "1":
                strAsist = "Si"
            if idAsist == "2":
                strAsist = "No"
            print(f"id cita:{cita_b['id']} \nid cliente:{cita_b['idCliente']} \nfecha:{cita_b['fecha']} \nhora:{cita_b['hora']} \nduracion:{cita_b['duracion']} \nobservacion:{cita_b['observacion']} \nasistencia {strAsist}")
    if(opt == 0):
        break

    opt = menus.pintarMenuPrincipal()
