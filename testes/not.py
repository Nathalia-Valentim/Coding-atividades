senha = input("Digite uma senha: ")

if not senha:
    print("Digite a senha")
elif len(senha) < 3:
    print("A senha deve ter mais de 3 caracteres")
elif not "@" in senha:
    print("A senha deve ter @")
else:
    print("A senha é adequada")