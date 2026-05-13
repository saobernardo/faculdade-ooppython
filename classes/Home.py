import time

class Home:
    VALUE_CONTRACT = 2000.00

    def __init__(self, price, extra_room_price, garage_price, garage_vacancy_multiplier):
        self.price = price
        self.extra_room_price = extra_room_price
        self.garage_price = garage_price
        self.garage_vacancy_multiplier = garage_vacancy_multiplier

    def show_parameters(self):
        return f'''
         --- {self.__class__.__name__} ---
        Aluguel: R${self.price}\n
        Quarto extra: R${self.extra_room_price if self.extra_room_price != None else 'Sem definição de quarto extra'}
        Garagem: R${self.garage_price}
        Extra por garagem: R${self.garage_vacancy_multiplier if self.garage_vacancy_multiplier != None else 'Sem definição de garagem extra'}
        '''
    
    def get_questions(self):
        while True:
            try:
                bedrooms = int(input('Quantos quartos? '))
                if bedrooms > 0 and bedrooms <= 2:
                    break
                print('Só temos imóveis de 1 ou 2 quartos.')
            except:
                print('Por favor, digite um número inteiro.')

        while True:
            garage = input('''\nDeseja garagem? (S|N) ''')
            if garage in ['S', 'N']:
                garage = True if garage == 'S' else False
                break
            print('Digite um valor válido: S ou N')
        
        while True:
            kids = input('''\nTem crianças? (S|N) ''')
            if kids == 'S' or kids == 'N':
                kids = True if kids == 'S' else False
                break
            print('''Digite um valor válido. S ou N''')

        while True:
            try:
                installments = int(input('''Vai parcelar? Se sim, em quantas vezes? (Máximo 5) \nDigite 0 se não for parcelar: '''))
                if installments <= 5:
                    break
                print('Podemos parcelar é ate 5 vezes apenas')
            except:
                print('Por favor, digite um número inteiro')

        self.resolve_payment(bedrooms, garage, kids, installments)

        return

    def resolve_payment(self, bedrooms, garage, kids, installments):

        value_bedroom = self.extra_room_price if bedrooms == 2 else 0.0
        value_garage = self.garage_price if garage == True else 0.0
        
        if(self.__class__.__name__ == 'Apartment'):
            print('Apartamento')

        time.sleep(5)
        return