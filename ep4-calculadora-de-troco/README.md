Calculadora de Troco
=========

Implementar um programa onde dada uma quantia inicial e o valor recebido seja retornada a quantidade de troco correspondente à diferença do valor respeitando as cédulas e moedas do **REAL**. Retornar sempre a maior quantidade da cédula de maior valor para atender ao troco.

O que verei neste EP?
-----------

- Uso de classes.
- Organização do código em módulos (scripts *.py*).
- Uso de testes unitários com o módulo [unittest](https://docs.python.org/2/library/unittest.html).
- Manipulação de dicionários ([dictionaries](https://docs.python.org/2/tutorial/datastructures.html?highlight=dictionary#dictionaries)).

Especificação
----------

### Termos usados

- **Valor inicial**: Valor total (de uma compra, por exemplo).
- **Valor recebido**: Valor recebido (dado pelo usuário ao caixa, por exemplo).

### Funcionalidades

O programa deve permitir:

- Entrada do valor inicial.
- Entrada do valor recebido (superior ao **valor inicial**).
- Saída de uma quantia de troco.

#### Interface com o usuário

- Ao rodar o programa, deve-se perguntar ao usuário o valor inicial, o valor recebido e em seguida mostrar o resultado, ex.:

```
>>> Entre com o valor inicial:
55.60
>>> Entre com o valor recebido:
60.00

Resultado:
2 cédulas de 2 reais.
1 moeda de 25 centavos.
1 moeda de 10 centavos.
1 moeda de 5 centavos
```


#### Cédulas e moedas que devem ser utilizadas.

Utilizar as cédulas e moedas presentes no **REAL**.

1. **Cédulas** de 1, 2, 5, 10, 20, 50 e 100 Reais.
2. **Moedas** de 1, 5, 10, 25, 50 e 1 Real.

#### Outras restrições

- Acusar erro caso o **valor recebido** seja inferior ao **valor inicial**.

Implementação
-----------

### Diretrizes básicas

O programa deve seguir algumas diretrizes para a sua implementação, são elas:

- Criar um **diretório** na base do EP com o **seu nome** para inclusão dos arquivos *.py*. Como este EP tende a ter mais de um arquivo, essa organização se mostra necessária.
- Utilizar **testes unitários** (vide seção **Links úteis**) com considerável cobertura (ao menos **60%** do código).

#### Arquivos

- Desenvolver um arquivo chamado **core.py** que deve conter a classe **CalculadoraDeTroco** (especificada a seguir) e todo o código necessário.
- Desenvolver um arquivo chamado **tests.py** contendo os testes unitários das classes da aplicação (vide seção **Links úteis** neste documento para mais informações).
- Desenvolver um script principal chamado **maquina_de_troco.py** que é responsável pela execução do programa e manipulação das classes e seus módulos (vide seção **Links úteis**).

### Classes

O programa deve ser conter em sua implementação a classe a seguir:

#### Calculadora de troco

Responsável pelo calculo do troco do usuário.

##### Atributos

- **Valores disponíveis**: Lista com as cédulas e moedas disponíveis (apenas os valores, sem gerenciamento de quantidades).

##### Métodos

- **_Construtor_**: Recebe um dicionário com as cédulas disponíveis para uso no cálculo.
- **Calcula troco**: Recebe o **valor inicial** e o **valor recebido** e retorna um **dicionário com as cédulas** e suas quantidades calculadas para troco.

Links úteis
-----------

- https://docs.python.org/2/tutorial/classes.html
- https://docs.python.org/2/tutorial/modules.html
- https://docs.python.org/2/library/unittest.html
