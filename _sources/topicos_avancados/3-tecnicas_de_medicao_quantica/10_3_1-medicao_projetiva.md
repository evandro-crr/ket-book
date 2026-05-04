# Medição Projetiva

A **medição projetiva** constitui um dos elementos centrais da formulação da mecânica quântica, sendo o mecanismo formal responsável por conectar estados quânticos — descritos por vetores em um espaço de Hilbert — a resultados clássicos observáveis. Em computação quântica, ela desempenha um papel essencial, pois é através dela que a informação codificada em superposição e entrelaçamento se torna acessível.

Diferentemente da evolução unitária, que é contínua, determinística e reversível, a medição projetiva introduz uma dinâmica intrinsecamente probabilística e não reversível. Esse processo não apenas extrai informação, mas também altera o estado do sistema, caracterizando a chamada transição do domínio quântico para o clássico.

## Estrutura Matemática e Interpretação

Formalmente, uma medição projetiva é descrita por um conjunto de operadores ${P_i}$ definidos sobre um espaço de Hilbert $\mathcal{H}$, satisfazendo propriedades fundamentais: são hermitianos, idempotentes, mutuamente ortogonais e completos. Essas condições garantem que cada operador $P_i$ atua como um projetor ortogonal sobre um subespaço específico de $\mathcal{H}$, e que o conjunto completo desses projetores induz uma decomposição direta do espaço:

$$
\mathcal{H} = \bigoplus_i \mathcal{H}_i
$$

Essa estrutura revela um ponto conceitual importante: a medição não seleciona um vetor específico, mas sim um subespaço do espaço de estados. Em particular, quando há degenerescência — isto é, múltiplos estados associados ao mesmo resultado — o colapso ocorre para um subespaço de dimensão maior que 1, preservando parcialmente a informação interna a esse subespaço.

Do ponto de vista operacional, cada projetor $P_i$ corresponde a um possível resultado da medição. A probabilidade de observar esse resultado é dada pela **regra de Born generalizada**, que assume formas equivalentes para estados puros e mistos:

$$
p(i) = \bra{\psi} P_i \ket{\psi}, \quad \text{ou} \quad p(i) = \mathrm{Tr}(P_i \rho)
$$

Essa formulação destaca que apenas a projeção do estado sobre o subespaço relevante contribui para a probabilidade. Fases globais são irrelevantes, e coerências entre subespaços distintos não influenciam diretamente os resultados observáveis.

## Dinâmica e Estrutura Estatística

Além de definir probabilidades, a medição projetiva induz uma transformação no estado do sistema. No caso de um resultado específico $i$, o estado é atualizado de forma condicional:

$$
\ket{\psi} \rightarrow \frac{P_i \ket{\psi}}{\sqrt{\bra{\psi} P_i \ket{\psi}}},
\quad
\rho \rightarrow \frac{P_i \rho P_i}{\mathrm{Tr}(P_i \rho)}
$$

Essa transformação possui propriedades importantes: é completamente positiva, preserva o traço, mas não é unitária nem reversível. Isso reflete o fato de que a medição envolve perda de informação — especialmente sobre coerências quânticas.

Se o resultado da medição não é observado (caso não seletivo), a dinâmica é descrita por um canal quântico:

$$
\mathcal{E}(\rho) = \sum_i P_i \rho P_i
$$

Esse mapa remove os termos fora da diagonal na base dos projetores, caracterizando um processo formal de **decoerência**. Em termos práticos, isso significa a perda de interferência quântica e a conversão de superposições em distribuições clássicas de probabilidades.

Consequentemente, a medição projetiva pode ser interpretada como a definição de uma variável aleatória clássica $X$, com distribuição:

$$
\mathbb{P}(X = i) = \mathrm{Tr}(P_i \rho)
$$

Essa conexão explicita como o formalismo quântico se integra à teoria clássica de probabilidades.

## Relação com Observáveis e Base de Medição

Toda medição projetiva pode ser associada a um operador hermitiano $A$, decomponível como:

$$
A = \sum_i a_i P_i
$$

onde os $a_i$ representam os possíveis valores observados. Essa decomposição estabelece uma correspondência direta entre espectro do operador e resultados da medição.

Um aspecto fundamental é que a medição depende intrinsecamente da base escolhida. Medir em uma base arbitrária é equivalente a aplicar uma transformação unitária seguida de uma medição na base computacional:

$$
P_i^{(U)} = U \ket{i}\bra{i} U^\dagger
$$

Esse princípio é central em computação quântica, pois a escolha da base determina quais propriedades do sistema serão acessíveis.

Além disso, medições associadas a operadores que comutam podem ser realizadas simultaneamente sem perturbação mútua. Quando operadores não comutam, a ordem das medições afeta os resultados, refletindo a estrutura não clássica da teoria.

## Sistemas Compostos e Efeitos Não Locais

Em sistemas compostos, descritos por espaços tensoriais $\mathcal{H}_A \otimes \mathcal{H}_B$, medições podem atuar localmente, mas ainda assim produzir efeitos globais. Em particular, se o sistema estiver entrelaçado, uma medição em uma parte pode induzir mudanças instantâneas na outra, fenômeno frequentemente descrito como colapso não local.

Esse comportamento não permite comunicação superluminal, mas evidencia a natureza profundamente não clássica da correlação quântica.

## Papel em Computação Quântica

Na prática, a medição projetiva é indispensável em computação quântica. Todo algoritmo quântico termina com uma medição, responsável por extrair o resultado final. No entanto, o sucesso do algoritmo depende criticamente do estado antes da medição, especialmente das interferências construídas ao longo da computação.

A escolha da base de medição define quais informações serão acessíveis, enquanto a própria medição atua como um mecanismo que converte informação quântica — rica em coerência e entrelaçamento — em dados clássicos utilizáveis.

Além disso, medições são frequentemente utilizadas em sub-rotinas, como preparação de estados, filtragem de resultados e protocolos adaptativos.

## Considerações Físicas e Informacionais

Do ponto de vista físico, a medição projetiva levanta questões fundamentais, pois o colapso do estado não é descrito pela evolução unitária governada pela equação de Schrödinger. Isso introduz uma descontinuidade no formalismo e sugere a necessidade de um aparato clássico para interpretar resultados.

Apesar dessas questões conceituais, o modelo é extremamente bem validado experimentalmente e funciona como uma ferramenta operacional precisa.

Sob a ótica da teoria da informação, a medição converte informação quântica em clássica, reduzindo coerências e, em muitos casos, aumentando a entropia média do sistema. Esse processo formaliza a perda de acessibilidade de certas informações quânticas após a medição.

## Conclusão

A medição projetiva não é apenas um componente técnico da mecânica quântica, mas o ponto onde toda a teoria se conecta com a observação. Ela define como resultados clássicos emergem de estados quânticos, introduz irreversibilidade e aleatoriedade, e atua como um mecanismo formal de decoerência.

Em computação quântica, seu papel é duplo: é tanto o meio de leitura dos resultados quanto um elemento estrutural que influencia profundamente o desenho dos algoritmos.
