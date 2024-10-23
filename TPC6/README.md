
O código apresentado é uma aplicação para gestão de alunos, permitindo aos utilizadores realizarem operações básicas como criar uma turma, inserir alunos, listar informações, consultar por ID e armazenar ou carregar dados de ficheiros. 

criar_turma(): 
Esta função cria uma nova turma, representada por uma lista vazia, que servirá como o armazenamento para os alunos inseridos.

inserir_aluno(turma): 
Esta função permite ao utilizador adicionar um novo aluno à turm, questionando sobre o nome, ID e notas do aluno. As notas são convertidas de strings para floats e são armazenadas num tuplo que é adicionado à lista da turma.

listar_turma(turma): 
Ao chamar esta função, o programa verifica se a turma está vazia. Se não estiver, ele itera sobre os alunos e imprime as suas informações, incluindo nome, ID e notas.

consultar_aluno(turma): 
Esta função permite ao utilizador procurar informações sobre um aluno em específico utilizando o seu ID. Se o aluno for encontrado, as suas informações são exibidas. Caso contrário, é informado de que o aluno não existe na turma.

guardar_turma(turma): 
Esta função é responsável por guardar os dados da turma num ficheiro. O utilizador deve fornecer o nome de um ficheiro e o nome de cada aluno é escrito numa linha separada, com as suas informações formatadas de maneira clara, utilizando vírgulas como delimitadores.

carregar_turma(): 
Ao usar esta função, o utilizador pode carregar os dados de uma turma a partir de um ficheiro. O programa lê o ficheir e processa cada uma das linhas para extrair as informações do aluno, armazenando-as na lista da turma. Se o ficheiro não for encontrado, o utilizador é informado.

Menu:
A aplicação apresenta um menu representado através da função menu(), que permite ao utilizador escolher a operação desejada. O loop continua até que este decida sair da aplicação. As opções disponíveis são: criar uma nova turma, inserir alunos, listar alunos, consultar por ID, guardar a turma num ficheiro e carregar uma turma de um ficheiro.


