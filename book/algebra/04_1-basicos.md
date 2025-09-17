# Conceitos Básicos de Álgebra

## Espaço Vetorial, Base e Dimensão

### Espaço Vetorial

O conjunto das $n$-uplas $(z_0, \ldots, z_{n-1})$ de números complexos com a soma e o produto por escalar definidos entrada a entrada é um *Espaço Vetorial Complexo* e é denotado por $\mathbb{C}^n$. É conveniente representar esses elementos por vetores coluna. Tem-se então:

$$
\begin{bmatrix}z_0 \\ z_{1} \\ \vdots \\ z_{n-1}\end{bmatrix} + \begin{bmatrix}w_0 \\ w_{1} \\ \vdots \\ w_{n-1}\end{bmatrix} = \begin{bmatrix}z_0 + w_0\\ z_{1} + w_1 \\ \vdots \\ z_{n-1} + w_{n-1}\end{bmatrix}  \ \ \ \text{ e } \ \ \   z \cdot \begin{bmatrix}z_0 \\ z_{1} \\ \vdots \\ z_{n-1}\end{bmatrix} = \begin{bmatrix}z \cdot z_0 \\ z\cdot z_{1} \\ \vdots \\ z \cdot z_{n-1}\end{bmatrix} \ .
$$

Em Mecânica Quântica, os vetores de $\mathbb{C}^n$ costumam ser usados na *notação de Dirac*, ou *notação de braket*:

$$
\ket{\psi} = (z_0 , z_{1} , \ldots , z_{n-1} ) =  \begin{bmatrix}z_0 \\ z_{1} \\ \vdots \\ z_{n-1}\end{bmatrix}   \ \ .
$$

Um vetor $\ket{\psi}$ é chamado *ket* (em contraponto com $\bra{\psi}$, que será definido posteriormente, e será chamado  *bra*).

Os vetores se comportam de maneira semelhante aos números no que diz respeito à soma e subtração. Em particular, a soma comuta $\ket{\phi} + \ket{\psi} = \ket{\psi} + \ket{\phi}$, há um vetor nulo, denotado por $0$ ou $\ket{\varnothing} = (0, \ldots , 0)$ de tal forma que $\ket{\psi} + 0 = \ket{\psi}$ e, ainda, vale $-\ket{\psi} = (-z_0, \dots , -z_{n-1}) = -1 \cdot \ket{\psi}$. O produto por escalar também se comporta de maneira semelhante ao produto numérico, e valem as propriedades distributivas $z(\ket{\phi} + \ket{\psi}) = z \ket{\phi} + z \ket{\psi}$ e $(z+w)\ket{\psi} = z\ket{\psi} + w \ket{\psi}$, por exemplo.

:::{admonition} Espaço de estados de 1 qubit
:class: tip

O conjunto

$$
\mathbb{C}^2 = \left\{ \ket{\psi} = \begin{bmatrix} a \\ b \end{bmatrix} : a,b \in \mathbb{C}\right\}
$$

é um espaço vetorial com soma e produto por escalar dados por

$$
\begin{bmatrix} a_1 \\ b_1 \end{bmatrix} + \begin{bmatrix} a_2 \\ b_2 \end{bmatrix} = \begin{bmatrix} a_1 + a_2 \\ b_1 + b_2 \end{bmatrix}
$$

$$
z \cdot \begin{bmatrix} a \\ b \end{bmatrix} = \begin{bmatrix} za \\ zb \end{bmatrix} \ .
$$

Esse espaço vetorial será largamente utilizado nos capítulos seguintes e descreve o espaço de estados de 1 *qubit*, o análogo do bit clássico.
:::

### Base e Dimensão

Uma base para o espaço vetorial $\mathbb{C}^n$ é um conjunto de vetores *linearmente independentes* (LI) e que *geram o espaço*.  Demonstra-se que todas as bases de um espaço vetorial têm o mesmo número de elementos, e define-se a *dimensão* do espaço vetorial pelo número de elementos de uma base.

O espaço vetorial $\mathbb{C}^n$ tem dimensão $n$, isto é, todas as suas bases têm $n$ vetores. Uma base muito útil é a chamada *base computacional*, ou base canônica\`(O adjetivo "canônico", na Matemática, tem um sentido de "padrão", como na expressão "configuração padrão"):

$$
\ket{0} = \begin{bmatrix}1 \\ 0 \\ \vdots \\ 0\end{bmatrix} \ \ , \ \ \ket{1} = \begin{bmatrix}0 \\ 1 \\ \vdots \\ 0 \end{bmatrix}  \ \ , \ \ \cdots \ \ , \ \ \ket{n-1}^= \begin{bmatrix}0 \\ 0 \\ \vdots \\ 1\end{bmatrix}  \ \ .
$$

Na base computacional, um vetor $\ket{\psi} = (z_0 , z_{1} , \ldots , z_{n-1} )$ é escrito como

$$
\ket{\psi} = z_0 \ket{0} + z_1 \ket{1} + \ldots + z_{n-1} \ket{n-1} \ \ .
$$

Numa base qualquer $\beta = \big\{\ket{b_0}, \ldots, \ket{b_{n-1}} \big\}$, qualquer vetor $\psi$ pode ser escrito como combinação linear dos vetores dessa base. Os coeficientes da combinação linear, colocados em um vetor coluna, representam o vetor $\psi$ escrito na base $\beta$, conforme o esquema abaixo:

$$
\ket{\psi} = a_0 \ket{b_0} + \ldots + a_{n-1} \ket{b_{n-1}} \ \  \Leftrightarrow \ \ \big[ \ket{\psi} \big]_\beta = \begin{bmatrix} a_0 \\ \vdots \\ a_{n-1} \end{bmatrix}_\beta \ .
$$

O subscrito $\beta$ pode ser omitido se não houver risco de confusão. Normalmente omite-se esse subscrito quando se trata da base computacional.

(base-para-1-qubit)=

:::{admonition} Bases para 1 qubit
:class: tip

Há especial interesse no espaço $\mathbb{C}^2$. Este espaço modela um *qubit* --- o análogo quântico do bit --- a ser discutido em mais detalhes posteriormente. O espaço $\mathbb{C}^2$ tem dimensão $2$ e admite, entre outras, as seguintes bases:

$$
\begin{array}{rll}
  \mathcal{I} = \mathcal{Z} &=& \big\{ \ket{0} \  , \  \ket{1} \big\} \\
  \mathcal{X} &=& \left\{ \ket{+} = \tfrac{1}{\sqrt{2}}( \ket{0} + \ket{1}) \ , \  \ket{-} = \tfrac{1}{\sqrt{2}}( \ket{0} - \ket{1})  \right\} \\
  \mathcal{Y} &=& \left\{ \ket{+i} = \tfrac{1}{\sqrt{2}}( \ket{0} + i\ket{1}) , \ket{-i} = \tfrac{1}{\sqrt{2}}( \ket{0} -i \ket{1}) \right\} \ \ .
\end{array}
$$

Essa notação para as bases será justificada *a posteriori*.
:::

:::{admonition} $\mathcal{X}$ é base para 1 qubit
:class: tip

Para mostrar que

$$
\mathcal{X} = \left\{ \ket{+} = \tfrac{1}{\sqrt{2}}( \ket{0} + \ket{1}) \ , \  \ket{-} = \tfrac{1}{\sqrt{2}}( \ket{0} - \ket{1})  \right\}
$$

é base do espaço de estados de 1 qubit, deve-se mostrar que os vetores são LI (Linearmente Independentes) e geram o espaço $\mathbb{C}^2$.

$\mathcal{X}$ **é LI**: Considere a combinação linear nula:

$$
\begin{array}{r}
a_0 \ket{+} + a_1 \ket{-} = 0 \\
a_0 \frac{1}{\sqrt{2}}( \ket{0} + \ket{1}) + a_1 \frac{1}{\sqrt{2}}( \ket{0} - \ket{1}) = 0 \\
\frac{a_0 + a_1}{\sqrt{2}} \ket{0} + \frac{a_0 - a_1}{\sqrt{2}} \ket{1} = 0
\end{array}
$$

Tem-se que

$$
\begin{cases}
  \frac{a_0 + a_1}{\sqrt{2}} = 0 \\
  \frac{a_0 - a_1}{\sqrt{2}} = 0
\end{cases}
\implies
\begin{cases}
  a_0 + a_1 = 0 \\
  a_0 - a_1 = 0
\end{cases}
\implies
\begin{cases}
  a_0 = 0 \\
  a_1 = 0 \ .
\end{cases}
$$

Portanto os coeficientes da combinação linear nula devem ser todos nulos, e isso significa que os vetores $\ket{+}$ e $\ket{-}$ são LI.

$\mathcal{X}$ **gera o espaço**: Seja $\ket{\psi} = z_0 \ket{0} + z_1 \ket{1}$ um vetor qualquer de $\mathbb{C}^2$. Tenta-se escrever $\ket{\psi}$ como combinação linear de $\ket{+}$ e $\ket{-}$. Se for possível, esses vetores geram o espaço.

$$
\begin{array}{rll}
  z_0 \ket{0} + z_1 \ket{1}
  &=& a_0 \ket{+} + a_1 \ket{-} \\
  &=& a_0 \frac{1}{\sqrt{2}}( \ket{0} + \ket{1}) + a_1 \frac{1}{\sqrt{2}}( \ket{0} - \ket{1}) \\
  &=&  \frac{a_0 + a_1}{\sqrt{2}} \ket{0} + \frac{a_0 - a_1}{\sqrt{2}} \ket{1}
\end{array}
$$

Assim,

$$
\begin{cases}
\frac{a_0 + a_1}{\sqrt{2}} = z_0 \\
\frac{a_0 - a_1}{\sqrt{2}} = z_1
\end{cases}
\implies
\begin{cases}
a_0 = \frac{z_0 + z_1}{\sqrt{2}} \\
a_1 = \frac{z_0 - z_1}{\sqrt{2}}
\end{cases}
$$

Dessa forma, $\mathcal{X}$ gera o espaço $\mathbb{C}^2$ e é base desse espaço.

**Comentário**: Quando se sabe previamente que a dimensão do espaço é $n$ e se a lista de vetores candidatos a base tem $n$ elementos, então as condições de ser LI e gerar o espaço são equivalentes. Em consequência, basta verificar uma das condições para mostrar que os vetores formam uma base. Por exemplo, se sabemos que a dimensão de $\mathbb{C}^2$ é $\dim \mathbb{C}^2 = 2$, e temos que $\mathcal{X}$ tem dois elementos, então bastaria verificar uma das duas condições: $\mathcal{X}$ é LI ou $\mathcal{X}$ gera o espaço.
:::

:::{admonition} Exercício
:class: tip

Um Qubit se encontra em um estado:

$$
\frac{1}{2}\ket{0}-\frac{\sqrt{3}}{2}\ket{1}
$$

Escreva esse estado utilizando-se da notação de colunas

:::

:::{admonition} Exercício
:class: tip

Escreva uma função em Python que recebe uma matriz coluna dado por uma lista ou tuple e retorna ao usuário o a combinação linear dos vetores na notação de Dirac.

:::

(cap2matriz-de-mudanca-de-base)=

### Matriz de Mudança de base

Por vezes é conveniente expressar um vetor em outra base que não a base computacional. Essa mudança de base pode trazer novo *insight* em algumas situações, bem como tornar os cálculos mais simples e factíveis.

A matriz de mudança de base de $\beta_{\text{old}} = \big\{\ket{u_0}, \ldots, \ket{u_{n-1}} \big\}$ para $\beta_{\text{new}} = \big\{ \ket{v_0}, \ldots, \ket{v_{n-1}} \big\}$ é dada por

$$
[I]^{\beta_{\text{old}}}_{\beta_{\text{new}} } = \left[ \begin{matrix} | & & | \\ \big[\ket{v_0}\big]_{\beta_{\text{old}}} & \cdots & \big[\ket{v_{n-1}}\big]_{\beta_{\text{old}}} \\  | & & | \end{matrix} \right] \ .
$$

Isto é, para montar a matriz de mudança de base, os vetores da base nova devem ser escritos como combinação linear dos vetores da base antiga, obtendo vetores coluna. Esses vetores serão as colunas da matriz de mudança de base. Dessa forma, tem-se

$$
[v]_{\beta_{\text{new}}} = [I]^{\beta_{\text{old}}}_{\beta_{\text{new}} } [v]_{\beta_{\text{old}}} \ .
$$

A matriz de mudança de base admite matriz inversa, que corresponde à mudança de base da base nova de volta para a base antiga:

$$
[I]^{\beta_{\text{old}}}_{\beta_{\text{new}} }\phantom{|} ^{-1} = [I]^{\beta_{\text{new}}}_{\beta_{\text{old}} } \ .
$$

:::{note}
O símbolo $I$ na matriz de mudança de base $[I]^{\beta_{\text{old}}}_{\beta_{\text{new}}}$ refere-se ao operador identidade.
A matriz de mudança de base corresponde à matriz do operador identidade nas bases $\beta_{\text{old}}$ e $\beta_{\text{new}}$.
As matrizes referente a operadores lineares serão vistas na seção [Matriz de uma Transformação Linear](cap2sec-matriz-tl).
:::

(cap2ex-matrix-mudanca-de-base)=

:::{admonition} Exemplo
:class: tip

Considere as bases $\mathcal{I}$ e $\mathcal{X}$ apresentadas no exemplo [Base para 1 qubit]. A matriz de mudança de base da base computacional $\mathcal{I}$ para a base $\mathcal{X}$ é obtida escrevendo os vetores da base nova ($\mathcal{X}$) como combinação linear dos vetores na base antiga ($\mathcal{I}$):

$$
\begin{array}{c}
\ket{+}
&=& \frac{1}{\sqrt{2}} \ket{0} + \frac{1}{\sqrt{2}}  \ket{1}  = \begin{bmatrix} \frac{1}{\sqrt{2}}\\ \frac{1}{\sqrt{2}} \end{bmatrix}_{\mathcal{I}}\\
\ket{-}
&=& \frac{1}{\sqrt{2}} \ket{0} - \frac{1}{\sqrt{2}} \ket{1} = \begin{bmatrix} \phantom{-} \frac{1}{\sqrt{2}}\\  - \frac{1}{\sqrt{2}} \end{bmatrix}_{\mathcal{I}}
\end{array}
$$

Colocam-se as os vetores coluna na ordem em que aparecem na lista:

$$
[I]^\mathcal{I}_\mathcal{X} = \begin{bmatrix}  \begin{bmatrix} \frac{1}{\sqrt{2}}\\ \frac{1}{\sqrt{2}} \end{bmatrix}_{\mathcal{I}} & \begin{bmatrix} \phantom{-} \frac{1}{\sqrt{2}}\\  - \frac{1}{\sqrt{2}} \end{bmatrix}_{\mathcal{I}} \end{bmatrix} = \frac{1}{\sqrt{2}} \begin{bmatrix}1 & \phantom{-}1 \\ 1 & -1  \end{bmatrix} \ .
$$

Essa matriz é conhecida em Computação Quântica como *matriz de Hadamard*, e costuma ser denotada por $H$. Portanto

$$
H = [I]^\mathcal{I}_\mathcal{X} = \frac{1}{\sqrt{2}} \begin{bmatrix}1 & \phantom{-}1 \\ 1 & -1  \end{bmatrix} \ .
$$

Também vale que a matriz de mudança de base de $\mathcal{X}$ para $\mathcal{I}$ é $H$, visto que

$$
HH = I  \implies H^{-1} = H \implies [I]_\mathcal{I}^\mathcal{X} = \big([I]^\mathcal{I}_\mathcal{X} \big)^{-1} = H^{-1} = H \ .
$$

Então:

$$
\begin{array}{l}
  H\ket{0} = \ket{+} \\
  H\ket{1} = \ket{-}
  \end{array}
  \quad \quad
  \begin{array}{l}
  H\ket{+} = \ket{0} \\
  H\ket{-} = \ket{1}
\end{array} \ .
$$
:::

## Produto Interno, Norma e Produto Exterior

### Produto Interno

O espaço vetorial $\mathbb{C}^n$ admite o seguinte *produto interno*:

$$
\big( \ket{\phi} , \ket{\psi} \big) = \braket{\phi | \psi} = \begin{bmatrix}w_0^{\ *} & w_1^{\ *} & \cdots & w_{n-1}^{\ *}\end{bmatrix} \cdot \begin{bmatrix}z_0 \\ z_1 \\ \vdots \\ z_{n-1}\end{bmatrix} = \sum_{k=0}^{n-1} w_k^{\ *} z_k \ \ \ ,
$$

para $\ket{\phi} = \begin{bmatrix}w_0 \\ \vdots \\ w_{n-1}\end{bmatrix}$ e $\ket{\psi} = \begin{bmatrix}z_0 \\ \vdots \\ z_{n-1}\end{bmatrix}$. Pode-se considerar o símbolo $\bra{\phi}$ de maneira independente, definindo-o como:

$$
\bra{\phi} = \ket{\phi}^\dagger = \begin{bmatrix}w_0 \\ \vdots \\ w_{n-1}\end{bmatrix}^\dagger =  \begin{bmatrix}w_0^{\ *} & w_1^{\ *} & \cdots & w_{n-1}^{\ *}\end{bmatrix} \ \ ,
$$

em que o símbolo $\dagger$ denota transposição e conjugação do vetor. Essa notação também será justificada posteriormente.

A operação definida acima satisfaz as propriedades que definem um produto interno de maneira geral:

- **(PI1)** Linearidade no segundo argumento:

  $$
  \big( \ket{\phi} , z_1\ket{\psi_1} + z_2 \ket{\psi_2} \big) = z_1 \big( \ket{\phi} , \ket{\psi_1} \big) + z_2 \big( \ket{\phi} , \ket{\psi_2} \big)
  $$

- **(PI2)** Antilinearidade no primeiro argumento:

  $$
  \big( z_1 \ket{\phi_1} + z_2 \ket{\phi_2} , \ket{\psi} \big) = z_1^{\ *} \big( \ket{\phi_1} , \ket{\psi} \big) + z_2^{\ *} \big( \ket{\phi_2} , \ket{\psi} \big)
  $$

- **(PI3)** Simetria hermitiana:

  $$
  \big( \ket{\phi} , \ket{\psi} \big)^* = \big( \ket{\psi} , \ket{\phi} \big)
  $$

- **(PI4)** Positividade:

  $$
  \big( \ket{\phi} , \ket{\phi} \big) \geq 0 \ \ \  \text{e} \ \ \ \big( \ket{\phi} , \ket{\phi} \big) = 0  \Leftrightarrow \ket{\psi} = 0
  $$

A propriedade (PI2) decorre de (PI1) e de (PI3), mas foi incluída na lista por completeza. Por causa das propriedades (PI1) e (PI2), o produto interno é dito ser *sesquilinear* (O prefixo *sesqui* significa "um e meio").

O espaço vetorial $\mathbb{C}^n$ é, pois, dito ser um *espaço vetorial com produto interno*, ou ainda, um *espaço de Hilbert*.

:::{tip}
Um espaço de Hilbert é definido como sendo um espaço vetorial com produto interno e com uma propriedade adicional chamada *completude*. Essa propriedade é automática para espaços de dimensão finita.
:::

:::{admonition} Exemplo
:class: tip

O produto interno dos vetores

$$
\ket{\phi} = \frac{i}{2} \ket{0} + \frac{\sqrt{3}}{2} \ket{1} = \begin{bmatrix} \frac{i}{2}\\ \frac{\sqrt{3}}{2}\end{bmatrix}  \ \text{ e } \  \ket{\psi} = \frac{1}{\sqrt{2}} \ket{0} + \frac{-i}{\sqrt{2}} \ket{1} = \begin{bmatrix}\frac{1}{\sqrt{2}}\\ \frac{-i}{\sqrt{2}} \end{bmatrix}
$$

é dado por:

$$
\begin{array}{rcl}
  \braket{\phi | \psi}
  &=& \left( \frac{-i}{2} \bra{0} + \frac{\sqrt{3}}{2} \bra{1} \right) \left( \frac{1}{\sqrt{2}} \ket{0} + \frac{-i}{\sqrt{2}} \ket{1} \right)  \\
  &=&
  \frac{-i}{2\sqrt{2}} \braket{0 | 0} + \frac{-i^2}{2\sqrt{2}} \braket{0 | 1} + \frac{\sqrt{3}}{2\sqrt{2}} \braket{1 | 0} + \frac{-i\sqrt{3}}{2\sqrt{2}} \braket{0 | 0} \\
  &=&
  \frac{-i}{2\sqrt{2}} + 0 + 0 + \frac{-i\sqrt{3}}{2\sqrt{2}} = -i\frac{1+\sqrt{3}}{2\sqrt{2}} \ .
\end{array}
$$

Esse produto interno também pode ser calculado de maneira matricial:

$$
\begin{array}{rcl}
  \braket{\phi | \psi}
  &=&  \begin{bmatrix} \frac{i}{2}\\ \frac{\sqrt{3}}{2}\end{bmatrix}^\dagger \cdot \begin{bmatrix}\frac{1}{\sqrt{2}}\\ \frac{-i}{\sqrt{2}} \end{bmatrix} \\
  &=&   \begin{bmatrix} \frac{i}{2}^{*}  & \frac{\sqrt{3}}{2}^{*}\end{bmatrix} \cdot \begin{bmatrix}\frac{1}{\sqrt{2}}\\ \frac{-i}{\sqrt{2}} \end{bmatrix}   \\
  &=& \begin{bmatrix} \frac{-i}{2}  & \frac{\sqrt{3}}{2}\end{bmatrix} \cdot \begin{bmatrix}\frac{1}{\sqrt{2}}\\ \frac{-i}{\sqrt{2}} \end{bmatrix}   \\
  &=&  \frac{-i}{2\sqrt{2}} + \frac{-i\sqrt{3}}{2\sqrt{2}}
\end{array}
$$

:::

:::{admonition} Exercício
:class: tip

Considere:

$$
a = \frac{3+i\sqrt{3}}{4}\ket{0}+\frac{1}{2}\ket{1}
$$

$$
b = \frac{1}{4}\ket{0}+\frac{\sqrt{15}}{4}\ket{1}
$$

(a) Encontre $\braket{a | b}$

(b) Encontre $\braket{b | a}$ 

(c) Qual a relação entre os resultados obtidos?
:::

:::{admonition} Exercício
:class: tip

Escreva uma função em Python que receba dois vetores dados por uma lista ou tuple e retorne o produto interno entre eles na notação de matriz coluna e na notação de Dirac

:::

### Norma

A *norma*, ou *tamanho*, de um vetor é definida por

$$
||{\ket\psi}|| = \sqrt{\braket{\psi}} \geq 0,
$$

operação bem definida pois $\braket{\psi}$ é real e não-negativo. Por consequência da propriedade (P4), tem-se $||{\ket{\psi}}|| = 0 \Leftrightarrow \ket{\psi} = 0$. Um vetor *normalizado* é um vetor de tamanho unitário, e a operação de *normalização* consiste em multiplicar o vetor $\ket{\psi}$ por $\frac{1}{||{\ket{\psi}}||}$ para que o vetor resultante $\frac{\ket{\psi}}{||{\ket{\psi}}||}$ tenha norma 1.

(cap2ex-base-comp-norma-1)=

:::{admonition} Exemplo
:class: tip

Os vetores $\ket{0}$, $\ket{1}$, $\ket{+}$ e $\ket{-}$ têm norma 1.
:::

:::{admonition} Exemplo
:class: tip

A norma do vetor $\ket{\psi} = \frac{i}{2} \ket{0} + \frac{\sqrt{3}}{2} \ket{1}$ é

$$
||{\ket{\psi}}|| =  \sqrt{\left|{\frac{i}{2}}\right|^2 + \left|{\frac{\sqrt{3}}{2}} \right|^2}  = \sqrt{\frac{1}{4} + \frac{3}{4}} = 1 \ .
$$
:::

### Ortogonalidade

De forma análoga com o que se passa com vetores no $\mathbb{R}^3$, dois vetores $\ket{\phi}$ e $\ket{\psi}$ são ditos *ortogonais* se o produto interno entre eles é nulo. Em símbolos, $\ket{\phi} \perp \ket{\psi} \ \Leftrightarrow \ \braket{\phi | \psi} = 0$.

(cap2ex-ortogonalidade-base-comp)=

:::{admonition} Exemplo
:class: tip

Os vetores $\ket{0}$ e $\ket{1}$ são ortogonais:

$$
\braket{0 | 1} = \begin{bmatrix}1 & 0 \end{bmatrix} \cdot \begin{bmatrix}0 \\ 1\end{bmatrix} = 0 \ .
$$
:::

(cap2ex-ortogonalidade-base-x)=

:::{admonition} Exemplo
:class: tip

Os vetores $\ket{+} =  \frac{1}{\sqrt{2}} \ket{0} +  \frac{1}{\sqrt{2}} \ket{1}$ e $\ket{-} =  \frac{1}{\sqrt{2}} \ket{0} -  \frac{1}{\sqrt{2}} \ket{1}$ são ortogonais:

$$
\begin{array}{rcl}
\braket{+ | -}
&=& \left( \frac{1}{\sqrt{2}} \bra{0} +  \frac{1}{\sqrt{2}} \bra{1} \right) \left( \frac{1}{\sqrt{2}} \ket{0} - \frac{1}{\sqrt{2}} \ket{1} \right) \\
&=& \frac{1}{2} \braket{0 | 0} - \frac{1}{2} \braket{0 | 1} + \frac{1}{2} \braket{1 | 0}  - \frac{1}{2} \braket{1 | 1} \\
&=& \frac{1}{2} - 0 + 0 - \frac{1}{2} = 0 \ .
\end{array}
$$

:::

(cap2base-ortonormal)=

### Base Ortonormal

Uma base em que todos os vetores são ortogonais dois a dois e têm tamanho 1 é dita ser *base ortonormal*. Se $\beta = \{\ket{b_0}, \ldots, \ket{b_{n-1}} \}$ é uma tal base, vale a chamada *relação de ortogonalidade*

$$
\braket{b_k | b_l} = \delta_{k,l} = \left\lbrace \begin{matrix} 1 \ , \text{ se } k=l \\ 0 \ , \text{ se } k\neq l \end{matrix}\right. \ \ ,
$$

em que $\delta_{k,l}$ é conhecido como *delta de Kronecker*, e vale 1 se e somente se os seus dois índices são iguais; se forem diferentes, vale 0.

Um vetor $\ket{\psi}$ pode ser escrito como combinação linear dos vetores da base $\beta$ por $\ket{\psi} = \sum_k a_k \ket{b_k}$. Os coeficientes $a_k$ podem ser encontrados de maneira simples quando a base é ortonormal. Aplicando-se o produto interno em ambos os lados, tem-se

$$
\braket{b_l | \psi} = \bra{b_l} \left( \sum_k a_k \ket{b_k} \right) = \sum_k a_k \braket{b_l | b_k} = \sum_k a_k \delta_{l,k} = a_l \ .
$$

Percebe-se que isso é análogo à decomposição de um vetor $\vec{v} \in \mathbb{R}^3$ nas suas componentes $x$, $y$ e $z$ na base canônica. Nesse caso, as componentes do vetor são dadas por $v_x = \hat{x} \cdot \vec{v}$, $v_y = \hat{y} \cdot \vec{v}$ e $v_z = \hat{z} \cdot \vec{v}$, em que $\cdot$ denota o produto interno no $\mathbb{R}^3$.

Portanto, os coeficientes do vetor $\ket{\psi}$ na base ortonormal são obtidos realizando-se projeções de  $\ket{\psi}$ na direção dos vetores unitários $\ket{b_l}$ da base ortonormal. Assim:

$$
\ket{\psi} = \sum_k \braket{b_k | \psi} \ket{b_k} \ \  \Leftrightarrow \ \ \big[ \ket{\psi} \big]_\beta = \begin{bmatrix} \braket{b_0 | \psi}\\ \vdots \\ \braket{b_{n-1}}{\psi}\end{bmatrix}_\beta \ .
$$

:::{admonition} Exemplo
:class: tip

A base $\ket{0}$, $\ket{1}$ é ortonormal, em consequência dos exemplos [Normal 1](cap2ex-base-comp-norma-1) e [Ortogonalidade da Base Computacional](cap2ex-ortogonalidade-base-comp). As projeções de um vetor $\ket{\psi} = a_0 \ket{0} + a_1 \ket{1}$ na base computacional são dadas por

$$
\begin{array}{rcl}
a_0 &=& \braket{0 | \psi} \\
a_1 &=& \braket{1 | \psi}
\end{array}
$$

e o vetor $\ket{\psi}$ pode ser escrito como

$$
\ket{\psi} = \braket{0 | \psi} \ket{0} + \braket{1 | \psi} \ket{1} \ .
$$
:::

:::{admonition} Exemplo
:class: tip

A base $\ket{+}$, $\ket{-}$ é ortonormal em consequência dos exemplos [Norma 1](cap2ex-base-comp-norma-1) e [Ortogonalidade da Base X](cap2ex-ortogonalidade-base-x). Os coeficientes do vetor $\ket{\psi} = \frac{1}{2} \left( \ket{0} + i \sqrt{3} \ket{1} \right)$ na base $\mathcal{X}$ são dados por:

$$
\begin{array}{rcl}
  a_0
  &=& \braket{+ | \psi} \\
  &=& \frac{1}{\sqrt{2}} \ \frac{1}{2} \left( \bra{0} + \bra{1} \right) \left(  \ket{0} + i \sqrt{3} \ket{1} \right) \\
  &=& \frac{1}{2\sqrt{2}} (1 + i\sqrt{3} )
\end{array}
$$

$$
\begin{array}{rcl}
  a_1
  &=& \braket{- | \psi} \\
  &=& \frac{1}{\sqrt{2}} \ \frac{1}{2} \left( \bra{0} - \bra{1} \right) \left(  \ket{0} + i \sqrt{3} \ket{1} \right) \\
  &=& \frac{1}{2\sqrt{2}} (1 - i\sqrt{3} )
\end{array}
$$

Portanto,

$$
\ket{\psi} = \braket{+ | \psi} \ket{+} + \braket{- | \psi} \ket{-} = \frac{1 + i\sqrt{3}}{2\sqrt{2}} \ket{+} + \frac{1 - i\sqrt{3}}{2\sqrt{2}} \ket{-} \ .
$$

:::

### Desigualdade de Cauchy-Schwarz

Há uma desigualdade envolvendo normas de vetores que é válida de maneira geral, para quaisquer espaços vetoriais equipados com produto interno e norma. É conhecida por *desigualdade de Cauchy-Schwarz*.

:::{admonition} Desigualdade de Cauchy-Schwarz
:class: seealso

Dados $\ket{u}, \ket{v} \in V$, com $V$ um espaço vetorial qualquer munido de produto interno e norma, vale que

$$
|{\braket{u | v}}| \leq ||\ {\ket{u}}||\  ||\ {\ket{v}}|| \ .
$$

A igualdade ocorre se e somente se os vetores $\ket{u}$ e $\ket{v}$ forem múltiplos um do outro.

**Demonstração.** Considere o vetor $a\ket{u} - b\ket{v}$. O produto interno desse vetor consigo mesmo deve ser real e não-negativo, por propriedade do produto interno, portanto

$$
\begin{split}
 0
 &\leq \big( a^{*}\bra{u} - b^{*}\bra{v} \big) \big(a \ket{u} - b \ket{v} \big) \\
 &= |{a}|^2\braket{u | u} - a^{*}b\braket{u | v} - a b^{*} \braket{v | u} + |{b}|^2\braket{v | v} \ . \\
\end{split}
$$

Escolhendo $a = \braket{v | v}$ e $b = \braket{v | u}$, tem-se

$$
\begin{split}
  0
  &\leq  |{a}|^2\braket{u | u} - a^{*}b\braket{u | v} - a b^{*} \braket{v | u}  + |{b}|^2\braket{v | v} \\
  &=   |{\braket{v | v}}|^2\braket{u | u} - \braket{v | v} \braket{v | u} \braket{u | v} - \braket{v | v} \braket{u | v} \braket{v | u}  + |{\braket{v | u}}|^2\braket{v | v} \\
  &=   \braket{v | v}^2\braket{u | u} - 2 \braket{v | v} \braket{u | v} \braket{v | u}  + |{\braket{u | v}}|^2\braket{v | v} \\
  &=   \braket{v | v}^2\braket{u | u} - 2 \braket{v | v} |{ \braket{u | v}}|^2   + |{\braket{u | v}}|^2 \braket{v | v}
\end{split}
$$

Logo, obtém-se

$$
\begin{split}
    &0
    \leq
    \braket{u | u} \braket{v | v} -  |{ \braket{u | v}}|^2 \\
  &\implies  |{ \braket{u | v}}| \leq \sqrt{\braket{u | u} \braket{v | v}} \\
  & \implies |{ \braket{u | v}}| \leq ||{\ket{u}}|| ||{\ket{v}}|| \ ,
\end{split}
$$

e fica provada a desigualdade.

Ocorre igualdade se e somente se ocorrer igualdade em $0 \leq \big( a^{*}\bra{u} - b^{*}\bra{v} \big) \big(a \ket{u} - b \ket{v} \big)$, isto é, se e somente se o vetor $a \ket{u} - b \ket{v}$ for nulofootnote{Isso é devido à propriedade (PI4) do produto interno.}. Portanto deve-se ter um dos vetores $\ket{u}$, $\ket{v}$ múltiplo do outro.
:::

No espaço vetorial $\mathbb{R}^n$ essa desigualdade permite definir o conceito de ângulo entre dois vetores por meio da relação $\cos \theta = \frac{\overrightarrow{u} \cdot \overrightarrow{v}}{||{\overrightarrow{u}||} ||{\overrightarrow{v}}}||$. No caso de interesse para o presente trabalho, o do espaço vetorial $\mathbb{C}^n$, essa interpretação não é possível pois o produto interno pode assumir um valor complexo.

### Matriz de Mudança de Base entre Bases Ortonormais

Da mesma forma que em [Matriz de Mudança de Base](cap2matriz-de-mudanca-de-base), é possível escrever uma matriz que faz a mudança de base entre duas bases ortonormais $\beta_{\text{old}} = \big\{\ket{u_0}, \ldots, \ket{u_{n-1}} \big\}$ e $\beta_{\text{new}} = \big\{ \ket{v_0}, \ldots, \ket{v_{n-1}} \big\}$. As colunas da matriz de mudança de base são os vetores da base nova escritos como combinação linear dos vetores da base antiga. Como as bases são ortonormais, esses coeficientes podem ser obtidos pela projeção na direção dos vetores da base, como descrito na seção [Base Ortonormal](cap2base-ortonormal).

A matriz de mudança de base, nesse caso, é dada por

$$
\begin{array}{rcl}
[I]^{\beta_{\text{old}}}_{\beta_{\text{new}} }
&=&
      \begin{bmatrix} \Big| & \Big| & & \Big|
      \\ \big[\ket{v_0}\big]_{\beta_{\text{old}}} &  \big[\ket{v_1}\big]_{\beta_{\text{old}}} & \cdots & \big[\ket{v_{n-1}}\big]_{\beta_{\text{old}}} \\
        \Big| & \Big| & & \Big| \end{bmatrix} \\ \\
&=&
\begin{bmatrix} \braket{u_0 | v_0} & \braket{u_0 | v_1}& \ \cdots \  & \braket{u_0 | v_{n-1}} \\
      \braket{u_1 | v_0} & \braket{u_1 | v_1}& \cdots & \braket{u_1 | v_{n-1}} \\
      \vdots & \vdots & \ddots  & \vdots \\
      \braket{u_{n-1}}{v_0} & \braket{u_{n-1}}{v_1}& \cdots & \braket{u_{n-1}}{v_{n-1}}   \end{bmatrix}
\ .
\end{array}
$$

A matriz de mudança de base satisfaz $[I]^{\beta_{\text{old}}}_{\beta_{\text{new}} }\phantom{\big{|}}^{-1} = [I]^{\beta_{\text{old}}}_{\beta_{\text{new}} }\phantom{\big{|}}^{\dagger} = [I]^{\beta_{\text{new}}}_{\beta_{\text{old}} }$.

Isso significa que a matriz de mudança de base é *unitária*, um assunto que será visto na seção [Operadores Unitários](cap2operadores-unitarios).

:::{admonition} Exemplo
:class: tip

Sabendo que as bases $\mathcal{I}$ e $\mathcal{X}$ são ortonormais, pode-se encontrar a matriz de mudança de base fazendo as seguintes contas.

$$
\begin{array}{rcl}
\braket{0 | +} &=& \bra{0} \left( \frac{1}{\sqrt{2}}\ket{0} +  \frac{1}{\sqrt{2}}\ket{0} \right) =  \frac{1}{\sqrt{2}} \\
\braket{1 | +} &=& \bra{1} \left( \frac{1}{\sqrt{2}}\ket{0} +  \frac{1}{\sqrt{2}}\ket{0} \right) =  \frac{1}{\sqrt{2}} \\ \\
\braket{0 | -} &=& \bra{0} \left( \frac{1}{\sqrt{2}}\ket{0} -  \frac{1}{\sqrt{2}}\ket{0} \right) =  \frac{1}{\sqrt{2}} \\
\braket{1 | -} &=& \bra{1} \left( \frac{1}{\sqrt{2}}\ket{0} -  \frac{1}{\sqrt{2}}\ket{0} \right) = - \frac{1}{\sqrt{2}} \\
\end{array}
$$

Portanto, a matriz de mudança de base de $\mathcal{I}$ para $\mathcal{X}$ é dada por:

$$
[I]^\mathcal{I}_\mathcal{X} = \begin{bmatrix} \braket{0 | +} & \braket{0 | -} \\ \braket{1 | +} & \braket{1 | -} \end{bmatrix} = \frac{1}{\sqrt{2}} \begin{bmatrix} 1 & \phantom{-}1 \\ 1 & -1 \end{bmatrix}  = H \ .
$$

Esse é o mesmo resultado obtido no exemplo [Matrix Mudança de Base](cap2ex-matrix-mudanca-de-base).
:::

### Produto Exterior

É possível dar um significado ao símbolo $\bra{\phi}$ como sendo um vetor linha. Isso permite, pois, considerar-se o produto matricial $\ket{\psi} \cdot \bra{\phi} = \ket{\psi}\bra{\phi}$ de um vetor linha $n\times 1$ por um vetor coluna $1 \times n$, resultando em uma matriz $n \times n$. Essa operação é chamada de *produto exterior*.

:::{admonition} Exemplo
:class: tip

No espaço vetorial de 1 qubit, alguns exemplos de produto exterior são:

$$
\begin{array}{rcl}
  \ket{0}\bra{0} &=& \begin{bmatrix} 1 \\ 0 \end{bmatrix} \cdot \begin{bmatrix} 1 & 0 \end{bmatrix} = \begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix}  \\
  \ket{0}\bra{1} &=& \begin{bmatrix} 1 \\ 0 \end{bmatrix} \cdot \begin{bmatrix} 0 & 1 \end{bmatrix} = \begin{bmatrix} 0 & 1 \\ 0 & 0 \end{bmatrix}  \\
  \ket{1}\bra{0} &=& \begin{bmatrix} 0 \\ 1 \end{bmatrix} \cdot \begin{bmatrix} 1 & 0 \end{bmatrix} = \begin{bmatrix} 0 & 0 \\ 1 & 0 \end{bmatrix}  \\
  \ket{1}\bra{1} &=& \begin{bmatrix} 0 \\ 1 \end{bmatrix} \cdot \begin{bmatrix} 0 & 1 \end{bmatrix} = \begin{bmatrix} 0 & 0 \\ 0 & 1 \end{bmatrix}
\end{array}
$$

$$
\begin{array}{rcl}
  \ket{+}\bra{0} &=& \begin{bmatrix} \tfrac{1}{\sqrt{2}} \\ \tfrac{1}{\sqrt{2}} \end{bmatrix} \cdot \begin{bmatrix} 1 & 0 \end{bmatrix} = \begin{bmatrix} \tfrac{1}{\sqrt{2}} & 0 \\ \tfrac{1}{\sqrt{2}} & 0 \end{bmatrix}  \\
  \ket{+}\bra{-} &=& \begin{bmatrix} \tfrac{1}{\sqrt{2}} \\ \tfrac{1}{\sqrt{2}} \end{bmatrix} \cdot \begin{bmatrix} \tfrac{1}{\sqrt{2}} & -\tfrac{1}{\sqrt{2}} \end{bmatrix} = \begin{bmatrix} \tfrac{1}{2} & -\tfrac{1}{2} \\ \tfrac{1}{2}  & -\tfrac{1}{2}  \end{bmatrix}
\end{array}
$$
:::

