"""Pruebas del sistema escolar."""

import tempfile
import unittest
from pathlib import Path

from modelo import Alumno, Docente, Materia
from sistema import SistemaEscolar
from almacen import guardar, cargar


class PruebasSistemaEscolar(unittest.TestCase):
    """Comprueba el funcionamiento del sistema."""

    def setUp(self):
        """Prepara un sistema nuevo para cada prueba."""

        self.sistema = SistemaEscolar()

        self.sistema.agregar_materia(
            Materia("MAT101", "Matematicas", 2)
        )

    def test_registrar_alumno(self):
        """Comprueba el registro de un alumno."""

        alumno = Alumno(
            "123456789",
            "Ana Lopez",
            "Ciberseguridad"
        )

        self.sistema.registrar(alumno)

        self.assertIn(
            "123456789",
            self.sistema._personas
        )

    def test_registrar_docente(self):
        """Comprueba el registro de un docente."""

        docente = Docente(
            "987654321",
            "Luis Perez",
            "Computacion"
        )

        self.sistema.registrar(docente)

        self.assertIn(
            "987654321",
            self.sistema._personas
        )

    def test_nombre_vacio(self):
        """Rechaza nombres vacíos."""

        with self.assertRaisesRegex(
            ValueError, "nombre es obligatorio"
        ):
            self.sistema.registrar(
                Alumno("123456789", "   ", "Ciberseguridad")
            )

    def test_carrera_vacia(self):
        """Rechaza alumnos sin carrera."""

        with self.assertRaisesRegex(
            ValueError, "carrera"
        ):
            self.sistema.registrar(
                Alumno("123456789", "Ana", " ")
            )

    def test_departamento_vacio(self):
        """Rechaza docentes sin departamento."""

        with self.assertRaisesRegex(
            ValueError, "departamento"
        ):
            self.sistema.registrar(
                Docente("123456789", "Luis", "")
            )

    def test_codigo_longitud(self):
        """Rechaza códigos que no tienen nueve dígitos."""

        with self.assertRaisesRegex(
            ValueError, "9 dígitos"
        ):
            self.sistema.registrar(
                Alumno("12345", "Ana", "Ciberseguridad")
            )

    def test_codigo_con_letras(self):
        """Rechaza códigos con letras."""

        with self.assertRaisesRegex(
            ValueError, "solo admite dígitos"
        ):
            self.sistema.registrar(
                Alumno("12345AB89", "Ana", "Ciberseguridad")
            )

    def test_codigo_repetido(self):
        """Rechaza códigos repetidos entre tipos."""

        self.sistema.registrar(
            Alumno("123456789", "Ana", "Ciberseguridad")
        )

        with self.assertRaisesRegex(
            ValueError, "ya está registrado"
        ):
            self.sistema.registrar(
                Docente("123456789", "Luis", "Computacion")
            )

    def test_materia_invalida(self):
        """Comprueba las validaciones de materias."""

        with self.assertRaisesRegex(ValueError, "clave"):
            self.sistema.agregar_materia(
                Materia(" ", "Historia", 10)
            )

        with self.assertRaisesRegex(ValueError, "nombre"):
            self.sistema.agregar_materia(
                Materia("HIS101", " ", 10)
            )

        with self.assertRaisesRegex(ValueError, "cupo"):
            self.sistema.agregar_materia(
                Materia("HIS102", "Historia", 0)
            )

    def test_materia_inexistente(self):
        """Rechaza inscripciones en materias inexistentes."""

        self.sistema.registrar(
            Alumno("123456789", "Ana", "Ciberseguridad")
        )

        with self.assertRaisesRegex(ValueError, "no existe"):
            self.sistema.asignar(
                "123456789",
                "NOEXISTE"
            )

    def test_persona_no_registrada(self):
        """Rechaza personas que no están registradas."""

        with self.assertRaisesRegex(ValueError, "Primero"):
            self.sistema.asignar(
                "123456789",
                "MAT101"
            )

    def test_inscripcion_duplicada(self):
        """Rechaza inscripciones duplicadas."""

        self.sistema.registrar(
            Alumno("123456789", "Ana", "Ciberseguridad")
        )

        self.sistema.asignar(
            "123456789",
            "MAT101"
        )

        with self.assertRaisesRegex(
            ValueError, "ya está inscrita"
        ):
            self.sistema.asignar(
                "123456789",
                "MAT101"
            )

    def test_materia_llena(self):
        """Rechaza inscripciones cuando se llena la materia."""

        self.sistema.registrar(
            Alumno("123456789", "Ana", "Ciberseguridad")
        )

        self.sistema.registrar(
            Alumno("234567891", "Beto", "Redes")
        )

        self.sistema.registrar(
            Alumno("345678912", "Caro", "Software")
        )

        self.sistema.asignar("123456789", "MAT101")
        self.sistema.asignar("234567891", "MAT101")

        with self.assertRaisesRegex(
            ValueError, "está llena"
        ):
            self.sistema.asignar(
                "345678912",
                "MAT101"
            )

    def test_archivo_inexistente(self):
        """Comprueba que el sistema arranque sin archivo."""

        with tempfile.TemporaryDirectory() as carpeta:

            ruta = Path(carpeta) / "datos.json"

            cargar(self.sistema, ruta)

            self.assertEqual(
                len(self.sistema._personas), 0
            )

            self.assertEqual(
                len(self.sistema._materias), 0
            )

    def test_guardar_y_cargar(self):
        """Comprueba la recuperación de información."""

        self.sistema.registrar(
            Alumno("123456789", "Ana", "Ciberseguridad")
        )

        self.sistema.asignar(
            "123456789",
            "MAT101"
        )

        with tempfile.TemporaryDirectory() as carpeta:

            ruta = Path(carpeta) / "datos.json"

            guardar(self.sistema, ruta)

            nuevo_sistema = SistemaEscolar()

            cargar(nuevo_sistema, ruta)

            self.assertIn(
                "123456789",
                nuevo_sistema._personas
            )

            self.assertIn(
                "MAT101",
                nuevo_sistema._materias
            )

            self.assertEqual(
                len(
                    nuevo_sistema._materias[
                        "MAT101"
                    ].inscripciones
                ),
                1
            )


if __name__ == "__main__":
    unittest.main(verbosity=2)