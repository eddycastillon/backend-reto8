from app.controllers.libro import LibroController
from app.models.prestamo import Prestamo
from app.helpers.menu import Menu
from app.helpers.helper import input_data, print_table, question

class PrestamoController:
    def __init__(self):
        self.prestamo = Prestamo()
        self.salir = False

    def menu(self):
        try:
            while True:
                print('''
                ==================
                    Prestamos
                ==================
                ''')
                lista_menu = ["Listar", "Buscar", "Crear", "Salir"]
                respuesta = Menu(lista_menu).show()

                if respuesta == 1:
                    self.all_prestamos()
                elif respuesta == 2:
                    self.search_prestamo()
                elif respuesta == 3:
                    self.insert_prestamo()
                else:
                    self.salir = True
                    break
        except Exception as e:
            print(f'{str(e)}')

    def all_prestamos(self):
        try:
            print('''
            ==========================
                Listar prestamos
            ==========================
            ''')
            prestamos = self.prestamo.get_prestamos('prestamo_id')
            print(print_table(prestamos, ['ID', 'Fecha_inicio', 'Fecha_fin', 'Alumno_id', 'Libro_id']))
            input('\nPresiona una tecla para continuar...')
        except Exception as e:
            print(f'{str(e)}')

    def search_prestamo(self):
        print('''
        ========================
            Buscar prestamo
        ========================
        ''')
        try:
            prestamo_id = input_data("Ingrese el ID del prestamo >> ", "int")
            prestamo = self.prestamo.get_prestamo({
                'prestamo_id': prestamo_id
            })
            print(print_table(prestamo, ['ID', 'Nombre', 'Edad', 'Correo']))

            if prestamo:
                if question('¿Deseas dar mantenimiento al prestamo?'):
                    opciones = ['Editar', 'Eliminar', 'Salir']
                    respuesta = Menu(opciones).show()
                    if respuesta == 1:
                        self.update_prestamo(prestamo_id)
                    elif respuesta == 2:
                        self.delete_prestamo(prestamo_id)
        except Exception as e:
            print(f'{str(e)}')
        input('\nPresiona una tecla para continuar...')

    def insert_prestamo(self):
        libro = LibroController()
        libro_disponible, libro_id = libro.prestar_libro()
    
        if libro_disponible:
            fecha_inicio = input_data('Ingrese fecha de inicio >> ')
            fecha_fin = input_data('Ingrese fecha de fin >> ')
            alumno_id = input_data('Ingrese alumno_id >> ', 'int')
            self.prestamo.insert_prestamo({
                'fecha_inicio': fecha_inicio,
                'fecha_fin': fecha_fin,
                'alumno_id': alumno_id,
                'libro_id': libro_id
            })
            print('''
            ================================
                Nuevo prestamo agregado
            ================================
            ''')
            self.all_prestamos()
        else:
            print("libro no disponible")


    def update_prestamo(self, prestamo_id):
        nombre = input_data('Ingrese el nuevo nombre del prestamo >> ')
        edad = input_data('Ingrese la nueva edad del prestamo >> ', 'int')
        correo = input_data('Ingrese el nuevo correo del prestamo >> ')
        self.prestamo.update_prestamo({
            'prestamo_id': prestamo_id
        }, {
            'nombres': nombre,
            'edad': edad,
            'correo': correo
        })
        print('''
        ============================
            prestamo Actualizado
        ============================
        ''')

    def delete_prestamo(self, prestamo_id):
        self.prestamo.delete_prestamo({
            'prestamo_id': prestamo_id
        })
        print('''
        =========================
            prestamo Eliminado
        =========================
        ''')

