'''
Contagem de Votos em uma Eleição de Classe
Você vai simular a apuração de votos para representante de turma, e os
candidatos possíveis são Alice, Bruno e Camila.
    1. Crie uma lista com os nomes dos candidatos.
    2. Pergunte ao usuário quantos votos serão computados
(votos_totais).
    3. Em um for de range(votos_totais), peça para digitar o nome do
candidato (string) e faça append() em votos, desde que o nome seja
um dos nomes válidos (definidos na lista do item 1).
    4. Se o usuário digitar um nome inválido, o voto será considerado
“nulo”, ou seja, não será contabilizado na votação final. Digitou
errado, perdeu o voto.
    5. Ao final, percorra a lista de candidatos e use o método count() em
votos para exibir quantos votos cada um dos três candidatos
recebeu.
    Exemplo de execução:
    Quantos votos serão computados? 7
    Digite o voto #1: Alice
    Digite o voto #2: Bruno
    Digite o voto #3: Camila
    Digite o voto #4: Alice
    Digite o voto #5: Elvis
    Candidato inválido, voto será anulado.
    Digite o voto #6: Alice
    Digite o voto #7: Camila

    Resultado:
    Alice: 3
    Bruno: 1
    Camila: 2
'''

# Solução
