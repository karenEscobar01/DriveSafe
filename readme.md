# DOCUMENTACION
# 🚗 DriveSafe Girón - Sistema de Gestión de Clases de Conducción

Sistema interactivo por consola desarrollado en Python para la administración de clientes, instructores, vehículos y programación de citas de práctica de conducción en la academia **DriveSafe Girón**.

---

## 📋 Tabla de Contenidos

1. [Descripción General](#-descripción-general)
2. [Características Principales](#-características-principales)
3. [Estructura del Proyecto](#-estructura-del-proyecto)
4. [Modelo y Estructura de Datos (JSON)](#-modelo-y-estructura-de-datos-json)
5. [Requisitos Previos](#-requisitos-previos)
6. [Instalación y Ejecución](#-instalación-y-ejecución)
7. [Guía de Uso del Menú](#-guía-de-uso-del-menú)
8. [Detalles de Módulos](#-detalles-de-módulos)

---

## 🚘 Descripción General

**DriveSafe Girón** es un software de consola enfocado en simplificar y automatizar los procesos operativos de una academia de conducción. Permite llevar el control completo de clientes, instructores y vehículos, además de contar con un motor de validación de disponibilidad para evitar solapamientos en la agenda de clases.

---

## ⚡ Características Principales

* **Gestión de Entidades Básicas:**
  * **Clientes:** Registro con validación de existencia única por documento (NIT/Cédula).
  * **Instructores:** Registro clasificado según especialidad (`1`: Moto, `2`: Carro).
  * **Vehículos:** Control de flota por tipo (`1`: Moto, `2`: Carro), placa única y estado de disponibilidad.
* **Programación Inteligente de Citas:**
  * Algoritmo de validación de disponibilidad horaria que previene cruces de agenda en tiempo real entre cliente, instructor y vehículo.
* **Consultas y Filtrado de Citas:**
  * Listado general de todas las citas programadas.
  * Filtro por rango de fechas (`YYYY-MM-DD`).
  * Consulta personalizada por documento del cliente.
* **Confirmación e Historial de Clases:**
  * Módulo para registrar observaciones posteriores a la clase y tomar asistencia (`1`: Sí, `2`: No).
  * Reporte histórico de clases finalizadas por cliente.

---

## 📁 Estructura del Proyecto

```text
DriveSafe-Giron/
│
├── Data/                       # Carpeta para almacenamiento persistente en JSON
│   ├── clientes.json           # Registro de clientes
│   ├── instructores.json       # Registro de instructores
│   ├── vehiculos.json          # Registro de vehículos
│   └── citas.json              # Registro de citas y agenda
│
├── cliente.py                  # Módulo CRUD y validaciones para clientes
├── instructor.py               # Módulo CRUD y validaciones para instructores
├── vehiculo.py                 # Módulo CRUD y validaciones para vehículos
├── cita.py                     # Lógica de gestión de agenda, disponibilidad e historial
├── menus.py                    # Vistas por consola y capturadores de entrada de datos
└── main.py                     # Flujo principal y punto de entrada del programa
```

---

## 🗃️ Modelo y Estructura de Datos (JSON)

Toda la información se persiste automáticamente en archivos `.json` dentro del directorio `Data/`:

### 1. `Data/clientes.json`
```json
[
    {
        "nit": "1005236072",
        "nombre": "Karen",
        "apellido": "Escobar",
        "id": 1
    }
]
```

### 2. `Data/instructores.json`
```json
[
    {
        "nit": "12345678",
        "nombre": "Carlos",
        "apellidos": "Martínez",
        "especialidad": "2",
        "id": 1
    }
]
```
> *Especialidad:* `1` = Moto | `2` = Carro

### 3. `Data/vehiculos.json`
```json
[
    {
        "placa": "VFT17F",
        "tipo": "1",
        "disponibilidad": "si",
        "id": 1
    }
]
```
> *Tipo:* `1` = Moto | `2` = Carro

### 4. `Data/citas.json`
```json
[
    {
        "idCliente": 1,
        "idInstructor": 1,
        "idVehiculo": 1,
        "fecha": "2026-07-25",
        "hora": "08:00",
        "duracion": "2",
        "observacion": "Clase completada exitosamente",
        "asistencia": "1",
        "id": 1
    }
]
```

---

## 🛠️ Requisitos Previos

* **Python 3.8+**
* Módulos estándar requeridos (incluidos de forma nativa en Python):
  * `json`
  * `datetime`

---

## 🚀 Instalación y Ejecución

1. **Clonar o descargar** la carpeta del repositorio localmente.
2. **Crear la carpeta de datos:**
   Asegúrate de que la carpeta `Data/` existe en el directorio principal del proyecto.
3. **Ejecutar la aplicación:**
   ```bash
   python main.py
   ```

---

## 🖥️ Guía de Uso del Menú

Al iniciar la aplicación con `python main.py`, se muestra el menú interactivo principal:

```text
Seleccione la opcion de menu:
1. Registrar Cliente
2. Registrar Instructor
3. Registrar vehiculo
4. Programar cita
5. Consultar citas
6. Confirmacion de cita
7. Consultar historial por cliente
0. Salir
```

### Formatos Requeridos:
* **Fechas:** `YYYY-MM-DD` (Ejemplo: `2026-07-25`)
* **Hora:** Formato militar `HH:MM` (Ejemplo: `14:00`)
* **Duración:** Número entero en horas (Ejemplo: `2`)
* **Asistencia:** `1` para **Sí**, `2` para **No**

---

## 🧩 Detalles de Módulos

* **`main.py`**: Bucle principal que coordina los submenús y ejecuta las acciones seleccionadas.
* **`menus.py`**: Maneja las entradas por teclado del usuario y los textos de navegación.
* **`cliente.py`**: Administra la persistencia de los clientes y la comprobación de duplicados por NIT.
* **`instructor.py`**: Maneja el registro de instructores y consulta de ID por documento.
* **`vehiculo.py`**: Permite registrar nuevos vehículos en la flota y obtener su ID por placa.
* **`cita.py`**: Módulo núcleo del sistema. Contiene el algoritmo `validacionDisponibilidadCitas` para evitar traslapes de horas según cliente, instructor y vehículo.