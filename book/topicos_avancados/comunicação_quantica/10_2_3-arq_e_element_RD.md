# Arquitetura e Elementos de Redes Quânticas

Uma rede quântica é composta por diferentes elementos que permitem a transmissão de estados quânticos e a distribuição de emaranhamento entre sistemas distantes. Diferente de redes clássicas, sua arquitetura é fortemente influenciada por restrições fundamentais da mecânica quântica, como a impossibilidade de clonagem e a sensibilidade à medição.

De forma geral, uma rede quântica pode ser modelada como um sistema no qual estados quânticos são preparados, transformados por canais físicos e posteriormente medidos, gerando informação clássica.

## Modelo geral de uma rede quântica

Formalmente, a comunicação em uma rede quântica pode ser descrita como a evolução de um estado quântico $\rho$ através de um canal quântico $\mathcal{E}$:

$$
\rho \rightarrow \mathcal{E}(\rho)
$$

onde $\mathcal{E}$ é um **mapa completamente positivo e preservador de traço (CPTP)**.

Após a transmissão, medições são realizadas, produzindo resultados clássicos que podem ser utilizados para inferir informação ou completar protocolos.

Esse modelo conecta diretamente a arquitetura de redes quânticas com a teoria da informação quântica, permitindo analisar perda de informação, ruído e limites de comunicação.

## Componentes de uma rede quântica

### Nós quânticos

Os nós quânticos são sistemas físicos capazes de armazenar e manipular informação quântica. Cada nó pode ser descrito por um espaço de Hilbert e operações locais que atuam sobre seus estados.

Em um nó quântico, é possível:

* preparar estados $\rho$
* aplicar operações unitárias
* realizar medições
* armazenar qubits (memória quântica)

Além disso, nós podem compartilhar estados emaranhados com outros nós, formando a base de muitos protocolos de comunicação.

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

Do ponto de vista da teoria da informação, os canais determinam **quanto da informação original pode ser preservada ou transmitida**.

### Canais clássicos

Mesmo em redes quânticas, a comunicação clássica é indispensável. Ela é utilizada para:

* transmitir resultados de medições
* coordenar protocolos distribuídos
* aplicar correções condicionais

Assim, redes quânticas são, na prática, sistemas **híbridos**, combinando comunicação clássica e quântica.

## Fluxo de informação em uma rede quântica

O funcionamento de uma rede quântica pode ser entendido como um fluxo de transformação de informação:

1. um estado quântico $\rho$ é preparado em um nó
2. o estado é transmitido por um canal $\mathcal{E}$
3. o estado resultante $\mathcal{E}(\rho)$ é medido
4. a medição gera informação clássica

Esse processo evidencia que a informação quântica não é acessada diretamente, mas sim através de medições, que podem introduzir perda de informação.

Além disso, em muitos protocolos, o objetivo não é transmitir diretamente um estado, mas **estabelecer correlações (emaranhamento)** entre diferentes nós.

## Tarefas fundamentais em redes quânticas

As redes quânticas são projetadas para executar tarefas específicas relacionadas à manipulação de informação.

### Distribuição de estados

Consiste em enviar um estado quântico entre nós. Esse processo é limitado pela ação do canal $\mathcal{E}$, que pode degradar o estado.

### Distribuição de emaranhamento

Uma das tarefas centrais é gerar estados emaranhados entre nós distantes. Esse recurso é essencial para protocolos como teletransporte e comunicação superdensa.

### Processamento distribuído

Em alguns casos, operações quânticas são realizadas de forma distribuída entre diferentes nós, utilizando comunicação clássica e recursos quânticos compartilhados.

## Limitações estruturais

A arquitetura de redes quânticas é fortemente impactada por limitações físicas.

Uma das mais importantes é a impossibilidade de amplificar estados quânticos arbitrários sem introduzir erro, consequência direta do teorema da não clonagem.

Além disso, canais quânticos são sujeitos a ruído e perdas, o que reduz a fidelidade dos estados transmitidos. Esses efeitos limitam a distância e a taxa de comunicação.

## Conexão com teoria da informação quântica

A descrição de redes quânticas está diretamente relacionada à teoria da informação quântica.

Os canais quânticos determinam a **capacidade de transmissão de informação**, enquanto resultados como o teorema de Holevo impõem limites à quantidade de informação clássica que pode ser extraída de estados quânticos.

A entropia de von Neumann, por sua vez, permite quantificar incerteza, correlações e perda de informação ao longo do processo de comunicação.

## Observação

A arquitetura de redes quânticas mostra que a comunicação quântica não se resume ao envio de mensagens, mas envolve a manipulação de estados, correlações e recursos distribuídos.

Nos próximos tópicos, esses elementos serão utilizados para descrever protocolos específicos e analisar como a informação é efetivamente transmitida em sistemas quânticos.
