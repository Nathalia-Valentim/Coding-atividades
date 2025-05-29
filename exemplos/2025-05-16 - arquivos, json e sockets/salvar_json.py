import json

dict = {
  "RM1234": {
    "nome": "Elvis",
    "nascimento": "2000-01-25"
  },
  "RM1235": {
    "nome": "João",
    "nascimento": "2001-02-12"
  }
}

with open("alunos.json", "w", encoding="utf-8") as arquivo_alunos:
  json.dump(dict, arquivo_alunos, indent=2, ensure_ascii=False)