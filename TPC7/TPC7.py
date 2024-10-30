
import matplotlib.pyplot as plt

def medias(tabMeteo):
    res = []
    for registo in tabMeteo:
        data, temp_min, temp_max, precipitacao = registo
        temperatura_media = (temp_min + temp_max) / 2
        res.append((data, temperatura_media))
    return res

def guardaTabMeteo(t, fnome):
    f = open(fnome, 'w')
    for registo in t:
        f.write(f"{registo}\n")
    f.close()
    return

def carregaTabMeteo(fnome):
    res = []
    f = open(fnome, 'r')
    for linha in f:
        registo = eval(linha.strip())
        res.append(registo)
    f.close()
    return res

def minMin(tabMeteo):
    minima = float('inf')
    for registo in tabMeteo:
        data, temp_min, temp_min, temp_max = registo
        if temp_min < minima:
            minima = temp_min
    return minima

def amplTerm(tabMeteo):
    res = []
    for registo in tabMeteo:
        data, temp_min, temp_max, precipitacao = registo
        amplitude = temp_max - temp_min
        res.append((data, amplitude))
    return res

def maxChuva(tabMeteo):
    max_prec = float('-inf')
    max_data = None
    for registo in tabMeteo:
        data, temp_min, temp_max, precip = registo
        if precip > max_prec:
            max_prec = precip
            max_data = data
    return (max_data, max_prec)

def diasChuvosos(tabMeteo, p):
    res = []
    for registo in tabMeteo:
        data, temp_min, temp_max, precip = registo
        if precip > p:
            res.append((data, precip))
    return res

def maxPeriodoCalor(tabMeteo, p):
    max_consecutivos = 0
    atuais_consecutivos = 0

    for registo in tabMeteo:
        data, temp_min, temp_max, precip = registo
        if precip < p:
            atuais_consecutivos += 1
            max_consecutivos = max(max_consecutivos, atuais_consecutivos)
        else:
            atuais_consecutivos = 0

    return max_consecutivos

def grafTabMeteo(t):
    datas = [registo[0] for registo in t]
    temps_min = [registo[1] for registo in t]
    temps_max = [registo[2] for registo in t]
    precip = [registo[3] for registo in t]

    plt.figure(figsize=(10, 6))

    plt.subplot(3, 1, 1)
    plt.plot(datas, temps_min, label='Temperatura Mínima', color='blue')
    plt.ylabel('Temperatura (°C)')
    plt.title('Temperaturas Mínimas')
    plt.grid()

    plt.subplot(3, 1, 2)
    plt.plot(datas, temps_max, label='Temperatura Máxima', color='red')
    plt.ylabel('Temperatura (°C)')
    plt.title('Temperaturas Máximas')
    plt.grid()

    plt.subplot(3, 1, 3)
    plt.bar(datas, precip, label='Precipitação', color='green')
    plt.ylabel('Precipitação (mm)')
    plt.title('Precipitação')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

tabMeteo1 = [((2022, 1, 20), 2, 16, 0), 
              ((2022, 1, 21), 1, 13, 0.2), 
              ((2022, 1, 22), 7, 17, 0.01)]

def menu():
    while True:
        print("\nMenu:")
        print("1. Calcular a média das temperaturas")
        print("2. Guardar a tabela meteorológica num ficheiro")
        print("3. Carregar a tabela meteorológica de um ficheiro")
        print("4. Calcular a temperatura mínima")
        print("5. Calcular a amplitude térmica")
        print("6. Encontrar o dia com precipitação máxima")
        print("7. Dias com precipitação acima de um limite")
        print("8. Máximo de dias com precipitação abaixo de um limite")
        print("9. Mostrar o gráfico de temperaturas e precipitação")
        print("0. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            print(medias(tabMeteo1))
        elif escolha == '2':
            guardaTabMeteo(tabMeteo1, "meteorologia.txt")
            print("Tabela meteorológica guardada em 'meteorologia.txt'.")
        elif escolha == '3':
            tabMeteo2 = carregaTabMeteo("meteorologia.txt")
            print("Tabela meteorológica carregada.")
            print(tabMeteo2)
        elif escolha == '4':
            print("Temperatura mínima:", minMin(tabMeteo1))
        elif escolha == '5':
            print(amplTerm(tabMeteo1))
        elif escolha == '6':
            print("Dia com precipitação máxima:", maxChuva(tabMeteo1))
        elif escolha == '7':
            limite = float(input("Digite o limite de precipitação: "))
            print(diasChuvosos(tabMeteo1, limite))
        elif escolha == '8':
            limite = float(input("Digite o limite de precipitação: "))
            print("Máximo de dias com precipitação abaixo do limite:", maxPeriodoCalor(tabMeteo1, limite))
        elif escolha == '9':
            grafTabMeteo(tabMeteo1)
        elif escolha == '0':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()