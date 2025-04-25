alunos_manha = ("João", "Maria", "Thiago")
alunos_noite = ("Anna", "Fernanda", "João")

alunos = alunos_manha + alunos_noite

for item in alunos:
    print("- ", item)

#
print("")
#

aluno = {
    "nome": "Felicity",
    "rm": "126702",
    "turma": "1TDCPG",
    "nota": 10,
    "aprovado": True,
}

print(aluno["rm"], "-", aluno["nome"])

#
print("") 
#

aluno = {
  "nome": "Elvis",
  "turma": "1TDCPG",
  "rm": 1234
}

nota = float(input(f"Qual a nota do aluno {aluno['nome']}? "))

aluno["nota"] = nota

aluno["aprovado"] = nota >= 6

### É o mesmo que:
# if nota >= 6:
#   aluno["aprovado"] = True
# else:
#   aluno["aprovado"] = False

if aluno["aprovado"] == True:
  aluno["turma"] = "2TDCPG"

print(aluno)

#
print("") 
#

alunos_manha = ("João", "Maria", "José")
alunos_noite = ("Ana", "Beatriz", 10, True, ['a', 'b'])

alunos = alunos_manha + alunos_noite

alunos[3] = "Elvis" # Isso não funciona, pois a tupla não permite alteração!!

print(alunos.index("Beatriz"))

# for item in alunos:
#   print('-', item)

lista = ["a", 10, True, (1, 2, 3)]
tupla = ("a", 10, True, (1, 2, 3))

#
print("") 
#

alunos = {
  "1234": {
    "nome": "Elvis",
    "turma": "1TDCPG"
  },
  "1235": {
    "nome": "Maria",
    "turma": "1TDCPG"
  }
}

rm = input("Qual RM você quer consultar? ")

if rm in alunos:
  aluno = alunos[rm]
  # aluno = alunos.get(rm)
  print(aluno['nome'])
else:
  print("Este RM não está cadastrado")

#
print("") 
#

try:
   num1 = int(input("Digite o primeiro número: "))
   num2 = int(input("Digite o segund número: "))
   
   resultado = num1 / num2
except ZeroDivisionError:
   print("Não é possível dividir por zero")
except ValueError:
   print("Informe apenas números inteiros")
else:
   print(resultado)