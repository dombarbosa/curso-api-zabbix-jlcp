from tqdm import tqdm
import time

time_lapsed = time.time()


with open('t.txt', 'w', encoding='utf-8') as test:
    for t in tqdm(range(1, 21)):
        l = 'l-%s\n' %t
        test.write(l)


with open('t.txt', 'r', encoding='utf-8') as read_t:
    for r in tqdm(read_t):
        print(r)


time_finished = time.time() - time_lapsed

print('O tempo gasto nesse processo foi de: {}'.format(time_finished))