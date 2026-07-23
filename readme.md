# 🚗 DriveSafe Girón - Sistema de Gestión de Clases de Conducción

**DriveSafe Girón** es un sistema interactivo de consola desarrollado en Python para la administración integral de una escuela de conducción. Permite gestionar clientes, instructores, vehículos y programar citas de práctica de conducción evitando cruces de agenda y garantizando la disponibilidad de recursos.

---

## 📋 Tabla de Contenidos

1. [Descripción General](#-descripción-general)
2. [Características Principales](#-características-principales)
3. [Estructura del Proyecto](#-estructura-del-proyecto)
4. [Modelo de Datos y Persistencia (JSON)](#-modelo-de-datos-y-persistencia-json)
5. [Requisitos del Sistema](#-requisitos-del-sistema)
6. [Instalación y Ejecución](#-instalación-y-ejecución)
7. [Guía de Uso y Menú Principal](#-guía-de-uso-y-menú-principal)
8. [Descripción de Módulos](#-descripción-de-módulos)

---

## 🚘 Descripción General

El software automatiza la logística operativa de la academia **DriveSafe Girón**. Gestiona el registro de los actores involucrados en el servicio de enseñanza de conducción y cuenta con un motor de validación de disponibilidad que impide agendar citas donde haya solapamiento de horarios entre un vehículo, un instructor o un cliente.

---

## ⚡ Características Principales

* **Gestión de Entidades:**
  * **Clientes:** Registro y control por documento de identidad (NIT/Cédula).
  * **Instructores:** Registro con clasificación por especialidad (`1`: Moto, `2`: Carro).
  * **Vehículos:** Registro por tipo (`1`: Moto, `2`: Carro), placa única y estado de disponibilidad.
* **Programación Inteligente de Citas:**
  * Verificación automatizada de disponibilidad basada en fecha, hora militar y duración en horas.
  * Prevención en tiempo real de sobreposición de horarios para cliente, instructor y vehículo.
* **Consultas y Reportes:**
  * Listado general de citas agendadas.
  * Filtro de citas por rango de fechas (`YYYY-MM-DD`).
  * Consulta de citas asociadas a un cliente específico.
* **Seguimiento e Historial:**
  * Registro de observaciones y estado de asistencia posterior a la clase (`1`: Sí, `2`: No).
  * Consulta de historial de clases finalizadas por cliente.

---

## 📁 Estructura del Proyecto

```text
DriveSafe-Giron/
│
├── Data/                       # Directorio de almacenamiento persistente en JSON
│   ├── clientes.json           # Base de datos de clientes
│   ├── instructores.json       # Base de datos de instructores
│   ├── vehiculos.json          # Base de datos de vehículos
│   └── citas.json              # Base de datos de citas y agenda
│
├── cliente.py                  # Gestión CRUD y validaciones de clientes
├── instructor.py               # Gestión CRUD y validaciones de instructores
├── vehiculo.py                 # Gestión CRUD y validaciones de vehículos
├── cita.py                     # Lógica de agenda, disponibilidad e historial
├── menus.py                    # Interfaces de texto e interacción con el usuario
└── main.py                     # Punto de entrada y flujo principal de la aplicación
```

---

## 🗃️ Modelo de Datos y Persistencia (JSON)

La información se almacena localmente en archivos en formato JSON dentro de la carpeta `Data/`:

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
> **Especialidad:** `1` = Moto | `2` = Carro

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
> **Tipo:** `1` = Moto | `2` = Carro

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
        "observacion": "Clase de parqueo completada con éxito",
        "asistencia": "1",
        "id": 1
    }
]
```

---

## 🛠️ Requisitos del Sistema

* **Python 3.8+**
* Módulos estándar requeridos (incluidos por defecto en la biblioteca estándar de Python):
  * `json`
  * `datetime`

---

## 🚀 Instalación y Ejecución

1. **Clonar o descargar** el repositorio en el equipo local.
2. **Verificar estructura:** Asegúrese de que la carpeta `Data/` existe en la raíz del proyecto.
3. **Ejecutar el programa principal:**
   ```bash
   python main.py
   ```

---

## 🖥️ Guía de Uso y Menú Principal

Al ejecutar la aplicación, se presenta el siguiente menú interactivo:

```text
Seleccione la opcion de menu:
1. Registrar Cliente
2. Registrar Instructor
3. Registrar vehiculo
4. Programar cita
5. Consultar citas
6. Registro de asistencia y observaciones de la cita
7. Consultar historial por cliente
0. Salir
```

### Formatos Estándar de Entrada:
* **Fechas:** `YYYY-MM-DD` (Ejemplo: `2026-08-15`)
* **Hora:** Formato militar `HH:MM` (Ejemplo: `14:30`)
* **Duración:** Entero en horas (Ejemplo: `2`)
* **Asistencia:** `1` para **Sí**, `2` para **No**

---

## 🧩 Descripción de Módulos

* **`main.py`**: Orquesta la ejecución del sistema, coordinando el flujo de menús y la interacción entre módulos.
* **`menus.py`**: Contiene la presentación visual por consola y captura de variables de entrada del usuario.
* **`cliente.py`**: Maneja el archivo `clientes.json`, la generación de IDs autoincrementables y la validación de duplicados por NIT.
* **`instructor.py`**: Administra la persistencia de instructores y las búsquedas por documento de identidad.
* **`vehiculo.py`**: Controla el registro de la flota vehicular y validación de existencia previa por placa.
* **`cita.py`**: Implementa la lógica de programación y filtrado de citas. Incluye la función `validacionDisponibilidadCitas` encargada de validar la no superposición de horarios entre recursos.