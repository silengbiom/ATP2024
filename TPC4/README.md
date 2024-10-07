
Este programa premite a criação de uma aplicação que interage com o utilizador, permitindo que este manipule listas.O programa oferece várias funcionalidades como a criação de listas, cálculos da soma e média e verificação da ordenação das listas. Desta forma, a função menu() inicia um loop (resposta = True; while resposta:) que começa por dar as boas vindas ao utilizador, mostrando-lhe as opções disponíveis e pedindo-lhe para indicar a opção que deseja, atribuindo essa resposta a uma variável escolha, terminando apenas com a escolha da opção "0".

Escolhas:

(0) Sair
Se a opção escolhida for 0, é impressa a mensagem a indicar que o programa terminou, indicando a lista final (print("Obrigado por ter usado o nosso programa!"); print("Lista final:", lista)). É atribuído o valor False à variável resposta, fazendo o loop terminar, fechando o programa (resposta = False).

(1) Criar Lista com elementos aleatórios entre 1 e 100:
Se a opção escolhida for a 1, o programa começa por questionar o utilizador sobre o número de elementos que deseja ter na lista (n = int(input("Insira o número de elementos da lista:"))), atribuindo esse valor a uma variável n e de seguida preenche-a com números aleatórios entre 1 e 100 através do "import random" e o respetivo "random.randint(1,100)", atribuindo os valores aleatórios à variável num (lista.append(num)). No final, imprime a lista resultante (print("Lista criada:", lista)).

(2) Ler Lista:
Se a opção escolhida for a 2, o programa começa por questionar o utilizador sobre o número de elementos que deseja ter na lista atribuindo esse valor a uma variável nu (nu = int(input("Quantos números pretende inserir na lista?"))), e de seguida preenche-a com os respetivos elementos inseridos pelo utilizador que foram atribuídos à variável p (p = int(input("Insira o/os número/números:")); lista.append(p)), até se atingir o fim do ciclo determinado pelo numero de elementos que a lista terá (while i < nu:). Por fim, imprime a lista resultante (print("Lista criada:", lista)).

(3) Soma:
Se a opção escolhida for a 3, o programa calcula (soma = soma + i) e exibe a soma dos elementos (print("A soma dos elementos é:", soma)) da lista gerada anteriormente 
numa das opções (1) ou (2).

(4) Média:
Se a opção escolhida for a 4, o programa começa por verificar se a lista não está vazia (if len(lista) != 0:) e se esta não estiver calcula a soma dos elementos da lista 
gerada anteriormente (soma = soma + i) numa das opções (1) ou (2) e divide-a pelo número de elementos presentes nessa lista para obter a média (soma/len(lista)), gerando a mensagem com a média correspondente (print("A média dos elementos é:", media)). Se a lista estiver vazia, é mostrada uma mensagem indicando o mesmo (print("a lista está vazia!")).

(5) Maior:
Se a opção escolhida for 5, o programa começa por verificar se a lista não está vazia (if len(lista) != 0:) e se não estiver atribui o valor zero à variável maior (maior = 0) e de seguida compara-a com os elementos i presentes na lista gerados anteriormente (if i > maior:). Se algum dos elementos i for maior do que a variável maior, então o maior será esse i (maior = i), imprimindo de seguida uma mensagem indicando qual o maior elemento da lista (print("O maior elemento da lista é:", maior)).
Se a lista estiver vazia, é mostrada uma mensagem indicando o mesmo (print("a lista está vazia!")).

(6) Menor:
Se a opção escolhida for a 6, o programa começa por verificar se a lista não está vazia (if len(lista) != 0:) e se não estiver atribui à variável menor o primeiro elemento da lista (menor = lista[0]). De seguida compara essa variável com os elementos i da lista ( if i < menor:), e se houver algum menor do que a variável menor então esta passa a ser esse elemtno i (menor = i). No final imprime a menssagem indicando o menor elemento da lista (print("O menor elemento da lista é:", menor)). Se a lista estiver vazia, é mostrada uma mensagem indicando o mesmo (print("a lista está vazia!")).

(7) estaOrdenada por ordem crescente:
Se a a opção escolhida for a 7, o programa começa por atribuir a uma nova lista (lista1) a lista feita pelo utilizador, mas ordenada (lista1 = sorted(lista)). De seguida, verifica se a lista armazenada é igual à lista1 (if lista == lista1:), se esta for, indica a mensagem de que está ordenada de forma crescente (print("Sim, a lista está ordenada de forma crescente")), senão mostra a mensagem de que não está ordenada de forma crescente (print("Não, a lista não está ordenada de forma crescente")), através de uma condição.

(8) estaOrdenada por ordem decrescente:
Se a opção escolhida for a 8, o programa começa por atribuir a uma nova lista (lista2) a lista feita pelo utilizador ordenada de forma decrescente (lista2 = sorted(lista, reverse=True)). De seguida, verifica se a lista armazenada é igual à lista2 e se esta for, indica a mensagem de que está ordenada de forma decrescente (print("Sim, a lista está ordenada de forma decrescente")), senão mostra a mensagem de que não está ordenada de forma decrescente (print("Não, a lista não está ordenada de forma decrescente")), atarvés de uma condição.

(9) Procura um elemento:
Se a opção escolhida for a 9, o programa começa por perguntar qual o elemento que o utilizador pretende procurar na lista e atribui esse valor a uma variável elemento 
(elemento = int(input("Insira o elemento a procurar:"))). Se algum dos valores na lista for igual a esse valor (if elemento in lista:), é atribuído a uma variável numero o valor do índice desse elemento na lista (numero = lista.index(elemento)) e é impressa uma mensagem a indicar a posição deste na lista (print("O elemento está na posição:", numero)). Se não existir na lista mostra uma mensagem a indicar essa situação (print("-1, o elemento não pertence à lista")).

Por fim, se o utilizador não inserir nenhuma destas opções, o programa imprime uma mensagem indicando que a opção não é válida (print("A opção inserida é inválida! Tente novamente")) e o programa é iniciado através do comando menu().


