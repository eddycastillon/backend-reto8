from app.models.alumno import Alumno
from app.helpers.menu import Menu
from app.helpers.helper import input_data, print_table, question

class AlumnoController:
    def __init__(self):
        self.alumno = Alumno()
        self.salir = False

    def menu(self):
        try:
            while True:
                print('''
                ==================
                    Alumnos
                ==================
                ''')
                lista_menu = ["Listar", "Buscar", "Crear", "Salir"]
                respuesta = Menu(lista_menu).show()

                if respuesta == 1:
                    self.all_alumnos()
                elif respuesta == 2:
                    self.search_alumno()
                elif respuesta == 3:
                    self.insert_alumno()
                else:
                    self.salir = True
                    break
        except Exception as e:
            print(f'{str(e)}')

    def all_alumnos(self):
        try:
            print('''
            ==========================
                Listar Alumnos
            ==========================
            ''')
            alumnos = self.alumno.get_alumnos('alumno_id')
            print(print_table(alumnos, ['ID', 'Nombre', 'Apellido_paterno', 'Apellido_materno', 'documento_identidad']))
            input('\nPresiona una tecla para continuar...')
        except Exception as e:
            print(f'{str(e)}')

    def search_alumno(self):
        print('''
        ========================
            Buscar Alumno
        ========================
        ''')
        try:
            alumno_id = input_data("Ingrese el ID del alumno >> ", "int")
            alumno = self.alumno.get_alumno({
                'alumno_id': alumno_id
            })
            print(print_table(alumno, ['ID', 'Nombre', 'Edad', 'Correo']))

            if alumno:
                if question('¿Deseas dar mantenimiento al alumno?'):
                    opciones = ['Editar', 'Eliminar', 'Salir']
                    respuesta = Menu(opciones).show()
                    if respuesta == 1:
                        self.update_alumno(alumno_id)
                    elif respuesta == 2:
                        self.delete_alumno(alumno_id)
        except Exception as e:
            print(f'{str(e)}')
        input('\nPresiona una tecla para continuar...')

    def insert_alumno(self):
        nombre = input_data('Ingrese el nombre del alumno >> ')
        edad = input_data('Ingrese la edad del alumno >> ', 'int')
        correo = input_data('Ingrese el correo del alumno >> ')
        self.alumno.insert_alumno({
            'nombres': nombre,
            'edad': edad,
            'correo': correo
        })
        print('''
        ================================
            Nuevo alumno agregado
        ================================
        ''')
        self.all_alumnos()

    def update_alumno(self, alumno_id):
        nombre = input_data('Ingrese el nuevo nombre del alumno >> ')
        edad = input_data('Ingrese la nueva edad del alumno >> ', 'int')
        correo = input_data('Ingrese el nuevo correo del alumno >> ')
        self.alumno.update_alumno({
            'alumno_id': alumno_id
        }, {
            'nombres': nombre,
            'edad': edad,
            'correo': correo
        })
        print('''
        ============================
            Alumno Actualizado
        ============================
        ''')

    def delete_alumno(self, alumno_id):
        self.alumno.delete_alumno({
            'alumno_id': alumno_id
        })
        print('''
        =========================
            Alumno Eliminado
        =========================
        ''')

