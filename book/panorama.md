# Panorama Atual da Computação Quântica

```{note}
Material extraído do TCC [*Computação Quântica: Uma abordagem para estudantes de graduação em Ciências Exatas*](./tcc-giovani.pdf), de Giovani Goraiebe Pollachini.
```

## Breve histórico 

No início do século XX, a Física Clássica enfrentava dificuldades em descrever alguns fenômenos observados à época, como, por exemplo, o espectro de radiação de corpo negro ou o efeito fotoelétrico. Essa crise culminou na criação da Mecânica Quântica, que se consolidou por volta da década de 1920, e tem sido aplicada com sucesso em diversos fenômenos.

O desenvolvimento tecnológico na década de 1970 permitiu o controle de sistemas quânticos individuais permitindo-se aprisionar átomos individuais em armadilhas (traps), isolando-os do restante do ambiente, e medindo seus diversos aspectos com precisão notável. Nesse contexto, passou-se a considerar a possibilidade de se usar sistemas quânticos para realizar processamento e transmissão de informação, fazendo uso de fundamentos da Mecânica Quântica, como superposição e emaranhamento. Esses sistemas guardam analogia com os bits clássicos, e são chamados de qubits. (\!\!\cite{book:qcqi_nc} p.3-4).

O físico R. Feynman, na década de 1980, sugeriu o uso de computadores quânticos para simular sistemas quânticos. E em 1994, o matemático P. Shor propôs um algoritmo quântico capaz de resolver o problema de fatoração de números em fatores primos de forma mais eficiente que os algoritmos clássicos conhecidos. Há uma expectativa de que um tal algoritmo possa ameaçar alguns protocolos de criptografia, como o RSA, usado largamente na atualidade. O cientista da computação Lov Grover também elaborou um algoritmo quântico de busca em uma base de dados não estruturada, que possui ganho quadrático de desempenho em comparação ao melhor algoritmo clássico conhecido. (\!\! \cite{book:pqci_benenti}, p.3).

 Atualmente, a Computação Quântica e a Informação Quântica estão se consolidam como áreas de pesquisa com desenvolvimento acelerado nas últimas décadas. Empresas de tecnologia como IBM, Google, Intel e Microsoft têm projetos e pesquisas nessa área, e diversas Startups têm surgido nesse contexto. 

## Motivação para Computação Quântica

A lei de Moore, formulada em 1965, previu que a capacidade computacional dos sistemas digitais dobraria a cada dois
anos. Surpreendentemente, os avanços computacionais se mantiveram aproximadamente nesse ritmo até a atualidade. No entanto, à medida que a escala dos transistores se reduz, aproxima-se de limites físicos fundamentais, e aparentemente insuperáveis. Os efeitos quânticos, em alguns aspectos indesejáveis,
passam a interferir intensamente no funcionamento ideal do transistor. Para que o ritmo ditado pela lei de Moore continue, tem-se
apostado, entre outras abordagens, na Computação Quântica.

Outro ponto refere-se ao consumo de energia. O princípio
de Landauer afirma que para cada bit de informação apagado,
dissipa-se no ambiente a energia correspondente a pelo menos. Pelas características da Mecânica Quântica, as portas
lógicas quânticas precisam ser reversíveis. Isso corresponderia,
em princípio, à não necessidade de se apagar informação e à
possibilidade de se ter um computador que não dissipa energia
no processamento.

Um terceiro ponto motivador das pesquisas em Computação Quântica é que a investigação nessa área pode elucidar aspectos da Mecânica Quântica, frequentemente contra intuitivos
em relação à Física Clássica, ou mesmo, apontar fenômenos
ainda não explorados.

Por fim, a Computação Quântica apresenta desafios em
diversas áreas, com manipulação de sistemas quânticos, novas
técnicas experimentais, desenvolvimento de algoritmos, teoria da
informação, entre outros, o que torna a área multidisciplinar.

```{note}
A Computação Quântica é uma tecnologia ainda em estágio inicial, e tem se mostrado uma área de pesquisa estratégica no cenário internacional. 
Neste capítulo, faz-se um breve estudo das expectativas de mercado em relação à Computação Quântica, em grande parte baseado na Gartner, uma consultoria em Tecnologia da Informação \cite{webinar:gartner}. Apresenta-se também algumas das principais empresas com pesquisas em Computação Quântica, e mostra-se um resumo dos desenvolvimentos realizados nessas empresas tanto em hardware como em software.
```

## Expectativas de mercado

A Gartner estima que a Computação Quântica será uma realidade no mercado dentro de 5 a 10 anos. Espera-se que essa tecnologia se torne mais rápida e escalável, de forma a tratar problemas reais que a computação atual não conseguiria abordar satisfatoriamente. A curva da figura \ref{cap6:fig_hype_cicle}, chamada \emph{hype-cicle}, mostra as tecnologias em alta no mercado e as que já atingiram maturidade. A posição da Computação Quântica é de subida na curva de expectativas. 

![hype_cicle_gartner](https://github.com/user-attachments/assets/c8e76d63-a52d-441f-8c32-2f3c6fadd072)

Há uma percepção no mercado que a Computação Quântica gere uma disrupção algo similar às ocorridas na Revoluções Industrial, Tecnológica e Digital. O panorama atual da Computação Quântica é comparável, nessa percepção, ao computador ENIAC da decada de 1950 (para comparar, ver figura \ref{cap6:fig_eniac}). À época, não havia como prever o desenvolvimento tecnológico subsequente, e a capacidade de processamento que se conseguiria obter nas décadas seguintes. 

![eniac](https://github.com/user-attachments/assets/53f10d93-0118-4b7d-a724-d81affdaadf4)

 A expectativa é que um modelo híbrido entre Computação Clássica e Quântica seja a tecnologia emergente no cenário atual. A computação seria realizada em um processador quântico para problemas nos quais há vantagens no uso da Computação Quântica, como espera-se que ocorra com os problemas chamados NP-difíceis. 
 
 Dentre as principais aplicações previstas para a Computação Quântica, destaca-se resolução de problemas de otimização, machine learning, desenvolvimento de novos materiais, fármacos e processos químicos. Outra aplicação de destaque é em criptografia. A figura \ref{cap6:fig_aplic_cq_1} 

 mostra aplicações em que se espera utilizar processamento quântico.

![qc_applications](https://github.com/user-attachments/assets/c06c9038-afe8-4c84-a9fe-cbed87688c07)

![qc_applications_2](https://github.com/user-attachments/assets/748eed13-633c-4e7c-ae29-ca30f1ad3517)

O impacto da Computação Quântica em sistemas de segurança é considerado certo dentro de poucos anos. Algumas tecnologias atuais como a \emph{criptografia RSA} e o \emph{blockchain} (do qual o \emph{bitcoin} faz uso, em particular) seriam vulneráveis à Computação Quântica. Há demanda por protocolos de criptografia que levem em conta a existência da Computação Quântica, isto é, por criptografia \emph{pós-quântica} (\emph{post-quantum}/\emph{quantum-safe}/\emph{quantum-proof cryptography}). 

## Empresas e Desenvolvimentos Atuais

A Computação Quântica encontra-se em um estágio de desenvolvimento acelerado. Empresas como IBM, Google, Intel e Microsoft, e Startups como Rigetti, têm pesquisas para desenvolvimento de processadores quânticos. Algumas dessas empresas, como a IBM e Rigetti, disponibilizam protótipos de computadores quânticos para acesso pela nuvem ao público. Também há desenvolvimento de simuladores, linguagens de programação para Computação Quântica e kits de softwares por essas empresas. Alguns comentários são desenvolvidos no que segue.

### IBM 

A IBM utiliza tecnologia de qubits supercondutores, compostos por junções de Josephson. Em 10 de novembro de 2017, foram anunciados protótipos de 50 e de 20 qubits, em uma iniciativa de tornar a computação quântica comercialmente disponível em um futuro próximo. 
   
No projeto IBM Quantum Experience, um computador quântico de 5 qubits está disponível para uso através da nuvem. A programação é feita por uma interface gráfica, que permite realizar simulação e/ou enviar o algoritmo para execução no computador quântico. A programação pode ser realizada em modo texto, com a linguagem OpenQASM (Open Quantum Assembly Language). Em relação à simulação, a IBM também colabora no projeto open source QISKit (Quantum Information Software Kit), uma biblioteca python para Computação e Informação Quântica que funciona em conjunto com OpenQASM.

### Google 

O processador quântico Bristlecone, de 72 qubits, foi apresentado em 5 de março de 2018. A tecnologia de qubits da Google é baseada em filmes supercondutores de alumínio em substrato de safira. Para simulação de computadores quânticos, a empresa tem um projeto open source chamado Quantum Playground, em que é possível simular um computador quântico de até 22 qubtis. 

### Intel 

Em 8 de janeiro de 2018 foi anunciado pela Intel a fabricação de um processador quântico, em fase de teste, de 49 qubits supercondutores. A tecnologia utilizada atualmente para realizar os qubits são as junções de Josephson, consistindo em uma camada fina de óxido entre dois fios de alumínio.
A Intel também pesquisa qubits de spin em silício.

### Microsoft

A Microsoft vem empregando esforços na elaboração de qubits topológicos por meio de férmions de Majorana. Além disso, foi lançado em 11 de dezembro de 2017 o Microsoft Quantum Development Kit, contendo a linguagem de programação Q\# dedicada para Computação Quântica, e acompanhada de simuladores.

### Riggeti

A Startup Rigetti disponibiliza um processador quântico de 19 qubits e um ambiente de desenvolvimento, chamado Forest, para programação quântica. A empresa também disponibiliza um simulador, chamado Quantum Virtual Machine, de 26 qubits. A Rigetti também desenvolveu a linguagem open source Quil, que baseia-se em um modelo computacional clássico/quântico com memória compartilhada, e trabalha em uma biblioteca python para programação quântica, a pyQuil.

### Outras Startups e Empresas

![early_pioneers_in_qc](https://github.com/user-attachments/assets/a1507703-32c5-45c2-b183-34e03801e920)

### Outras empresas 

Empresas como Baidu e Alibaba entraram no cenário da Computação Quântica. Em 23 de fevereiro de 2018, a empresa Alibaba lança um serviço de computação quântica na nuvem com 11 qubits. Em 8 de março de 2018, a Baidu, que domina o mercado chinês de mecanismos de busca na internet, anuncia o Instituto de Computação Quântica Baidu.

## Comentários

comentar que a computação quântica ainda está na fase de protótipos 
 
 erros nos qubits e nas portas ainda é alto
 
 é necessário utilizar códigos corretores de erros
 
 qubits lógicos: conjunto de qubits físicos, o que significa que a quantidade de qubits na prática será menor que a informada pelas empresas
