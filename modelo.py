
"""Clases principales del sistema escolar."""


class Persona:
    """Clase padre de alumnos y docentes."""

    def __init__(self, codigo, nombre):
        """Inicializa los datos comunes."""
        self._codigo = str(codigo).strip()
        self._nombre = str(nombre).strip()

    @property
    def codigo(self):
        """Devuelve el codigo."""
        return self._codigo

    @property
    def nombre(self):
        """Devuelve el nombre."""
        return self._nombre

    def describir(self):
        """Describe a la persona."""
        raise NotImplementedError(
            "Las clases hijas deben implementar este metodo."
        )


class Alumno(Persona):
    """Representa a un alumno."""

    def __init__(self, codigo, nombre, carrera):
        """Inicializa los datos del alumno."""
        super().__init__(codigo, nombre)
        self._carrera = str(carrera).strip()

    @property
    def carrera(self):
        """Devuelve la carrera."""
        return self._carrera

    def describir(self):
        """Describe al alumno."""
        return (
            f"Alumno | Codigo: {self._codigo} | "
            f"Nombre: {self._nombre} | Carrera: {self._carrera}"
        )


class Docente(Persona):
    """Representa a un docente."""

    def __init__(self, codigo, nombre, departamento):
        """Inicializa los datos del docente."""
        super().__init__(codigo, nombre)
        self._departamento = str(departamento).strip()

    @property
    def departamento(self):
        """Devuelve el departamento."""
        return self._departamento

    def describir(self):
        """Describe al docente."""
        return (
            f"Docente | Codigo: {self._codigo} | "
            f"Nombre: {self._nombre} | "
            f"Departamento: {self._departamento}"
        )


class Inscripcion:
    """Relaciona una persona con una materia."""

    def __init__(self, codigo_persona, clave_materia):
        """Inicializa una inscripcion."""
        self._codigo_persona = str(codigo_persona)
        self._clave_materia = str(clave_materia)

    @property
    def codigo_persona(self):
        """Devuelve el codigo de la persona."""
        return self._codigo_persona

    @property
    def clave_materia(self):
        """Devuelve la clave de la materia."""
        return self._clave_materia


class Materia:
    """Representa una materia con cupo limitado."""

    def __init__(self, clave, nombre, cupo):
        """Inicializa los datos de la materia."""
        self._clave = str(clave).strip()
        self._nombre = str(nombre).strip()
        self._cupo = cupo
        self._inscripciones = []

    @property
    def clave(self):
        """Devuelve la clave."""
        return self._clave

    @property
    def nombre(self):
        """Devuelve el nombre."""
        return self._nombre

    @property
    def cupo(self):
        """Devuelve el cupo."""
        return self._cupo

    @property
    def inscripciones(self):
        """Devuelve una copia de las inscripciones."""
        return list(self._inscripciones)

    @property
    def lugares_disponibles(self):
        """Calcula los lugares disponibles."""
        return self._cupo - len(self._inscripciones)

    def agregar_inscripcion(self, inscripcion):
        """Agrega una inscripcion a la materia."""
        self._inscripciones.append(inscripcion)
