from Helpers.menu import Menu
from Controllers.Profesor import ProfesorController
from Controllers.Alumno import AlumnoController

def menu():
    try:
        print('''
        ==========================
            Sistema de colegio
        ==========================
        ''')
        menu_principal = ["Profesores", "Alumnos", "Cursos", "Periodo Escolar", "Salones", \
        "Malla Curricular", "Registrar Notas", "Salir"]
        respuesta = Menu(menu_principal).show()

        if respuesta == 1:
            profesor = ProfesorController()
            profesor.menu()
            if profesor.salir:
                menu()
        elif respuesta == 2:
            alumno = AlumnoController()
            alumno.menu()
            if alumno.salir:
                app()
        elif respuesta == 3:
            curso = CursoController()
            curso.menu()
            if curso.salir:
                app()
        elif respuesta == 4:
            periodo = PeriodoController()
            periodo.menu()
            if periodo.salir:
                app()
        elif respuesta == 5:
            salon = SalonController()
            salon.menu()
            if salon.salir:
                app()
        elif respuesta == 6:
            malla = MallaController()
            malla.menu()
            if malla.salir:
                app()
        elif respuesta == 7:
            nota = NotasController()
            nota.menu()
            if nota.salir:
                app()

        print("\n Gracias por utilizar el sistema \n")
    except KeyboardInterrupt:
        print('\n Se interrumpio la aplicación')
    except Exception as e:
        print(f'{str(e)}')
    except:
        pass

menu()