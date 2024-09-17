pin = 1234
senha= int (input("Informe sua senha: "))
while senha !=pin and tent<3
    senha = int(input(f"Senha errada \n"
                      f"Você tem {3-tent}\n"
                      f"Informe sua senha novamente: "))
    tent+=1
    if tent ===3 and senha != pin:
        print("Senha bloqueada!")
    else:
        print("Login efetuado com sucesso") 