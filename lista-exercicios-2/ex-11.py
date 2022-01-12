
print("|---------| Média anual |---------|")

disciplina = input("Informe qual a disciplina: ")

primeiroBimestre = float(input("Informe sua nota do primeiro bimestre: "))
segundoBimestre = float(input("Informe sua nota do segundo bimestre: "))
terceiroBimestre = float(input("Informe sua nota do terceiro bimestre: "))
quartoBimestre = float(input("Informe sua nota do quarto bimestre: "))

media = (primeiroBimestre + segundoBimestre + terceiroBimestre + quartoBimestre) / 4

# Suas notas na disciplina de DISCIPLINA foram A, B, C e D e a média anual foi de MEDIA

print(
	"Suas notas na disciplina de " + disciplina +
	" foram", primeiroBimestre, ", ", 
	segundoBimestre, ", ", terceiroBimestre, 
	" e", quartoBimestre, 
	" e a média anual foi de", media
)