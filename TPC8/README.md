
TPC1:

a. Elementos não Comuns:
Esta função utiliza listas em compreensão para identificar elementos que estão presentes na lista1 mas não na lista2 e vice-versa. 

b. Palavras com Mais de Três Letras:
O texto é dividido em palavras e a lista é usada para filtrar apenas aquelas com mais de três letras. 

c. Enumerar Elementos de uma Lista:
Uma lista de tuplos é criada, onde cada tuplo contém um índice (inicinado em 1) e o respetivo elemento da lista.


TPC2: 

a. Contar Substrings
A função strCount conta quantas vezes uma substring aparece numa string. Aqui, a função utiliza o método count.

b. Produto dos Três Menores Números
A função produtoM3 ordena a lista e calcula o produto dos três menores números. 

c. Reduzir um Número
A função reduxInt continua a somar os dígitos de um número até que ele tenha apenas um dígito. 

d. Encontrar Índice de uma Substring
A função myIndexOf procura a primeira ocorrência de uma substring dentro de outra string e devolve o índice dessa ocorrência ou -1 se esta não for encontrada.


TPC3:

a. Contar Posts
Esta função tem o objetivo de contar quantos posts estão registados na rede social. Esta devolve o comprimento da lista redeSocial.

b. Listar Posts por Autor
A função postsAutor devolve todos os posts feitos por um autor específico. Para isso, percorremos a lista de posts e vamos juntando aqueles cujo autor corresponde ao fornecido. A função devolve uma lista com todos os posts desse autor.

c. Obter Lista de Autores
A função gera uma lista de todos os autores que contribuíram com posts na rede social, ordenada alfabeticamente. Utilizamos um conjunto para evitar repetições e, em seguida, convertemos para uma lista e ordenamos. 

d. Inserir Novo Post
Com a função insPost, podemos adicionar um novo post à rede social. A função determina automaticamente um novo ID para o post, baseado nos IDs existentes, e cria um dicionário com as informações fornecidas. O novo post é então adicionado à lista de posts.

e. Remover um Post
A função remPost permite remover um post específico da rede social, baseado no seu ID. Percorre a lista de posts e, ao encontrar o ID correspondente, remove o post da lista. 

f. Distribuição de Posts por Autor
A função postsPorAutor cria uma distribuição de posts agrupados por autor. Utilizamos um dicionário onde cada chave é um autor e o valor é uma lista de posts desse autor. 

g. Posts Comentados por um Autor
Por fim, a função comentadoPor devolve uma lista de posts que foram comentados por um autor específico. A função percorre todos os posts e os seus comentários, verificando se o autor está presente. Os posts nos quais o autor comentou são colecionados e retornados.

