import json

with open("alunos.json", encoding="utf-8") as arquivo_alunos:
  meus_alunos = json.load(arquivo_alunos)
  
  print(meus_alunos)