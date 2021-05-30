from app.models.libro import Libro
from app.helpers.menu import Menu
from app.helpers.helper import input_data, print_table, question

class LibroController:
    def __init__(self):
        self.libro = Libro()
        self.salir = False

    def menu(self):
        try:
            while True:
                print('''
                ==================
                    libros
                ==================
                ''')
                lista_menu = ["Listar", "Buscar", "Crear", "Salir"]
                respuesta = Menu(lista_menu).show()

                if respuesta == 1:
                    self.all_libros()
                elif respuesta == 2:
                    self.search_libro()
                elif respuesta == 3:
                    self.insert_libro()
                else:
                    self.salir = True
                    break
        except Exception as e:
            print(f'{str(e)}')

    def all_libros(self):
        try:
            print('''
            ==========================
                Listar Libros
            ==========================
            ''')
            libros = self.libro.get_libros('libro_id')
            print(print_table(libros, ['ID', 'Nombre', 'Disponible', 'Autor_id', 'Editorial_id']))
            input('\nPresiona una tecla para continuar...')
        except Exception as e:
            print(f'{str(e)}')

    def search_libro(self):
        print('''
        ========================
            Buscar libro
        ========================
        ''')
        try:
            libro_id = input_data("Ingrese el ID del libro >> ", "int")
            libro = self.libro.get_libro({
                'libro_id': libro_id
            })
            print(print_table(libro, ['ID', 'Nombre', 'Edad', 'Correo']))

            if libro:
                if question('¿Deseas dar mantenimiento al libro?'):
                    opciones = ['Editar', 'Eliminar', 'Salir']
                    respuesta = Menu(opciones).show()
                    if respuesta == 1:
                        self.update_libro(libro_id)
                    elif respuesta == 2:
                        self.delete_libro(libro_id)
        except Exception as e:
            print(f'{str(e)}')
        input('\nPresiona una tecla para continuar...')

    def insert_libro(self):
        nombre = input_data('Ingrese el nombre del libro >> ')
        edad = input_data('Ingrese la edad del libro >> ', 'int')
        correo = input_data('Ingrese el correo del libro >> ')
        self.libro.insert_libro({
            'nombres': nombre,
            'edad': edad,
            'correo': correo
        })
        print('''
        ================================
            Nuevo libro agregado
        ================================
        ''')
        self.all_libros()

    def update_libro(self, libro_id):
        nombre = input_data('Ingrese el nuevo nombre del libro >> ')
        edad = input_data('Ingrese la nueva edad del libro >> ', 'int')
        correo = input_data('Ingrese el nuevo correo del libro >> ')
        self.libro.update_libro({
            'libro_id': libro_id
        }, {
            'nombres': nombre,
            'edad': edad,
            'correo': correo
        })
        print('''
        ============================
            libro Actualizado
        ============================
        ''')

    def delete_libro(self, libro_id):
        self.libro.delete_libro({
            'libro_id': libro_id
        })
        print('''
        =========================
            libro Eliminado
        =========================
        ''')

    def prestar_libro(self):

        try:
            self.all_libros()
            search_libro = input_data("Ingrese el ID del libro >> ", "int")
            libro  = self.libro.search_libro({'libro_id': search_libro })
            if libro[0][2]:
                return  True, libro[0][0] 
            else:
                return False, libro[0][0] 
            
        except Exception as e:
            print(f'{str(e)}')
        input('\nPresiona una tecla para continuar...')