import os
import json

os.system("cls")

alunos = {
    "RM1234": {
        "nome": "Elvis",
        "sobrenome": "Silva",
        "nascimento": "2000-05-03"
    }
}

json.load(alunos)