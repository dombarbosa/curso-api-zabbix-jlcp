altura = float(input('Digite sua altura:\n'))
peso = float(input('Digite seu peso:\n'))
imc = round((peso / (altura**2)),2)

print(imc)

if imc >= 16 and imc <= 16.9:
    print("Te liga que tu vai voar")
if imc >=17 and imc <= 29.9:
    print("Está no peso")
if imc >= 30:
    print("Te liga doido! Que tu tá pesado")


