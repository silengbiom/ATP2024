

def inserir_sala(cinema, sala):
    if sala not in cinema:
        cinema.append(sala)
    else:
        print("A sala já existe no sistema!")
    print("A sala foi adicionada com sucesso!")


def remover_sala(cinema, sala):
    if sala in cinema:
        cinema.remove(sala)
        print("A sala foi removida com sucesso")
    else:
        print("A sala não foi encontrada")


def listar(cinema):
    for i in range(len(cinema)):
        sala = cinema[i]
        print(f"Sala: {i + 1} | Lotação: {sala[0]} | Filme: {sala[2]}")


def disponivel(cinema, filme, lugar):
    for sala in cinema:
        if sala[2] == filme:
            if lugar not in sala[1]:
                return True
    return False


def vende_bilhete(cinema, filme, lugar):
    for sala in cinema:
        if sala[2] == filme and lugar not in sala[1]:
            sala[1].append(lugar)
            return True
    return False


def listar_disponibilidades(cinema):
    for i in range(len(cinema)):
        sala = cinema[i]
        disponiveis = sala[0] - len(sala[1])
        print(f"Sala {i + 1}: {disponiveis} lugares disponíveis")


def menu():
    cinema = []
    escolha = -1
    while escolha != 0:
        print("\nMenu:\n")
        print("1 -> Listar")
        print("2 -> Disponível")
        print("3 -> Vende bilhete")
        print("4 -> Listar disponibilidades")
        print("5 -> Inserir sala")
        print("6 -> Remover sala")
        print("0 -> Sair")

        escolha = int(input("\nEscolha uma opção: "))

        if escolha == 1:
            listar(cinema)

        elif escolha == 2:
            filme = input("Nome do filme: ")
            lugar = int(input("Número do lugar: "))
            if disponivel(cinema, filme, lugar):
                print(f"Lugar {lugar} disponível.")
            else:
                print(f"Lugar {lugar} não disponível.")

        elif escolha == 3:
            filme = input("Nome do filme: ")
            lugar = int(input("Número do lugar: "))
            if vende_bilhete(cinema, filme, lugar):
                print(f"Bilhete vendido para o Lugar {lugar}.")
            else:
                print("Não foi possível vender o bilhete.")

        elif escolha == 4:
            listar_disponibilidades(cinema)

        elif escolha == 5:
            nlugares = int(input("Lotação da sala: "))
            vendidos = []
            filme = input("Nome do filme: ")
            sala = [nlugares, vendidos, filme]
            inserir_sala(cinema, sala)

        elif escolha == 6:
            numero_sala = int(input("Número da sala a ser removida: ")) - 1
            if 0 <= numero_sala < len(cinema):
                remover_sala(cinema, cinema[numero_sala])
            else:
                print("Sala não encontrada")

        elif escolha == 0:
            print("Saindo do programa.")
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

menu()