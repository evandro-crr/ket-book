# Álgebra Linear para Computação Quântica

```{note}
Material extraído do TCC [*Computação Quântica: Uma abordagem para estudantes de graduação em Ciências Exatas*](./tcc-giovani.pdf), de Giovani Goraiebe Pollachini.
```

NESTE capítulo, um resumo de Álgebra Linear voltado para Computação Quântica é apresentado. A teoria é apresentada usando-se a *notação de Dirac*, ou, *notação de braket*, uma notação utilizada largamente em Mecânica Quântica e que será necessária para o restante do trabalho. Essa notação é conveniente para se fazer contas e faz com que as diversas operações possíveis se encaixem naturalmente.

Na Álgebra Linear abstrata, pode-se considerar espaços vetoriais sobre diversos corpos (ou escalares), que são estruturas algébricas com propriedades semelhantes aos números reais e complexos. Os espaços vetoriais podem ter dimensão finita ou infinita.

Na Computação Quântica o interesse é voltado a espaços vetoriais de **dimensão finita** sobre o corpo dos números complexos. Isso permite a identificação do espaço com as $n$-uplas de números complexos, o que simplifica grandemente a teoria. Os resultados resumidos neste capítulo estão situados nesse contexto.

A principal referência para esse capítulo é {cite}`nielsen_quantum_2010`. Outra referência muito útil é {cite}`lima_algebra_2021`, que possui um capítulo voltado a espaços vetoriais complexos. Livros texto clássicos de Álgebra Linear, como {cite}`steinbruch_algebra_2009` também são úteis. Embora tenham ênfase em espaços vetoriais reais, a maioria das definições, resultados e demonstrações se transporta integralmente para os espaços vetoriais complexos.

Será considerado um pré-requisito a este texto um curso de Álgebra Linear ao nível de graduação abordando-se os seguintes itens: espaços vetoriais, base e dimensão, transformações lineares, autovalores e autovetores. Por ter um caráter de resumo, os resultados apresentados, via de regra, não são acompanhados de suas demonstrações, as quais podem ser encontradas nos livros mencionados no parágrafo anterior.

## Notação de Dirac

Como mencionado, neste trabalho será utilizada a notação de Dirac ou notação de Braket. Esta notação é uma forma compacta de representar vetores, permitindo representar cálculos e operações de forma mais compacta e intuitiva.

Esta notação consiste de 2 representações o ket $\ket{\cdot}$ e o bra $\bra{\cdot}$

### Ket
O ket representa um vetor coluna, isto é, um vetor com uma única coluna:

$$
\ket{\psi} = \begin{bmatrix}  z_0 \\ z_1 \\ \vdots \\ z_{n-1} \end{bmatrix}
$$

Este vetor lê-se como *ket* $\psi$.

### Bra
O bra representa o ket$^\dagger$, onde $\dagger$ (adaga/dagger) é equivalente às operações de conjugação e transposição. Portanto, bra será o vetor linha cujos sinais das partes imaginárias serão opostos ao do ket:

$$
\bra{\psi} = \ket{\psi}^\dagger = \begin{bmatrix} z_{0}^{*} & z_{1}^{*} & \cdots & z_{n-1}^{*} \end{bmatrix}
$$

Este vetor lê-se como *bra* $\psi$.

::: {admonition} Exemplo
:class: tip
Dado um vetor $v$, onde:

$$
v = \begin{bmatrix} 3 + 9i \\ 19 - 8i \end{bmatrix}
$$

Temos que:

O *ket* é o vetor em forma de coluna:

$$
\ket{v} = \begin{bmatrix} 3 + 9i \\ 19 - 8i \end{bmatrix}
$$

O *bra* é obtido aplicando o operador $\dagger$ (transposição + conjugação):

$$
\bra{v} = \ket{v}^\dagger = (\ket{v}^*)^T = \begin{bmatrix} 3 - 9i \\ 19 + 8i \end{bmatrix}^T = \begin{bmatrix} 3 - 9i & 19 + 8i \end{bmatrix}
$$

:::

