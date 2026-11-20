
"""Clases principales del sistema escolar."""


class Persona:
    """Clase padre de alumnos y docentes."""

    def __init__(self, codigo, nombre):
        """Inicializa los datos comunes."""

        codigo = str(codigo).strip()
        nombre = str(nombre).strip()

        if not codigo:
            raise ValueError("El codigo es obligatorio.")

        if not nombre:
            raise ValueError("El nombre es obligatorio.")

        partes = nombre.split()

        for parte in partes:

            palabra = (
                parte.replace("-", "")
                .replace("'", "")
                .replace("’", "")
            )

            if not palabra.isalpha():
                raise ValueError(
                    "El nombre solo debe contener letras."
                )

        self._codigo = codigo
        self._nombre = nombre

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

        carrera = str(carrera).strip()

        if not carrera:
            raise ValueError("La carrera es obligatoria.")

        if not any(letra.isalpha() for letra in carrera):
            raise ValueError(
                "La carrera debe contener letras."
            )

        self._carrera = carrera

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

        departamento = str(departamento).strip()

        if not departamento:
            raise ValueError("El departamento es obligatorio.")

        if not any(letra.isalpha() for letra in departamento):
            raise ValueError(
                "El departamento debe contener letras."
            )

        self._departamento = departamento

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

        codigo_persona = str(codigo_persona).strip()
        clave_materia = str(clave_materia).strip()

        if not codigo_persona:
            raise ValueError(
                "El codigo de persona es obligatorio."
            )

        if not clave_materia:
            raise ValueError(
                "La clave de materia es obligatoria."
            )

        self._codigo_persona = codigo_persona
        self._clave_materia = clave_materia

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

        clave = str(clave).strip()
        nombre = str(nombre).strip()

        if not clave:
            raise ValueError("La clave es obligatoria.")

        if not nombre:
            raise ValueError("El nombre es obligatorio.")

        if not any(letra.isalpha() for letra in nombre):
            raise ValueError(
                "El nombre de la materia debe contener letras."
            )

        if isinstance(cupo, bool) or not isinstance(cupo, int):
            raise ValueError("El cupo debe ser un numero entero.")

        if cupo <= 0:
            raise ValueError(
                "El cupo debe ser mayor que cero."
            )

        self._clave = clave
        self._nombre = nombre
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

        if not isinstance(inscripcion, Inscripcion):
            raise ValueError(
                "Se requiere una inscripcion valida."
            )

        if self.lugares_disponibles <= 0:
            raise ValueError(
                "La materia no tiene lugares disponibles."
            )

        self._inscripciones.append(inscripcion)
