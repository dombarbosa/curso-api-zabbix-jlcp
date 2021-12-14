with open('/home/dombarbosa/workspace/scripts/scripts-python/lista.txt') as test:
    for l in test:
        print(l.replace(',','\n').replace('\n', '\t'))
