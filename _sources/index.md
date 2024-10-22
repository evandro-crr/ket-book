# Introdução à Computação Quântica

Este é um material didático auxiliar para a disciplina FSC7152 – Computação Quântica da UFSC, que tem como objetivo estabelecer uma ponte entre os conceitos teóricos vistos em sala de aula e a prática da programação quântica utilizando a [plataforma Ket](https://quantumket.org).

Parte deste material é adaptada das notas de aula do Prof. Dr. Eduardo Inácio Duzzioni e do TCC de Giovani Goraiebe Pollachini.

# Panorama Atual da Computação Quântica

```{note}
Material extraído do TCC [*Computação Quântica: Uma abordagem para estudantes de graduação em Ciências Exatas*](./tcc-giovani.pdf), de Giovani Goraiebe Pollachini.
```

## Breve histórico 

No início do século XX, a Física Clássica enfrentava dificuldades em descrever alguns fenômenos observados à época, como, por exemplo, o espectro de radiação de corpo negro ou o efeito fotoelétrico. Essa crise culminou na criação da Mecânica Quântica, que se consolidou por volta da década de 1920, e tem sido aplicada com sucesso em diversos fenômenos.

O desenvolvimento tecnológico na década de 1970 permitiu o controle de sistemas quânticos individuais permitindo-se aprisionar átomos individuais em armadilhas (traps), isolando-os do restante do ambiente, e medindo seus diversos aspectos com precisão notável. Nesse contexto, passou-se a considerar a possibilidade de se usar sistemas quânticos para realizar processamento e transmissão de informação, fazendo uso de fundamentos da Mecânica Quântica, como superposição e emaranhamento. Esses sistemas guardam analogia com os bits clássicos, e são chamados de qubits.

O físico R. Feynman, na década de 1980, sugeriu o uso de computadores quânticos para simular sistemas quânticos. E em 1994, o matemático P. Shor propôs um algoritmo quântico capaz de resolver o problema de fatoração de números em fatores primos de forma mais eficiente que os algoritmos clássicos conhecidos. Há uma expectativa de que um tal algoritmo possa ameaçar alguns protocolos de criptografia, como o RSA, usado largamente na atualidade. O cientista da computação Lov Grover também elaborou um algoritmo quântico de busca em uma base de dados não estruturada, que possui ganho quadrático de desempenho em comparação ao melhor algoritmo clássico conhecido.

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
Neste capítulo, faz-se um breve estudo das expectativas de mercado em relação à Computação Quântica, em grande parte baseado na Gartner, uma consultoria em Tecnologia da Informação. Apresenta-se também algumas das principais empresas com pesquisas em Computação Quântica, e mostra-se um resumo dos desenvolvimentos realizados nessas empresas tanto em hardware como em software.
```

## Site Interativo

Todo código presente neste site pode ser executado diretamente na própria página ou carregado para ambientes interativos como o Google Colab ou o Binder. Isso permite que você experimente e modifique os exemplos de código para entender melhor os conceitos apresentados.

Ativar a execução dos exemplos de código é fundamental para uma experiência de aprendizado mais interativa e prática. Isso permite que você teste as implementações apresentadas, experimente diferentes parâmetros e explore o comportamento das operações quânticas em tempo real.

Para ativar a execução de código no site, basta clicar na opção <i class="fas fa-rocket"></i> **Live Code** presente na barra superior direita da página (quando disponível). Isso iniciará a execução do código e você poderá ver o resultado diretamente na página. Além disso, você também pode clicar nos botões <i class="fas fa-rocket"></i> **Colab** ou <i class="fas fa-rocket"></i> **Binder** para carregar o código em um ambiente interativo externo, onde poderá executá-lo, modificá-lo e salvar o resultado conforme desejado.

Essa abordagem oferece uma maneira prática e didática de explorar os conceitos de computação quântica, permitindo que você experimente ativamente e desenvolva sua compreensão por meio da prática e da experimentação direta.

## Conteúdo

```{tableofcontents}
```
