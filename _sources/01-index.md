# Bem-vindo ao Aprenda Ket

Este é um material didático produzido por membros do Grupo de Computação Quântica da UFSC, com o objetivo de disseminar o ensino e promover a acessibilidade na área de computação quântica.

Desenvolvido para estabelecer uma ponte entre os conceitos teóricos fundamentais e a prática da programação quântica utilizando a [plataforma Ket](https://quantumket.org), este material foi testado e validado como recurso auxiliar na disciplina FSC7152 – Computação Quântica da UFSC, mas também foi estruturado para servir como um guia de aprendizado independente para qualquer pessoa interessada em ingressar neste campo, independente de seus conhecimentos prévios.

Parte deste conteúdo é adaptada das notas de aula do Prof. Dr. Eduardo Inácio Duzzioni e do TCC de Giovani Goraiebe Pollachini, incorporando anos de experiência docente e de pesquisa em computação quântica. Demais material utilizados estão devidamente citados em seus momentos de uso e nas referências.

## O que é a Computação Quântica

A Computação Quântica é um paradigma revolucionário de processamento de informação que utiliza os princípios fundamentais da Mecânica Quântica para realizar operações computacionais. Ao procurar por novas perspectivas para o processamento de dados, ela se apresenta não como uma evolução incremental, mas como uma transformação radical, capaz de redefinir os limites do que é computacionalmente possível.

Esta abordagem permite encontrar soluções para desafios computacionais que eram considerados impossíveis para os computadores atuais, abrindo portas para descobertas em diversas áreas.

## Fundamentos Quânticos

Diferente dos computadores clássicos que utilizam bits (unidade que podem ou ser 0 ou ser 1), os computadores quânticos utilizam qubits (bits quânticos), que podem existir em superposição de estados, representando simultaneamente 0 e 1. 

Esta capacidade de superposição, combinada com outros fenômenos quânticos como emaranhamento e interferência, permite que computadores quânticos resolvam certos tipos de problemas de forma exponencialmente mais rápida que os computadores clássicos. Problemas complexos em áreas como criptografia, otimização, simulação de materiais e machine learning podem ser abordados de maneira completamente nova através da computação quântica.

## Propósito e Aplicações

A computação quântica não visa substituir os computadores clássicos, mas sim complementá-los, criando uma nova classe de dispositivos capazes de resolver problemas que são intratáveis mesmo para os supercomputadores mais poderosos da atualidade.

## Site Interativo

Todo código presente neste site pode ser executado diretamente na própria página ou carregado para ambientes interativos como o Google Colab ou o Binder. Isso permite que você experimente e modifique os exemplos de código para entender melhor os conceitos apresentados.

Ativar a execução dos exemplos de código é fundamental para uma experiência de aprendizado mais interativa e prática. Isso permite que você teste as implementações apresentadas, experimente diferentes parâmetros e explore o comportamento das operações quânticas em tempo real.

Para ativar a execução de código no site, basta clicar na opção <i class="fas fa-rocket"></i> **Live Code** presente na barra superior direita da página (quando disponível). Isso iniciará a execução do código e você poderá ver o resultado diretamente na página. Além disso, você também pode clicar nos botões <i class="fas fa-rocket"></i> **Colab** ou <i class="fas fa-rocket"></i> **Binder** para carregar o código em um ambiente interativo externo, onde poderá executá-lo, modificá-lo e salvar o resultado conforme desejado.

Essa abordagem oferece uma maneira prática e didática de explorar os conceitos de computação quântica, permitindo que você experimente ativamente e desenvolva sua compreensão por meio da prática e da experimentação direta.

## Entendendo o Material

Esse material cobrirá todos os conteúdos necessários para o pleno entendimento da computação quântica, ele é dividido em três sessões principais, com cada uma contendo subsessões de tópicos necessários no estudo da matería.

- **Pré-requisitos**: Os pré-requisitos da computação quântica contém uma base de conhecimentos que serão de suma importância ao se aprofundar em tópicos mais complexos, nele possuímos:
    - [Tutorial de Python](02-pytutorial.ipynb) : A linguagem de programação Python, que, mais tarde, será utilizada para o entendimento da plataforma de programação quântica Ket.
    - [Números Complexos](03-complexos.md) : Fundamentos matemáticos essenciais para representar estados quânticos e operações.
    - [Algebra Linear](04-algebra.md) : Base matemática para compreender espaços vetoriais, operadores e transformações na computação quântica.
    - [Postulados da Mecânica Quântica](05-postulados.ipynb) : Princípios fundamentais que regem o comportamento dos sistemas quânticos.
    - [Computação Clássica](06-computacao_classica.md) : Conceitos básicos de computação tradicional para contrastar com o paradigma quântico.

- **Fundamentos da Computação Quântica**: Conceitos centrais que formam a base da computação quântica, você encontrará:
    - [Computação Quântica](07-computacao_quantica.md) : Introdução aos princípios e elementos fundamentais da computação quântica.
    - [Tutorial do Ket](08-kettutorial.ipynb) : Guia prático para utilizar a plataforma de programação quântica Ket.

- **Algoritmos Quânticos**: Estudo dos principais algoritmos quânticas da literatura atual, nessa sessão, você estudará:
    - [Como Entender um Algoritmo](09-algoritmos.md) : Metodologia para análise e compreensão de algoritmos quânticos.
        - [Algoritmos Introdutórios](algoritmos/introdutórios/09_1_0-algoritmos_introdutórios.md) : Algoritmos básicos que introduzem conceitos fundamentais.
        - [Algoritmos de Busca](algoritmos/busca/09_2_0-algoritmos_de_busca.md) : Algoritmos como o de Grover para busca em bancos de dados.
        - [Algoritmos Baseados em QFT](algoritmos/baseados_em_QFT/09_3_0-algoritmos_qft.md) : Algoritmos que utilizam a Transformada Quântica de Fourier.
        - [Algoritmos Variacionais](algoritmos/variacionais/09_4_0-algoritmos_variacionais.md) : Algoritmos híbridos quântico-clássicos para otimização.

- [Referências](10-referencias.md) : Fontes bibliográficas.
