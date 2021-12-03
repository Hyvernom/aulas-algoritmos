
idade = int(input('Informe sua Idade:   '))

if (idade <= 25):
    classe = "Jovem Padawan"

elif (idade >= 26 and idade <= 50):
    classe = "Jedi"

elif (idade > 50):
    classe = "Mestre Jedi"

print("Voçê é um :", classe)