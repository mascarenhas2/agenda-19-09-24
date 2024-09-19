import os 


def dia_da_semana():
    os.system ("cls || clear")

    while True:
        try:
            numero = int(input("Digite um dia da semana de 1 a 7: "))

            match(numero):
                case 1:
                    print("\t--Domingo--\n")
                    print("Programacao aleatoria.")
                    break

                case 2:
                    print("\t--Segunda feira--\n")
                    print("==00:00 - 6:10== \n Dormindo")
                    print("==6:10 - 11:30== \n Locomocao + Aula de Christiane ")
                    print("==11:30 - 17:30== \n Locomocao + Trabalho ")
                    print("==17:30 - 18:30== \n Ida pra casa")
                    print("==18:30 - 00:00== \n Descanso/Estudo")
                    break

                case 3:
                    print("\t--Terça Feira--\n")
                    print("==00:00 - 6:10== \n Dormindo")
                    print("==6:10 - 11:30== \n Locomocao + Aula de Christiane ")
                    print("==11:30 - 17:30== \n Locomocao + Trabalho ")
                    print("==17:30 - 18:30== \n Ida pra casa")
                    print("==18:30 - 00:00== \n Descanso/Estudo")
                    break
                case 4:
                    print("\t--Quarta Feira--\n")
                    print("==00:00 - 6:10== \n Dormindo")
                    print("==6:10 - 11:30== \n Locomocao + Aula de Christiane ")
                    print("==11:30 - 17:30== \n Locomocao + Trabalho ")
                    print("==17:30 - 18:30== \n Ida pra casa")
                    print("==18:30 - 00:00== \n Descanso/Estudo")
                    break
                case 5:
                    print("\t--Quinta Feira--\n")
                    print("==00:00 - 6:10== \n Dormindo")
                    print("==6:10 - 11:30== \n Locomocao + Aula de Christiane ")
                    print("==11:30 - 17:30== \n Locomocao + Curso do trabalho ")
                    print("==17:30 - 18:30== \n Ida pra casa")
                    print("==18:30 - 00:00== \n Descanso/Estudo")
                    break
                case 6:
                    print("\t--Sexta feira--\n")
                    print("==00:00 - 6:10== \n Dormindo")
                    print("==6:10 - 11:30== \n Locomocao + Aula de Christiane ")
                    print("==11:30 - 17:30== \n Locomocao + Trabalho ")
                    print("==17:30 - 18:30== \n Ida pra casa")
                    print("==18:30 - 00:00== \n Descanso/Estudo")
                    break
                case 7:
                    print("\t--Sabado--\n")
                    print("==Programacao Aleatoria.==")
                    break
                case _:
                    input("Opção invalida")

        except ValueError:
                print("Entrada inválida. Por favor, insira um número válido.")
                continue
dia_da_semana()
        