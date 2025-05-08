'''
Cadastro com múltiplas validações
Monte um cadastro de alunos que pergunta:
• Nome (string)
• Idade (inteiro positivo)
• Nota (float de 0 a 10)
Valide cada entrada com try/except e mensagens personalizadas. Faça o
cadastro repetir até que todas as entradas estejam corretas.
'''

# Solução
while True:
    try:
        nome = input("Nome do aluno: ").strip()
        if nome == "":
            raise ValueError("Nome não pode ser vazio.")

        idade = int(input("Idade: "))
        if idade <= 0:
            raise ValueError("Idade deve ser um número positivo.")

        nota = float(input("Nota (0 a 10): "))
        if nota < 0 or nota > 10:
            raise ValueError("Nota deve estar entre 0 e 10.")

        print("\nCadastro realizado com sucesso:")
        print(f"Nome: {nome}, Idade: {idade}, Nota: {nota}")
        break

    except ValueError as erro:
        print(f"Erro: {erro}")
