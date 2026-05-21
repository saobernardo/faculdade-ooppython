from classes.Apartment import Apartment
from classes.House import House
from classes.Studio import Studio
from functionalityClasses.OSOperations import OSOperations

import time

class Main:
    contract = {}

    @staticmethod
    def first_menu():
        OSOperations.clear()
        print('''Bem-vindo ao R.M. sistemas. O que deseja fazer?\n\n''')
        print('''
        1. Ver imóveis disponíveis\n
        2. Alugar\n
        
        CTRL+C para fechar o programa
        ''')

        opcao = int(input())

        try:
            Main.handle_options(opcao)
        except ValueError:
            OSOperations.clear()
            print('Informe uma opção válida')
            time.sleep(2)
            Main.first_menu()

    @staticmethod
    def handle_options(opcao):
        OSOperations.clear()

        if opcao not in [1, 2]:
            raise ValueError
        
        match(opcao):
            case 1:
                Main.show_home_options()
            case 2:
                Main.menu_select_home_type()
    
    @staticmethod
    def show_home_options():
        OSOperations.clear()

        apartment = Apartment()
        house = House()
        studio = Studio()

        print(f'''
        --- Apartamento ---
        Aluguel: R${apartment.price:.2f}
        Quarto extra: R${apartment.extra_room_price:.2f}
        Garagem: R${apartment.garage_price:.2f}

        --- Casa ---
        Aluguel: R${house.price:.2f}
        Quarto extra: R${house.extra_room_price:.2f}
        Garagem: R${house.garage_price:.2f}

        --- Estudio ---
        Aluguel: R${studio.price:.2f}
        Quarto extra: R${studio.extra_room_price:.2f}
        Garagem: R${studio.garage_price:.2f}
        ''')
        time.sleep(5)
        Main.first_menu()
    
    @staticmethod
    def menu_select_home_type():
        OSOperations.clear()

        print(f'''Qual tipo de imóvel deseja alugar?
              
              1. Casa
              2. Apartamento
              3. Estúdio
              \n\n
              0. Voltar''')
    
        opcao = int(input())

        match(opcao):
            case 0:
                Main.first_menu()
            case 1:
                House().get_questions()
                Main.first_menu()
            case 2:
                Apartment().get_questions()
                Main.first_menu()
            case 3:
                Studio().get_questions()
                Main.first_menu()
    
if __name__ == "__main__":
    try:
        Main.first_menu()
    except KeyboardInterrupt:
        OSOperations.close_program()