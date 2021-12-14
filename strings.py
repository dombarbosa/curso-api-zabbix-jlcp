cidade = 'Sao luis'
print(cidade)

cidade = cidade.replace(' ', '-')
print(cidade)

cidade_fin_s = cidade.endswith('s')
print(cidade_fin_s)

cidade_ini_s = cidade.startswith('S')
print(cidade_ini_s)

cidade_split = cidade.split('-')
print(cidade_split)

cidadejoin = ' '.join(cidade_split)
print(cidadejoin)
