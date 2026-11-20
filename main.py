
"""Menu principal del sistema escolar."""

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
    print("5. Lista de informacion")
    print("6. Guardar informacion")
    print("0. Guardar y salir")


def ejecutar():
    """Ejecuta el menu principal."""

    sistema = SistemaEscolar()

    try:
        cargar(sistema, ARCHIVO_DATOS)
        print("Informacion cargada correctamente.")

    except (ValueError, OSError) as error:
        print(f"No se pudieron cargar los datos: {error}")

    while True:

        mostrar_menu()

        opcion = input("Selecciona una opcion: ").strip()

        try:

            if opcion == "1":

                codigo = input("Codigo de 9 digitos: ")
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

                codigo = input("Codigo de 9 digitos: ")
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

                cupo_texto = input("Cupo maximo: ")

                try:
                    cupo = int(cupo_texto)

                except ValueError:
                    raise ValueError(
                        "El cupo debe ser un numero entero."
                    )

                materia = Materia(
                    clave,
                    nombre,
                    cupo
                )

                sistema.registrar(materia)

                print("Materia agregada correctamente.")

            elif opcion == "4":

                codigo = input("Codigo de la persona: ")
                clave = input("Clave de la materia: ")

                sistema.asignar(
                    codigo,
                    clave
                )

                print("Inscripcion realizada correctamente.")

            elif opcion == "5":

                sistema.listar()

            elif opcion == "6":

                guardar(
                    sistema,
                    ARCHIVO_DATOS
                )

                print("Informacion guardada correctamente.")

            elif opcion == "0":

                guardar(
                    sistema,
                    ARCHIVO_DATOS
                )

                print("Informacion guardada. Hasta luego.")

                break

            else:

                print("Opcion no valida.")

        except (ValueError, TypeError, OSError) as error:

            print(f"No se pudo realizar la operacion: {error}")


if __name__ == "__main__":
    ejecutar()
