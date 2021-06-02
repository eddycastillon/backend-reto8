from app.helpers.menu import Menu
from app.controllers.prestamo import PrestamoController
from app.controllers.alumno import AlumnoController
from app.controllers.libro import LibroController



def menu():
    try:
        print('''
        ==========================
            Sistema de colegio
        ==========================
        ''')
        menu_principal = ["Prestamo", "Alumno", "Libro", "Editorial", "Autor", \
        "Configuracion", "Salir"]
        respuesta = Menu(menu_principal).show()

        if respuesta == 1:
            prestamo = PrestamoController()
            prestamo.menu()
            if prestamo.salir:
                menu()
        elif respuesta == 2:
            alumno = AlumnoController()
            alumno.menu()
            if alumno.salir:
                menu()
        elif respuesta == 3:
            curso = LibroController()
            curso.menu()
            if curso.salir:
                app()
        elif respuesta == 4:
            periodo = EditorialController()
            periodo.menu()
            if periodo.salir:
                app()
        elif respuesta == 5:
            salon = AutorController()
            salon.menu()
            if salon.salir:
                app()
        elif respuesta == 6:
            malla = configuracionController()
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