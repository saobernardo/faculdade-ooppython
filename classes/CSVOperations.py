import time
import csv

class CSVOperations:
    @staticmethod
    def export(total_value, price, installments, installment_value, value_garage, value_bedroom):
        with open('rentdata.csv', 'w',  newline='') as csvfile:
            fieldnames = ['total_value', 'price', 'installment', 'installment_value', 'value_garage', 'value_bedroom']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()

            i = 1
            while i <= installments:
                writer.writerow({'total_value': total_value, 'price': price, 'installment': i, 'installment_value': installment_value, 'value_garage': value_garage, 'value_bedroom': value_bedroom})
                i += 1

        return