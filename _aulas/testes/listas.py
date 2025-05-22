lista = ["laranja", "maçã", "banana", 100, 1000]

for item in lista:
    print(f"- {item}")

#

frutas = ["laranja", "maçã", "banana"]
print(frutas)

frutas += (["abacaxi", "uva"])
print(frutas)

#

calculo = [10, 1, 15, 10, 7]
total = 0

for num in calculo:
    total = total + num
print(total)

#

alunos = [Fred, Daphne, Velma, Salsicha, Scooby]

alunos.sort(reverse = True)
print(alunos)