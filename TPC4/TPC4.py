import random

def menu():
    lista = []
    resposta = True

    while resposta:
        print("Seja bem-vindo! Escolha uma das opções para continuar:")
        print("0 = Sair;")
        print("1 = Criar lista;")
        print("2 = Ler lista;")
        print("3 = Soma;")
        print("4 = Média;")
        print("5 = Maior;")
        print("6 = Menor;")
        print("7 = estaOredenada por ordem Crescente;")
        print("8 = estaOrdenada por ordem decrescente;")
        print("9 = procura um elemento;")

        escolha = input("Escolha a opção para continuar")

        if escolha == "0":
            print("Obrigado por ter usado o nosso programa!")
            print("Lista final:", lista)
            resposta = False
        
        elif escolha == "1":
            n = int(input("Insira o número de elementos da lista:"))
            for i in range(n):
                num = random.randint(1,100)
                lista.append(num)
            print("Lista criada:", lista)

        elif escolha == "2":
            lista = []
            nu = int(input("Quantos números pretende inserir na lista?"))
            i = 0
            while i < nu:
                p = int(input("Insira o/os número/números:"))
                lista.append(p)
                i = i + 1
            print("Lista criada:", lista)

        elif escolha == "3":
            soma = 0
            for i in lista:
                soma = soma + i
            print("A soma dos elementos é:", soma)

        elif escolha == "4":
            soma = 0
            if len(lista) != 0:
                for i in lista:
                    soma = soma + i
                media = soma / len(lista)
                print("A média dos elementos é:", media)
            else:
                print("a lista está vazia!")


        elif escolha == "5":
            maior = 0
            if len(lista) != 0:
                for i in lista:
                    if i > maior:
                        maior = i
                print("O maior elemento da lista é:", maior)
            else:
                print("A lista está vazia!")


        elif escolha == "6":
            menor = lista[0]
            if len(lista) != 0:
                for i in lista:
                    if i < menor:
                        menor = i
                print("O menor elemento da lista é:", menor)
            else:
                print("A lista está vazia!")

        elif escolha == "7":
            lista1 = sorted(lista)
            if lista == lista1:
                print("Sim, a lista está ordenada de forma crescente")
            else:
                print("Não, a lista não está ordenada de forma crescente")
    
        elif escolha == "8":
            lista2 = sorted(lista, reverse=True)
            if lista == lista2:
                print("Sim, a lista está ordenada de forma decrescente")
            else:
                print("Não, a lista não está ordenada de forma decrescente")
        
        elif escolha == "9":
            elemento = int(input("Insira o elemento a procurar:"))
            if elemento in lista:
                numero = lista.index(elemento)
                print("O elemento está na posição:", numero)
            else:
                print("-1, o elemento não pertence à lista")
        
        else:
            print("A opção inserida é inválida! Tente novamente")

menu()