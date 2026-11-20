
"""Almacenamiento y recuperacion de informacion."""

import json
from pathlib import Path

from modelo import Alumno, Docente, Materia, Inscripcion


class Bitacora:
    """Registra los eventos del sistema."""

    def __init__(self):
        """Inicializa una bitacora vacia."""
        self._eventos = []

    def registrar_evento(self, mensaje):
        """Agrega un evento."""
        self._eventos.append(str(mensaje))

    def obtener_eventos(self):
        """Devuelve una copia de los eventos."""
        return list(self._eventos)


def guardar(sistema, ruta):
    """Guarda el estado del sistema en un archivo JSON."""

    datos = {
        "personas": [],
        "materias": [],
        "eventos": sistema._bitacora.obtener_eventos()
    }

    for persona in sistema._personas.values():

        if isinstance(persona, Alumno):
            datos["personas"].append({
                "tipo": "alumno",
                "codigo": persona.codigo,
                "nombre": persona.nombre,
                "carrera": persona.carrera
            })

        elif isinstance(persona, Docente):
            datos["personas"].append({
                "tipo": "docente",
                "codigo": persona.codigo,
                "nombre": persona.nombre,
                "departamento": persona.departamento
            })

    for materia in sistema._materias.values():

        datos["materias"].append({
            "clave": materia.clave,
            "nombre": materia.nombre,
            "cupo": materia.cupo,
            "inscripciones": [
                inscripcion.codigo_persona
                for inscripcion in materia.inscripciones
            ]
        })

    destino = Path(ruta)

    destino.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    with destino.open("w", encoding="utf-8") as archivo:
        json.dump(
            datos,
            archivo,
            ensure_ascii=False,
            indent=4
        )


def cargar(sistema, ruta):
    """Recupera la informacion del archivo JSON."""

    from sistema import SistemaEscolar

    origen = Path(ruta)

    if not origen.exists():
        sistema._personas.clear()
        sistema._materias.clear()
        sistema._bitacora = Bitacora()
        return

    try:
        with origen.open("r", encoding="utf-8") as archivo:
            datos = json.load(archivo)

    except json.JSONDecodeError as error:
        raise ValueError(
            "El archivo de datos esta dañado."
        ) from error

    except OSError as error:
        raise ValueError(
            "No se pudo leer el archivo."
        ) from error

    if not isinstance(datos, dict):
        raise ValueError(
            "La estructura del archivo de datos es invalida."
        )

    personas = datos.get("personas", [])
    materias = datos.get("materias", [])
    eventos = datos.get("eventos", [])

    if not all(isinstance(lista, list) for lista in (
        personas, materias, eventos
    )):
        raise ValueError(
            "La informacion del archivo tiene un formato invalido."
        )

    temporal = SistemaEscolar()

    for registro in personas:

        if not isinstance(registro, dict):
            raise ValueError(
                "Existe un registro de persona invalido."
            )

        tipo = registro.get("tipo")

        if tipo == "alumno":

            if not all(campo in registro for campo in (
                "codigo", "nombre", "carrera"
            )):
                raise ValueError(
                    "El registro del alumno esta incompleto."
                )

            persona = Alumno(
                registro["codigo"],
                registro["nombre"],
                registro["carrera"]
            )

        elif tipo == "docente":

            if not all(campo in registro for campo in (
                "codigo", "nombre", "departamento"
            )):
                raise ValueError(
                    "El registro del docente esta incompleto."
                )

            persona = Docente(
                registro["codigo"],
                registro["nombre"],
                registro["departamento"]
            )

        else:
            raise ValueError(
                "Tipo de persona desconocido."
            )

        temporal.registrar(persona)

    for registro in materias:

        if not isinstance(registro, dict):
            raise ValueError(
                "Existe un registro de materia invalido."
            )

        if not all(campo in registro for campo in (
            "clave", "nombre", "cupo"
        )):
            raise ValueError(
                "El registro de la materia esta incompleto."
            )

        materia = Materia(
            registro["clave"],
            registro["nombre"],
            registro["cupo"]
        )

        temporal.agregar_materia(materia)

    for registro in materias:

        inscripciones = registro.get("inscripciones", [])

        if not isinstance(inscripciones, list):
            raise ValueError(
                "Las inscripciones tienen un formato invalido."
            )

        for codigo in inscripciones:

            temporal.asignar(
                codigo,
                registro["clave"]
            )

    sistema._personas = temporal._personas
    sistema._materias = temporal._materias
    sistema._bitacora = Bitacora()

    for evento in eventos:
        sistema._bitacora.registrar_evento(evento)
