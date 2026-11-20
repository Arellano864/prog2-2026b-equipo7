
"""Administracion del sistema escolar."""

from modelo import Alumno, Docente, Materia, Inscripcion
from almacen import Bitacora


class SistemaEscolar:
    """Administra personas, materias e inscripciones."""

    def __init__(self):
        """Inicializa el sistema."""
        self._personas = {}
        self._materias = {}
        self._bitacora = Bitacora()

    def _validar_codigo(self, codigo):
        """Comprueba que el codigo tenga nueve digitos."""

        codigo = str(codigo)

        if not codigo.isascii() or not codigo.isdigit():
            raise ValueError(
                "El codigo solo admite digitos."
            )

        if len(codigo) != 9:
            raise ValueError(
                "El codigo debe tener exactamente 9 digitos."
            )

    def registrar(self, objeto):
        """Registra alumnos, docentes o materias."""

        if isinstance(objeto, Materia):
            self.agregar_materia(objeto)
            return

        if not isinstance(objeto, (Alumno, Docente)):
            raise ValueError(
                "Solo se pueden registrar alumnos, docentes o materias."
            )

        self._validar_codigo(objeto.codigo)

        if objeto.codigo in self._personas:
            raise ValueError(
                "Ese codigo ya esta registrado."
            )

        self._personas[objeto.codigo] = objeto

        self._bitacora.registrar_evento(
            f"Se registro {objeto.__class__.__name__}: "
            f"{objeto.codigo}"
        )

    def agregar_materia(self, materia):
        """Registra una materia con cupo limitado."""

        if not isinstance(materia, Materia):
            raise ValueError(
                "El objeto debe ser una materia."
            )

        if materia.clave in self._materias:
            raise ValueError(
                "Esa clave de materia ya esta registrada."
            )

        self._materias[materia.clave] = materia

        self._bitacora.registrar_evento(
            f"Se agrego la materia: {materia.clave}"
        )

    def asignar(self, identificador, clave):
        """Inscribe una persona en una materia."""

        codigo = str(identificador).strip()
        clave = str(clave).strip()

        if clave not in self._materias:
            raise ValueError(
                "La clave de materia no existe."
            )

        if codigo not in self._personas:
            raise ValueError(
                "Primero hay que registrar a la persona."
            )

        materia = self._materias[clave]

        for inscripcion in materia.inscripciones:

            if inscripcion.codigo_persona == codigo:
                raise ValueError(
                    "La persona ya esta inscrita en esta materia."
                )

        if materia.lugares_disponibles <= 0:
            raise ValueError(
                "La materia esta llena."
            )

        nueva_inscripcion = Inscripcion(
            codigo,
            clave
        )

        materia.agregar_inscripcion(
            nueva_inscripcion
        )

        self._bitacora.registrar_evento(
            f"Se inscribio {codigo} en la materia {clave}"
        )

    def listar(self):
        """Imprime todas las personas y materias registradas."""

        print("\n===== PERSONAS REGISTRADAS =====")

        if not self._personas:
            print("No hay personas registradas.")

        else:
            for persona in self._personas.values():
                print(persona.describir())

        print("\n===== MATERIAS =====")

        if not self._materias:
            print("No hay materias registradas.")

        else:
            for materia in self._materias.values():

                print(
                    f"{materia.clave} | {materia.nombre} | "
                    f"Inscritos: "
                    f"{len(materia.inscripciones)}/{materia.cupo}"
                )

                for inscripcion in materia.inscripciones:

                    persona = self._personas[
                        inscripcion.codigo_persona
                    ]

                    print(
                        f"  - {persona.nombre} "
                        f"({persona.codigo})"
                    )
