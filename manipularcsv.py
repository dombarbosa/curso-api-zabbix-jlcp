import csv
import time


file_exec = 'ponto.csv'
t_start = time.time()
try:
    with open(file_exec, 'w', newline='', encoding='utf-8') as writecsv:
        writingcsv = csv.writer(writecsv, delimiter=';')
        head_file = ['Data', 'Entrada 01', 'Almoco', 'Entrada 02', 'Saida']
        writingcsv.writerow(head_file)

    with open(file_exec) as readcsv:
        readingcsv = csv.reader(readcsv, delimiter=';')
        i = 1
        for [data, turno1, almoco, turno2, saida] in readingcsv:
            print('Item {}:\t{}\t{}\t{}\t{}\t{}'.format(i, data, turno1, almoco, turno2, saida))
            i = i + 1
except Exception as err:
    print("Finalizado com erro: --> {} <-- ".format(err))

t_finished = time.time() - t_start

print("O processo demorou {}".format(t_finished))