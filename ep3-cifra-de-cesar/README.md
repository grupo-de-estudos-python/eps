EP 3 - Cifra de Cesar
=======

A *Cifra de Cesar* é uma das primeiras e mais simples técnicas de criptografia. Consiste basicamente na troca de letras com um alfabeto base e um de referência para troca (chave). O nome é uma homenagem ao imperador Julio Cesar que usou para comunicação com seus generais em 50 A.C.

Exemplo:

	Alfabeto base:               A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
	Alfabeto para troca (chave): U V W X Y Z A B C D E F G H I J K L M N O P Q R S T

*Note que o alfabeto para substituição simplesmente teve as letras deslocadas para a direita.*

Texto para codificar: GRUPO DE ESTUDOS PYTHON
Resultado             ALOJI XY YMNOXIM JSNBIH

No exemplo acima, para a letra "G" por exemplo, buscamos a letra correspondente no alfabeto para troca, no caso "A".

Instruções
------

- Criar um arquivo na raiz do diretório do exercício com o seu nome.
- Criar duas funções, uma para codificar e outra para decodificar.
- Receber via linha de comando a ação desejada (codificar/decodificar).

Especificação
------

- Desenvolver um programa que codifique e decodifique usando a **Cifra de Cesar**.
- O programa deve guardar internamente o alfabeto de substituição (chave).
- O usuário informará como parâmetro na execução do programa a ação desejada (criptografar/descriptografar).
- O programa deve diferenciar letras maiúsculas e minúsculas.
- Números também devem ser codificados.

Exemplo
-------

Para codificar:

	$ python alisson.py -c
	Entre com o texto para criptografia: Alisson 1990
	Resultado: Ufcmmkh 4226

Para decodificar:

	$ python alisson.py -d
	Entre com o texto para descriptografia: Ufcmmkh 4226
	Resultado: Alisson 1990


Links úteis
-------

https://docs.python.org/2/library/sys.html#sys.argv
https://docs.python.org/2/library/string.html
http://pt.wikipedia.org/wiki/Cifra_de_C%C3%A9sar
https://pt.khanacademy.org/computing/computer-science/cryptography/crypt/v/caesar-cipher


Referências
------

https://pt.khanacademy.org/computing/computer-science/cryptography/crypt/v/caesar-cipher