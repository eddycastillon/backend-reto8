from app.helpers.menu import Menu
from app.controllers.prestamo import PrestamoController
from app.controllers.alumno import AlumnoController
from app.controllers.libro import LibroController
from app.controllers.devolucion import DevolucionController



def menu():
    try:
        print('''
        ==========================
            Sistema de colegio
        ==========================
        ''')
        menu_principal = ["Prestamo", "Devolucion", "Alumno", "Libro", "Editorial", "Autor", \
        "Configuracion", "Salir"]
        respuesta = Menu(menu_principal).show()

        if respuesta == 1:
            prestamo = PrestamoController()
            prestamo.menu()
            if prestamo.salir:
                menu()
        elif respuesta == 2:
            alumno = DevolucionController()
            alumno.menu()
            if alumno.salir:
                app()
        elif respuesta == 3:
            curso = AlumnoController()
            curso.menu()
            if curso.salir:
                app()
        elif respuesta == 4:
            periodo = LibroController()
            periodo.menu()
            if periodo.salir:
                app()
        elif respuesta == 5:
            salon = EditorialController()
            salon.menu()
            if salon.salir:
                app()
        elif respuesta == 6:
            malla = AutorController()
            malla.menu()
            if malla.salir:
                app()
        elif respuesta == 7:
            nota = configuracionController()
            nota.menu()
            if nota.salir:
                menu()

        print("\n Gracias por utilizar el sistema \n")
    except KeyboardInterrupt:
        print('\n Se interrumpio la aplicación')
    except Exception as e:
        print(f'{str(e)}')
    except:
        pass

menu()