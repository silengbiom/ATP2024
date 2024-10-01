
Este código implementa um jogo denominado por "O jogo dos 21 fósforos". Este jogo consite em retirar fósforos (entre 1 e 4) a partir de um número inicial (21), tendo como principal objetivo não tirar o último fósforo, sob risco de se perder.

O jogo apresenta dois modos para ser jogado, representado através de duas funções distintas no código (def jogar1() corresponde ao modo 1 e def jogar2() corresponde ao modo 2):
O jogo inicia perguntando ao jogador qual dos modos deseja jogar (escolha = int(input("Escolha o modo 1 ou 2 para jogar: (1- O jogador joga primeiro; 2- O computador joga primeiro)"))
if escolha == 1:
    resultado = jogar1()
else:
    resultado = jogar2())

Modo 1: O jogador joga primeiro e o computador ganha sempre:
O jogo começa com 21 fósforos (numero_fosforos = 21) e enquanto o número de fósforos for maior que 0 (while numero_fosforos > 0) o jogo irá alternando entre o computador e o jogador, iniciando com a jogada do jogador. Desta forma, é pedido ao jogador para inserir o número de fósforos que pretende tirar, entre 1 e 4 (n = int(input("Retire entre 1 e 4 fósforos."))), atribuindo esse valor a n. De seguida, é determinado que, quando o valor de n for inferior a 0, superior a 4 ou superior ao numero-fosforos (while n < 1 or n > 4 or n > numero_fosforos), aparece uma mensagem ao jogador a dizer que a opção escolhida é inválida (print("Opção inválida. Tente novamente)) pedindo novamente ao jogador para este inserir outro número atribuindo-o novamente à variável n. Ao longo das jogadas vai sendo retirado o valor de n ao número inicial de fosforos (numero_fosforos = numero_fosforos - n) e vai sendo anunciado o número de fósforos retirados e quantos fósforos ficaram disponíveis (print ("O jogador tirou",n,"fosforos e sobraram",numero_fosforos), print ("O computador tirou",y,"fosforo e sobraram",numero_fosforos)).Por fim, é verificado se o jogador retira o último fósforo e se isso acontecer, o computador ganha (if numero_fosforos == 0: jogador = "jogador"; if resultado == "jogador":
    print("Tu Perdeste!!")
else:
    print("O computador perdeu!!")).
A quantidade de fósforos retirados pelo computador é determinada de forma a garantir que ele tenta forçar o jogador a perder, baseando-se na quantidade de fósforos restantes (if(numero_fosforos - 1) % 5 == 0: y = random.randint(1,4)
else:
y = (numero_fosforos - 1) % 5
numero_fosforos = numero_fosforos - y)).

Modo 2: O computador joga primeiro
Neste modo, o computador pode ganhar quando o jogador cometer um erro de cálculo.
O jogo começa com 21 fósforos (numero_fosforos = 21) e enquanto o número de fósforos for maior que 0 (while numero_fosforos > 0) o jogo irá alternando entre o computador e o jogador, iniciando com o computador. Desta forma, o computador joga primeiro (y = random.randint(1,4)), tendo em conta que o número escolhido pelo computador não pode ser superior ao numero de fosforos naquele momento (if y > numero_fosforos: y = numero_fosforos), uma vez que a cada jogada o numero de fosforos vai diminuindo (numero_fosforos = numero_fosforos - y; numero_fosforos = numero_fosforos - n), anunciando a cada jogada o numero de fosforos restantes (print ("O computador tirou",y,"fosforos e sobraram",numero_fosforos); print ("O jogador tirou",n,"fosforos e sobraram",numero_fosforos)). Após a jogada do computador, é a vez do jogador, aparecendo a mensagem a questionar o jogador sobre o número de fósforos que pretende retirar (n = int(input("Introduz um número entre 1 e 4:"))), avaliando se a opção é válida (while n < 1 or n > 4 or n > numero_fosforos) e caso não seja, imprime a mensagem diznedo que a opção é inválida (print ("Opção inválida. Tente novamente:")) questionando novamente o jogador sobre o número de fósforos para retirar. No final do jogo é avaliado quem tira o último fósforo e perde (if numero_fosforos == 0: jogador = "jogador"; if numero_fosforos == 0: jogador = "computador") aparecendo a mensagem de quem perdeu e quem ganhou (if resultado == "jogador":
    print("Tu Perdeste!!")
else:
    print("O computador perdeu!!")).

