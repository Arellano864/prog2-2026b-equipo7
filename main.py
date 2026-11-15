"""Menú principal del sistema escolar."""

from modelo import Alumno, Docente, Materia
from sistema import SistemaEscolar
from almacen import guardar, cargar


ARCHIVO_DATOS = "datos.json"


def mostrar_menu():
    """Muestra las opciones del sistema."""

    print("\n========== SISTEMA ESCOLAR SIIAU ==========")
    print("1. Registrar alumno")
    print("2. Registrar docente")
    print("3. Agregar materia")
    print("4. Inscribir persona")
    print("5. Listar información")
    print("6. Guardar información")
    print("0. Guardar y salir")


def ejecutar():
    """Ejecuta el menú principal."""

    sistema = SistemaEscolar()

    try:
        cargar(sistema, ARCHIVO_DATOS)
        print("Información cargada correctamente.")

    except (ValueError, OSError) as error:
        print(f"No se pudieron cargar los datos: {error}")

    while True:

        mostrar_menu()

        opcion = input("Selecciona una opción: ").strip()

        try:

            if opcion == "1":

                codigo = input("Código de 9 dígitos: ")
                nombre = input("Nombre: ")
                carrera = input("Carrera: ")

                alumno = Alumno(
                    codigo,
                    nombre,
                    carrera
                )

                sistema.registrar(alumno)

                print("Alumno registrado correctamente.")

            elif opcion == "2":

                codigo = input("Código de 9 dígitos: ")
                nombre = input("Nombre: ")
                departamento = input("Departamento: ")

                docente = Docente(
                    codigo,
                    nombre,
                    departamento
                )

                sistema.registrar(docente)

                print("Docente registrado correctamente.")

            elif opcion == "3":

                clave = input("Clave de la materia: ")
                nombre = input("Nombre de la materia: ")
                cupo = int(input("Cupo máximo: "))

                materia = Materia(
                    clave,
                    nombre,
                    cupo
                )

                sistema.agregar_materia(materia)

                print("Materia agregada correctamente.")

            elif opcion == "4":

                codigo = input("Código de la persona: ")
                clave = input("Clave de la materia: ")

                sistema.asignar(
                    codigo,
                    clave
                )

                print("Inscripción realizada correctamente.")

            elif opcion == "5":

                sistema.listar()

            elif opcion == "6":

                guardar(
                    sistema,
                    ARCHIVO_DATOS
                )

                print("Información guardada correctamente.")

            elif opcion == "0":

                guardar(
                    sistema,
                    ARCHIVO_DATOS
                )

                print("Información guardada. Hasta luego.")

                break

            else:

                print("Opción no válida.")

        except (ValueError, TypeError) as error:

            print(f"No se pudo realizar la operación: {error}")


if __name__ == "__main__":
    ejecutar()