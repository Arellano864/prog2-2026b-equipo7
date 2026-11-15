# Hito 2 - Sistema escolar SIIAU

## Descripcion

Sistema escolar desarrollado en Python para administrar
alumnos, docentes, materias e inscripciones.

El programa permite registrar personas, crear materias
con cupo limitado y realizar inscripciones.

Tambien cuenta con almacenamiento de informacion
para conservar los datos entre ejecuciones.

## Integrantes

- Johan Arellano Gallardo
- Jorge Ivan Ortega Meza

## Reparto del trabajo

### Johan Arellano Gallardo

- modelo.py
- almacen.py

Responsable de las clases principales, herencia,
polimorfismo, encapsulamiento y persistencia.

### Jorge Ivan Ortega Meza

- sistema.py
- pruebas.py

Responsable del registro, asignaciones,
validaciones y pruebas del programa.

### Ambos integrantes

- main.py
- README.md

Responsables de la integracion y documentacion
del proyecto.

## Archivos del proyecto

- modelo.py: clases principales.
- almacen.py: bitacora y almacenamiento.
- sistema.py: logica del sistema.
- pruebas.py: pruebas automaticas.
- main.py: menu principal.
- README.md: documentacion.

## Requisitos

Python 3.10 o posterior.

No requiere instalar librerias externas.

## Ejecutar el programa

Abrir una terminal en la carpeta del proyecto
y ejecutar:

python main.py

## Ejecutar las pruebas

python -m unittest -v pruebas.py

## Persistencia

El sistema utiliza un archivo JSON llamado
datos.json para guardar la informacion.

Si el archivo no existe, el programa inicia vacio.

El archivo de datos no se incluye en la entrega.