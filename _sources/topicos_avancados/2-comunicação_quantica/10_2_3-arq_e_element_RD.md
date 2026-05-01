# Arquitetura e Elementos de Redes Quânticas

Uma rede quântica é composta por diferentes elementos que permitem a transmissão de estados quânticos e a distribuição de emaranhamento entre sistemas distantes. Diferente de redes clássicas, sua arquitetura é fortemente influenciada por restrições fundamentais da mecânica quântica, como a impossibilidade de clonagem e a sensibilidade à medição.

Essas restrições fazem com que redes quânticas não possam ser construídas simplesmente adaptando infraestruturas clássicas. Em vez disso, é necessário repensar a forma como a informação é transmitida, armazenada e processada, levando em conta que estados quânticos não podem ser copiados, amplificados ou observados sem perturbação.

De forma geral, uma rede quântica pode ser modelada como um sistema no qual estados quânticos são preparados, transformados por canais físicos e posteriormente medidos, gerando informação clássica. Esse modelo estabelece uma ponte direta entre a arquitetura física da rede e o formalismo da teoria da informação quântica.

## Modelo geral de uma rede quântica

Formalmente, a comunicação em uma rede quântica pode ser descrita como a evolução de um estado quântico $\rho$ através de um canal quântico $\mathcal{E}$:

$$
\rho \rightarrow \mathcal{E}(\rho)
$$

onde $\mathcal{E}$ é um **mapa completamente positivo e preservador de traço (CPTP)**.

Essa descrição encapsula todos os efeitos físicos envolvidos na transmissão, incluindo ruído, perdas e interação com o ambiente. Dessa forma, a comunicação deixa de ser apenas um processo de envio de informação e passa a ser vista como uma **transformação de estados** sujeita a degradação.

Após a transmissão, medições são realizadas, produzindo resultados clássicos que podem ser utilizados para inferir informação ou completar protocolos. Esse passo é essencial, pois a informação quântica só se torna acessível por meio da medição.

Essa estrutura evidencia uma distinção importante:

* o estado quântico contém informação potencial
* a medição extrai apenas uma parte dessa informação

Esse modelo conecta diretamente a arquitetura de redes quânticas com a teoria da informação quântica, permitindo analisar perda de informação, ruído e limites de comunicação de forma quantitativa.

## Componentes de uma rede quântica

### Nós quânticos

Os nós quânticos são sistemas físicos capazes de armazenar e manipular informação quântica. Cada nó pode ser descrito por um espaço de Hilbert e por operações locais que atuam sobre seus estados.

Em um nó quântico, é possível:

* preparar estados $\rho$
* aplicar operações unitárias
* realizar medições
* armazenar qubits (memória quântica)

Além disso, nós podem compartilhar estados emaranhados com outros nós, formando a base de muitos protocolos de comunicação.

Do ponto de vista operacional, os nós funcionam como unidades de processamento e armazenamento, análogas a computadores em redes clássicas. No entanto, diferem fundamentalmente pelo fato de que a informação armazenada não pode ser copiada nem observada sem perturbação.

### Canais quânticos

Os canais quânticos descrevem a transmissão de estados entre nós e são formalmente representados por mapas CPTP.

Uma representação comum é dada pelos **operadores de Kraus**:

$$
\mathcal{E}(\rho) = \sum_k E_k \rho E_k^\dagger
$$

com

$$
\sum_k E_k^\dagger E_k = I
$$

Essa formulação permite modelar efeitos físicos como:

* decoerência
* perda de fótons
* ruído

Do ponto de vista da teoria da informação, os canais determinam **quanto da informação original pode ser preservada ou transmitida**. Em particular, eles definem limites como capacidade de transmissão e fidelidade do estado recebido.

É importante observar que, diferentemente de canais clássicos, canais quânticos não permitem amplificação sem degradação, o que tem impacto direto na construção de redes de longa distância.

### Canais clássicos

Mesmo em redes quânticas, a comunicação clássica é indispensável. Ela é utilizada para:

* transmitir resultados de medições
* coordenar protocolos distribuídos
* aplicar correções condicionais

Em muitos protocolos, como o teletransporte quântico, a comunicação clássica é necessária para completar a transmissão de informação.

Assim, redes quânticas são, na prática, sistemas **híbridos**, nos quais canais quânticos e clássicos desempenham papéis complementares.

## Fluxo de informação em uma rede quântica

O funcionamento de uma rede quântica pode ser entendido como um fluxo de transformação de informação:

1. um estado quântico $\rho$ é preparado em um nó
2. o estado é transmitido por um canal $\mathcal{E}$
3. o estado resultante $\mathcal{E}(\rho)$ é medido
4. a medição gera informação clássica

Esse processo evidencia que a informação quântica não é acessada diretamente, mas sim através de medições, que podem introduzir perda de informação e irreversibilidade.

Além disso, em muitos protocolos, o objetivo não é transmitir diretamente um estado, mas **estabelecer correlações (emaranhamento)** entre diferentes nós. Nesse caso, a informação relevante não está em um sistema isolado, mas nas correlações entre sistemas distribuídos.

## Tarefas fundamentais em redes quânticas

As redes quânticas são projetadas para executar tarefas específicas relacionadas à manipulação, transmissão e processamento de informação quântica. Essas tarefas exploram propriedades exclusivamente quânticas, como superposição e emaranhamento, permitindo funcionalidades que não possuem equivalente clássico direto.

### Distribuição de estados

A distribuição de estados consiste na transmissão de um estado quântico entre diferentes nós da rede. Esse processo é fundamental para diversas aplicações, mas é fortemente influenciado pelas imperfeições do meio físico.

Em termos formais, a evolução do estado pode ser descrita por um canal quântico $\mathcal{E}$, que introduz ruído e pode degradar a informação. Como consequência, o estado recebido geralmente apresenta uma fidelidade reduzida em relação ao estado original, tornando necessário o uso de técnicas de mitigação de erro e correção quântica.

### Distribuição de emaranhamento

A distribuição de emaranhamento é uma das tarefas centrais em redes quânticas. Ela consiste em gerar estados emaranhados entre nós espacialmente separados, criando correlações quânticas que não podem ser reproduzidas por sistemas clássicos.

Esse recurso é essencial para protocolos fundamentais, como o teletransporte quântico e a comunicação superdensa. Do ponto de vista da teoria da informação, o emaranhamento pode ser interpretado como um recurso que amplia as capacidades operacionais da rede, permitindo a realização de tarefas que seriam impossíveis em sua ausência.

### Processamento distribuído

O processamento quântico distribuído envolve a execução de operações quânticas de forma cooperativa entre diferentes nós da rede. Nesse modelo, sistemas locais são combinados por meio de comunicação clássica e compartilhamento de recursos quânticos, como estados emaranhados.

Essa abordagem permite contornar limitações físicas de dispositivos individuais, como número reduzido de qubits ou alta taxa de erro, ao mesmo tempo em que possibilita arquiteturas modulares e escaláveis. Além disso, o processamento distribuído é um elemento chave para o desenvolvimento de redes quânticas de larga escala.## Limitações estruturais

A arquitetura de redes quânticas é fortemente impactada por limitações físicas.

Uma das mais importantes é a impossibilidade de amplificar estados quânticos arbitrários sem introduzir erro, consequência direta do teorema da não clonagem. Isso impede o uso de estratégias clássicas como repetição e amplificação de sinal.

Além disso, canais quânticos são sujeitos a ruído e perdas, o que reduz a fidelidade dos estados transmitidos. Esses efeitos limitam:

* a distância de comunicação
* a taxa de transmissão
* a qualidade dos estados distribuídos

Essas limitações motivam o desenvolvimento de técnicas específicas, como repetidores quânticos e destilação de emaranhamento.

## Conexão com teoria da informação quântica

A descrição de redes quânticas está diretamente relacionada à teoria da informação quântica.

Os canais quânticos determinam a **capacidade de transmissão de informação**, enquanto resultados como o teorema de Holevo impõem limites à quantidade de informação clássica que pode ser extraída de estados quânticos.

A entropia de von Neumann, por sua vez, permite quantificar:

* incerteza associada a estados
* correlações entre subsistemas
* perda de informação ao longo da transmissão

Essa conexão permite analisar redes quânticas de forma quantitativa, indo além de descrições puramente qualitativas.

## Observação

A arquitetura de redes quânticas mostra que a comunicação quântica não se resume ao envio de mensagens, mas envolve a manipulação de estados, correlações e recursos distribuídos.

Mais do que transmitir informação, redes quânticas permitem **controlar como a informação é distribuída e acessada** entre diferentes sistemas.

Nos próximos tópicos, esses elementos serão utilizados para descrever protocolos específicos e analisar como a informação é efetivamente transmitida em sistemas quânticos.