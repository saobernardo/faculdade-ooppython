from classes.CSVOperations import CSVOperations

import time

class Home:
    VALUE_CONTRACT = 2000.00
    NO_KIDS_DISCOUNT = 0.05

    def __init__(self, price, extra_room_price, garage_price, garage_vacancy_multiplier):
        self.price = price
        self.extra_room_price = extra_room_price
        self.garage_price = garage_price
        self.garage_vacancy_multiplier = garage_vacancy_multiplier
    
    def get_questions(self):
        while True:
            try:
                bedrooms = int(input('Quantos quartos? '))
                if bedrooms > 0 and bedrooms <= 2:
                    break
                print('Só temos imóveis de 1 ou 2 quartos.')
            except ValueError:
                print('Por favor, digite um número inteiro.')

        while True:
            garage = input('''\nDeseja garagem? (S|N) ''')
            if garage in ['S', 'N']:
                garage = True if garage == 'S' else False
                break
            print('Digite um valor válido: S ou N')
        
        vacancy_garage = 0
        while True:
            if garage == True and self.__class__.__name__ == 'Studio':
                while True:
                    try:
                        vacancy_garage = int(input('Quantas vagas? '))
                        if vacancy_garage >= 2:
                            break
                        print('Mínimo de duas vagas')
                    except ValueError:
                        print('Por favor, digite um número inteiro.')
            break
            
        
        while True:
            kids = input('''\nTem crianças? (S|N) ''')
            if kids in ['S', 'N']:
                kids = True if kids == 'S' else False
                break
            print('''Digite um valor válido. S ou N''')

        while True:
            try:
                installments = int(input('''Vai parcelar? Se sim, em quantas vezes? (Máximo 5) \nDigite 1 se não for parcelar: '''))
                if installments > 0 and installments <= 5:
                    break
                print('Podemos parcelar em ate 5 vezes apenas')
            except:
                print('Por favor, digite um número inteiro')

        result = self.resolve_payment(self.price, bedrooms, garage, kids, installments, vacancy_garage)

        self.exportCSV(result)

        print('Dados salvos com sucesso')
        time.sleep(3)

        return

    def resolve_payment(self, price, bedrooms, garage, kids, installments, vacancy_garage = 0):
        value_bedroom = self.extra_room_price if bedrooms >= 2 else 0.0
        value_garage = self.garage_price if garage == True else 0.0

        if(self.__class__.__name__ == 'Studio'):
            value_garage = value_garage + (self.garage_vacancy_multiplier * (vacancy_garage - 2)) if vacancy_garage > 2 else value_garage

        total_value = self.VALUE_CONTRACT + price + value_bedroom + value_garage

        if(kids == False):
            discount = total_value * self.NO_KIDS_DISCOUNT
            total_value -= discount

        print(f'''Valor total: {total_value}\n''')
        time.sleep(3)

        if(installments > 1):
            installment_value = total_value / installments
            print(f'''
                Valor das parcelas: {installment_value:.2f}\n
                Parcelado em {installments} vezes, sem juros
                ''')
            time.sleep(4)

        return {
            "total_value": total_value,
            "price": price,
            "installments": installments,
            "installment_value" : installment_value if installments > 1 else 0.0,
            "value_garage": value_garage,
            "value_bedroom": value_bedroom
        }
    
    def exportCSV(self, data):
        while True:
            response = input('Deseja exportar? (S/N) ')

            if response in ['S', 'N']:
                if response == "N":
                    return
                
                CSVOperations.export(data['total_value'], data['price'], data['installments'], data['installment_value'], data['value_garage'], data['value_bedroom'])

                break
            print('''Digite um valor válido. S ou N''')
        
