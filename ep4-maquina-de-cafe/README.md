Máquina de Café
=========

O café (e obviamente a máquina) é um item essencial para o profissional de TI. Desta forma, implemente um programa que provê uma interface com uma máquina de café com certa variedade de bebidas.

O que verei neste EP?
-----------

- Uso de classes **concretas** e **abstratas** por meio do modulo [ABC](https://docs.python.org/2/library/abc.html).
- Herança de classes com sobrescrita de métodos e atributos.
- Organização do código em módulos (scripts *.py*).
- Uso de testes unitários por meio do módulo [unittest](https://docs.python.org/2/library/unittest.html).
- Manipulação de dicionários ([dictionaries](https://docs.python.org/2/tutorial/datastructures.html?highlight=dictionary#dictionaries)).

Especificação
----------

### Funcionalidades

O programa deve permitir:

- Entrada de valores (**moedas** e/ou **cédulas** de **REAL**) e apresentar na tela quanto o usuário possui de crédito.
- Escolha de uma bebida e a devolução do troco do usuário (caso exista).
- Devolução do valor no caso de desistência da compra.

#### Interface com o usuário

Ao rodar o programa, deve-se apresentar opções para a escolha da ação desejada, sendo elas: **adicionar valor**, **devolver valor** e **retirar bebida**.

- **Adicionar valor**: Apresentar para o usuário uma lista com as opções de valores predefinidas, respeitando as cédulas e moedas disponíveis na moeda **REAL** e especificadas a seguir neste documento.
- **Devolver valor**: A máquina deve devolver todo o valor inserido pelo usuário até o momento, seria a desistência da compra.
- **Retirar bebida**: Apresentar uma lista com as bebidas disponíveis na máquina. O usuário então seleciona a bebida desejada dentre as disponíveis, a máquina produz a bebida e devolve o troco, caso exista, ao usuário.


#### Valores que podem ser aceitos na adição de valores

1. **Cédulas** de 1, 2 e 5 Reais. *Acima desses valores problemas de troco são muito prováveis*.
2. **Moedas** de 1, 5, 10, 25, 50 e 1 Real.

#### Bebidas que devem estar disponíveis

1. Café espresso curto. R$ 0,00
2. Café espresso longo. R$ 0,00
3. Café com leite.  **R$ 0,60**
4. Cappuccino. **R$ 0,60**
5. Mocaccino. **R$ 0,60**
6. Chocolate. **R$ 0,60**
7. Chocoleite. **R$ 0,60**
8. Leite. **R$ 0,60**
9. Chá. R$ 0,00
10. Água quente. **R$ 0,25**

*Nota: a palavra **Espresso** (com "s") é devido à origem italiana deste tipo de café (e dá maquina usada como referência para este documento) e que aqui [no Brasil] é traduzido como **Expresso** (com "x"). [Referềncia](http://veja.abril.com.br/blog/sobre-palavras/consultorio/o-cafe-e-expresso-ou-espresso/)*

#### Outras restrições

- Não possibilitar a retirada de uma bebida caso o usuário não tenha atingido o valor necessário.

Implementação
-----------

### Diretrizes básicas

O programa deve seguir algumas diretrizes para a sua implementação, seguem abaixo.

- Criar um **diretório** na base do EP com o **seu nome** para inclusão dos arquivos *.py*. Como este EP tende a ter mais de um arquivo, essa organização se mostra necessária.
- Utilizar **testes unitários** (vide seção **Links úteis**) com considerável cobertura (ao menos **60%** do código).
- Desenvolver um script principal chamado **coffe_machine.py** que é responsável pela execução do programa e manipulação das classes e seus módulos (vide seção **Links úteis**).

### Classes e relacionamentos

O programa deve ser conter em sua implementação as classes a seguir.

#### Bebida

Classe **abstrata** (vide seção **Links úteis**) representando a entidade **Bebida** com o comportamento padrão de uma bebida.

##### Atributos

- Nome: nome da bebida. Ex: *Cappuccino*.
- Valor: valor da bebida. Ex: 0.60

*Recomendação: veja sobre **abstractproperty** no link da seção **Links úteis** sobre classes abstratas para implementação dos atributos abstratos da classe.*

#### Subclasses de Bebida

Desenvolver subclasses de bebida sobrescrevendo seus nomes e valores para cada bebida. Ex.: A classe **CafeExpressoCurtoBebida** é subclasse de **Bebida** e implementa os atributos *nome* e *valor* com, respectivamente, "Café expresso curto" e "0.00".

#### Calculadora de troco

Calcula o troco do usuário.

Ex.: Valor de R$ 0.60, o usuário inseriu R$ 1.00, o troco poderá ser 1 moeda de 0.25, 1 moeda de 0.05 e 1 moeda de 0.10.

##### Atributos

- **Valores disponíveis**: Lista Cédulas/Moedas disponíveis (apenas os valores, sem gerenciamento de quantidades).

##### Métodos

- **Calcula troco**: Recebe o valor total e o informado pelo usuário e retorna um dicionário com as cédulas e suas quantidades calculadas para troco.

#### Máquina de café

Classe que prove a interface principal da máquina de café. Essa classe deve receber uma instância da **Calculadora de troco** e uma lista com as **Bebidas** disponíveis.

##### Atributos

- **Bebidas**: Lista de bebidas que a máquina tem disponível para o usuário.
- **Calculadora de troco**: Instância da calculadora de troco.

##### Métodos

- ***Construtor***: Recebe uma **lista de classes bebidas** que estão disponíveis e uma instância da **calculadora de troco**.
- **Adiciona valor**: Inclusão do valor adicionado pelo usuário. Deve receber uma cédula ou moeda válida no **REAL**.
- **Retirar bebida**: Faz a retirada da bebida, deve receber via parâmetro a instância da bebida desejada.
- **Obter troco**: Devolve o valor do troco do usuário.
- **Devolver valor (desistência da compra)**: Devolve o valor que o usuário possui de crédito.

Links úteis
-----------

- https://docs.python.org/2/tutorial/classes.html
- https://docs.python.org/2/tutorial/modules.html
- https://docs.python.org/2/library/abc.html
- https://docs.python.org/2/library/unittest.html