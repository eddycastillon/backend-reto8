
class Menu:
    def __init__(self, list_menu):
        self.list_menu = list_menu

    def options(self):
        option = 0
        print('Selecciona una opción: ')
        for i in range(len(self.list_menu)):
            message = f'{i+1}) {self.list_menu[i]}'
            if i == len(self.list_menu)-1:
                message += '\n'
            print(message)

        while True:
            
            try:
                option = int(input(':: '))
                if option in range(1,len(self.list_menu)+1):
                        break
                else:
                    print('El valor ingresado no es correcto.')
            except Exception:
                print('El dato ingresado no es valido!') 
        return option 
