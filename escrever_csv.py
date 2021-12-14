import csv
import time

t_start = time.time()

with open('escrita.csv', 'w', newline='', encoding='utf-8') as writecsv:
    writingcsv = csv.writer(writecsv, delimiter=';')
    head_file = ['Data', 'Entrada 01', 'Almoco', 'Entrada 02', 'Saida']
    writingcsv.writerow(head_file)


t_finished = time.time() - t_start

print("O processo demorou {}".format(t_finished))