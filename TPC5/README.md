

O código presente no ficheiro python corresponde a uma aplicação para gestão de salas de cinema num centro comercial. Cada uma das salas é representada como um tuplo que contém a lotação máxima, uma lista dos lugares vendidos e o nome do filme que será exibido. Desta forma, o programa permite ao utilizador realizar diversas operações, como listar as salas disponíveis, verificar a disponibilidade de lugares, vender bilhetes ou adicionar e remover salas.

Função inserir_sala:
A função inserir_sala permite que o utilizador adicione uma nova sala à lista do cinema (cinema.append(sala)). Primeiro verifica se a sala já existe na lista (if sala not in cinema:). Se não existir adiciona (cinema.append(sala)), senão informa que essa sala já existe (print("A sala já existe no sistema!")). Após a adição, o programa informa o utilizador da ocorrência da operação (print("A sala foi adicionada com sucesso!")). 

Função remover_sala:
A função remover_sala permite remover uma sala existente na lista. Primeiro, verifica se a sala existe na lista (if sala in cinema:). Se existir, remove-a (cinema.remove(sala)) e infroma o utilizador (print("A sala foi removida com sucesso")), senão, informa o utilizador que a sala inserida não existe e não pode removê-la (print("A sala não foi encontrada")).

Função listar:
A função listar percorre a lista de salas usando um loop for com range(len(cinema)) (for i in range(len(cinema)):). Começa por atribuir o número da sala à variável sala (sala = cinema[i]) e depois imprime o número da sala, a lotação e o filme em exibição (print(f"Sala: {i + 1} | Lotação: {sala[0]} | Filme: {sala[2]}")). 

Função disponivel:
A função disponivel verifica se um lugar específico está disponível na sala de cinema com recurso a um ciclo for(for sala in cinema:). Começa por verificar se o filme dado como parametro existe na lista (if sala[2] == filme:), e se existir verifica se o lugar não está na lista (if lugar not in sala[1]:) e ,portanto, ocupado, retornando um valor booleano de verdadeiro quando está livre e falso quando está ocupado.

Função  vende_bilhete:
A função vende_bilhete processa a venda de um bilhete. Começa a percorrer a lista com recurso a um ciclo for (for sala in cinema:) e verifica que, se o filme dado como parâmetro for igual a um dos filmes disponíveis e o lugar não estiver na lista (if sala[2] == filme and lugar not in sala[1]:) e, portanto, ocupado, adiciona o lugar à lista de lugares ocupados (sala[1].append(lugar)). 

Função listar_disponibilidade:
A funçao listar_disponibilidades mostra quantos lugares estão disponíveis em cada sala. Ao percorrer as salas presentes na lista (for i in range(len(cinema)):), atribui à variável sala o valor de cada uma (sala = cinema[i]), calculando depois a diferença entre a lotação total e o número de lugares vendidos (disponiveis = sala[0] - len(sala[1])). Por fim, informa o utilizador da disponibilidade das salas (print(f"Sala {i + 1}: {disponiveis} lugares disponíveis")).

Função menu:
Esta é a função que permite imprimir o menu para o utilizador selecionar a opção pretendida.
É iniciado um ciclo que só termina quando a escolha do utilizador for "0", correspondendo à opção sair. Desta forma, dentro do ciclo pergunta ao utilizador a opção pertendida (escolha = int(input("\nEscolha uma opção: "))), atribuindo à variável escolha.
Se for a opção 1 chama a função listar.
Se for a opção 2 pergunta ao utilizador o nome do filme (filme = input("Nome do filme: ")) e o lugar (lugar = int(input("Número do lugar: "))), depois verifica se estão disponíveis através da função disponível (if disponivel(cinema, filme, lugar):) e se estiver imprime a mensagem print(f"Lugar {lugar} disponível."), senão imprime print(f"Lugar {lugar} não disponível.")
Se for a opção 3 pergunta ao utilizador o nome do filme (filme = input("Nome do filme: ")) e o lugar (lugar = int(input("Número do lugar: "))), depois verifica se estão disponiveis através da funcao vende_bilhete (if vende_bilhete(cinema, filme, lugar):) e se estiver disponível informa o utilizador da sua venda (print(f"Bilhete vendido para o Lugar {lugar}.")) ou da impossibilidade de concretizar a venda (print("Não foi possível vender o bilhete."))
Se for a opção 4 lista as salas, filmes e lugares disponíveis através da funçao listar_disponibilidades(cinema).
Se for a opção 5, pergunta ao utilizador o número de lugares da nova sala (nlugares = int(input("Lotação da sala: "))). Depois, pergunta o nome do filme (filme = input("Nome do filme: ")) e cria uma nova lista sala com esses 3 dados (sala = [nlugares, vendidos, filme]), inserindo-a na lista do cinema com recurso à função inserir_sala(inserir_sala(cinema, sala)).
Se for a opção 6, pergunta ao utilizador o número da sala a ser removida (numero_sala = int(input("Número da sala a ser removida: ")) - 1) e se estiver entre 0 e len(sala) (if 0 <= numero_sala < len(cinema):), remove-a (remover_sala(cinema, cinema[numero_sala])):, senão infroma que a sala não existe na lista (print("Sala não encontrada")).
Se for a opção 0 imprime a mensagem de que saiu do programa (print("Saindo do programa."))
Se não escolher nenhuma destas opções informa de que a opção inserida não é válida (print("Opção inválida. Por favor, escolha uma opção válida.")).
