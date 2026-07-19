import json
def crearCliente(nit,nombre,apellido):
    dtoCliente = {"nit":nit,"nombre":nombre,"apellido":apellido}
    listadoClientes = getListaClientes()
    listadoClientes.append(dtoCliente)
    dtoCliente["id"] = getId()
    with open("clientes.json","w") as archivoClientes:
        archivoClientes = json.dump(listadoClientes,archivoClientes,indent=4)


def getListaClientes():
    listaClientes = []
    try:
        with open("clientes.json","r") as archivoClientes:
            listaClientes = json.load(archivoClientes)
    except FileNotFoundError as e:
        print("No se ha creado el archivo clientes.json")
    return listaClientes

def validarClienteByNit(nit):
    listadoClientes = getListaClientes()
    for cliente in listadoClientes:
        if cliente["nit"] == nit:
            return False
    return True

def getId():
    listadoClientes = getListaClientes()
    idGenerate = 1
    if len(listadoClientes)>0:
        cliente = max(listadoClientes,key=lambda cliente:cliente["id"])
        idGenerate = cliente["id"]+1
    return idGenerate

def getIdByNit(nit):
    listadoClientes = getListaClientes()
    idCliente = -1
    for cliente in listadoClientes:
        if cliente["nit"] == nit:
            idCliente = cliente["id"]
    return idCliente



