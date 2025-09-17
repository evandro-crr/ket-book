(produto-tensorial)=
# Produto Tensorial

É possível compor dois espaços vetoriais para formar um terceiro espaço. Uma maneira de fazer isso é por meio do *produto tensorial*. Em Computação Quântica, essa construção é fundamental para se trabalhar com sistemas compostos por mais de um qubit. Um sistema de dois qubits será o produto tensorial de dois espaços $\mathbb{C}^2$, que modelam um qubit.

## Espaço Vetorial do Produto Tensorial

Dados dois espaços vetorias $V$ e $W$, com bases $\beta_V = \{ \ket{v_k} \}$ e $\beta_W = \{ \ket{w_l} \}$, o *produto tensorial* de $V$ e $W$, denotado por $V\otimes W$, é definido como o espaço vetorial gerado pela base:

$$
v_k \otimes w_l \ , \ \ \begin{matrix} k=0 , \ldots , \dim V - 1 \\  l=0 , \ldots , \dim W - 1 \end{matrix} \ .
$$

A dimensão do espaço vetorial do produto tensorial é, portanto,

$$
\dim V\otimes W = \dim V \cdot \dim W \ .
$$

O produto tensorial $\otimes$ forma uma dupla ordenada com propriedades diferentes das do produto cartesiano. Essas propriedades, listadas abaixos, são chamadas conjuntamente de *bilinearidade*:

- Para todos $z \in \mathbb{C}$, $\ket{v}\in V$ e $\ket{w} \in W$,

  $$
  z \cdot (\ket{v} \otimes \ket{w}) = (z\ket{v}) \otimes \ket{w} = \ket{v} \otimes(z\ket{w}) \ .
  $$

- Para todos  $\ket{v^1},\ket{v^2}\in V$ e $\ket{w} \in W$,

  $$
  (\ket{v^1}+ \ket{v^2}) \otimes \ket{w} = \ket{v^1} \otimes \ket{w} + \ket{v^2} \otimes \ket{w} \ .
  $$

- Para todos $\ket{v}\in V$ e $\ket{w^1},\ket{w^2} \in W$,

  $$
  \ket{v} \otimes (\ket{w^1} + \ket{w^2}) = \ket{v} \otimes \ket{w^1} + \ket{v} \otimes \ket{w^2} \ .
  $$

Um elemento genérico do espaço $V\otimes W$ é uma combinação linear dos vetores da base $\ket{v_k} \otimes \ket{w_l}$. Em geral, essa combinação não pode ser escrita da forma fatorada $\ket{v} \otimes \ket{w}$.

(cap2ex-espaco-vet-2qubits)=

:::{admonition} Exemplo
:class: tip

O sistema composto por 2 qubits é dado pelo produto tensorial de dois espaços vetoriais de 1 qubit. Esse espaço vetorial é denotado por $\mathbb{C}^2 \otimes \mathbb{C}^2$. A base desse espaço é formada pelos 4 vetores

$$
\begin{array}{rcl}
\ket{00} &=& \ket{0} \ket{0} = \ket{0} \otimes \ket{0} \\
\ket{01} &=& \ket{0} \ket{1} = \ket{0} \otimes \ket{1} \\
\ket{10} &=& \ket{1} \ket{0} = \ket{1} \otimes \ket{0} \\
\ket{11} &=& \ket{1} \ket{1} = \ket{1} \otimes \ket{1} \ ,
\end{array}
$$

e as igualdades apresentadas acima apenas referem-se a notações alternativas e mais compactas. A ordem em que as entradas aparecem no produto tensorial é importante, de forma que $\ket{01} \neq \ket{10}$, por exemplo.

Um vetor qualquer $\ket{\psi} \in \mathbb{C}^2 \otimes \mathbb{C}^2$ pode ser escrito como

$$
\ket{\psi} = a \ket{00} + b\ket{01} + c \ket{10} + d\ket{11} \ ,
$$

com $a,b,c,d \in \mathbb{C}$. Alguns exemplos de vetores pertencentes ao espaço em questão são:

$$
\frac{\ket{00} + \ket{11}}{\sqrt{2}}
$$

$$
\ket{0} \otimes \left(\ket{0} + 2\ket{1} \right) = \ket{00} + 2 \ket{01}
$$

$$
\left( 5\ket{1}\right)   \ket{1}  =  5 \ket{11}
$$

$$
\left(\frac{1}{\sqrt{2}}\ket{0} - \frac{i}{\sqrt{2}} \right) \ket{0} = \frac{1}{\sqrt{2}}\ket{00} - \frac{i}{\sqrt{2}}\ket{10} \ .
$$

As igualdades acima são exemplos da bilinearidade do produto tensorial.
:::

## Comparação do Produto Tensorial com o Produto Cartesiano

O *produto cartesiano*, às vezes chamado *soma direta* é outra maneira de se compor dois espaços vetoriais em um espaço "maior", denotado por $V \times W$ ou por $V \oplus W$. O produto cartesiano é formado por duplas $\big( \ket{v} , \ket{w} \big)$, com $\ket{v} \in V$ e $\ket{w} \in W$. Nesta subseção, a notação $( \cdot \, , \cdot )$ refere-se a par ordenado em vez de produto interno como no restante do texto.

As diferenças entre essas duas operações estão dispostas no que segue:

```{csv-table} Tabela comparativa entre produto tensorial e produto cartesiano (também chamado soma direta)
:delim: '&'
:header-rows: 1

& Produto Tensorial & Produto Cartesiano ou Soma Direta
Notação: &  $V \otimes W$ & $V \times W = V \oplus W$
Base: & $\ket{v_k} \otimes \ket{w_l}$  &   $\big( \ket{v_k} , 0 \big) \ , \ \big( 0 , \ket{w_l} \big)$
Dimensão: & $\dim V \otimes W = \dim V \cdot \dim W$ &   $\dim V \oplus W = \dim V + \dim W$
```

Outra diferença é que a soma, no produto cartesiano, é uma soma entrada a entrada

$$
\big( \ket{v^1} , \ket{w^1} \big) + \big( \ket{v^2} , \ket{w^2} \big) = \big( \ket{v^1} + \ket{v^2} , \ket{w^1} + \ket{w^2} \big) \ ,
$$

enquanto que a soma no produto tensorial, de modo geral, não se reduz

$$
\ket{v^1} \otimes \ket{w^1}  +  \ket{v^2} \otimes \ket{w^2}  \ ,
$$

a não ser que, por exemplo, $\ket{v^1} = \ket{v^2}$, de modo que

$$
\ket{v^1} \otimes \ket{w^1}  +  \ket{v^1} \otimes \ket{w^2} = \ket{v^1} \otimes \big( \ket{w^1}  + \ket{w^2} \big) \ .
$$

A multiplicação por escalar no produto cartesiano também é entrada a entrada

$$
z \cdot \big( \ket{v} , \ket{w} \big) = \big( z\ket{v} , z\ket{w} \big) \ ,
$$

enquanto que, no produto tensorial, o escalar pode ser incorporado a qualquer das duas entradas, mas deve ir para apenas uma delas

$$
z \cdot \big(\ket{v} \otimes \ket{w}\big) = \big(z\ket{v}\big) \otimes \ket{w} = \ket{v} \otimes \big(z\ket{w} \big) \ .
$$

## Produto Interno

Sejam $V$ e $W$ espaços de Hilbert, isto é, espaços munidos de produto interno. O produto tensorial $V\otimes W$ pode ser munido com um produto interno derivado dos produtos internos de $V$ e de $W$. Defina:

(cap2def-produto-interno-vetores-da-base)=

$$
\begin{array}{rcl}
  \Big( \ket{v_k}\otimes \ket{w_l} , \ket{v_{k^\prime}}\otimes \ket{w_{l^\prime}} \Big)
&=&  \Big( \ket{v_k} , \ket{v_{k^\prime}} \Big)_V \cdot \Big( \ket{w_l} , \ket{w_{l^\prime}} \Big)_W  \nonumber \\
&=& \braket{v_k | v_{k^\prime}}  \cdot \braket{w_l | w_{l^\prime}} =  \delta_{k,k\prime} \delta_{l,l^\prime} \ , \quad \quad \quad
\end{array}
$$

estendendo a definição para elementos arbitrários do produto tensorial por linearidade na segunda entrada e antilinearidade na primeira.

Para dois vetores da forma $\ket{v^1}\otimes \ket{w^1}$ e $\ket{v^2}\otimes \ket{w^2}$ do produto tensorial, pode-se denotar

$$
\Big( \ket{v^1}\otimes \ket{w^1} ,   \ket{v^2}\otimes \ket{w^2} \Big) = \big( \bra{v^1}\otimes \bra{w^1} \big) \big(  \ket{v^2}\otimes \ket{w^2} \big) \ ,
$$

e decorre da definição de produto interno que

$$
\big( \bra{v^1}\otimes \bra{w^1} \big) \big(  \ket{v^2}\otimes \ket{w^2} \big) = \braket{v^1 | v^2}_V  \cdot \braket{w^1 | w^2}_W \ .
$$

:::{admonition} Exemplo
:class: tip

O espaço vetorial $\mathbb{C}^2 \otimes \mathbb{C}^2$ que descreve 2 qubits foi apresentado no exemplo [Espaço Vetorial de 2 Qubits](cap2ex-espaco-vet-2qubits). O produto interno nesse espaço é explicitado no que segue.
Use os índices $A$ e $B$ para fazer referência à primeira e à segunda entrada tensorial, respectivamente.

O produto interno dos vetores da base é dado pela equação [Produto Interno de Vetores da Base](cap2def-produto-interno-vetores-da-base), que se traduz em

$$
\begin{array}{rcl}
\braket{jk | pq}_{AB}
&=& \big( \ket{jk} , \ket{pq} \big)_{AB} \\
&=& \big(\ket{j},\ket{p} \big)_A \cdot \big( \ket{k},\ket{q} \big)_B \\
&=& \braket{j | p}_A \cdot \braket{k | q}_B \\
&=& \delta_{j,p} \cdot \delta_{k,q}  = \delta_{jk,pq} \ ,
\end{array}
$$

em que $j,k,p,q = 0,1$. Por exemplo,

$$
\text{$\braket{01 | 01} = 1$, $\braket{11 | 10} = 0$ e $\braket{10 | 01} = 0$ .}
$$

Sejam

$$
\begin{array}{rcl}
    \ket{\phi} &=& a_1 \ket{00} + b_1 \ket{01} + c_1 \ket{10} + d_1 \ket{11} \\
    \ket{\psi} &=& a_2 \ket{00} + b_2 \ket{01} + c_2 \ket{10} + d_2 \ket{11} \ .
\end{array}
$$

O produto interno de $\ket{\phi}$ com $\ket{\psi}$ é dado por

$$
\begin{array}{rcl}
\braket{\phi | \psi}
&=& \big(a_1^{\ *} \bra{00} + b_1^{\ *} \bra{01} + c_1^{\ *} \bra{10} + d_1^{\ *} \bra{11}\big) \big(a_2 \ket{00} + b_2 \ket{01} + c_2 \ket{10} + d_2 \ket{11} \big) \\
& =&  a_1^{\ *} a_2 + b_1^{\ *} b_2 + c_1^{\ *} c_2 + d_1^{\ *} d_2 \ .
\end{array}
$$

A norma de $\ket{\phi}$ é dada por

$$
||{\ket{\phi}||} = \sqrt{|{a_1}|^2 + |{b_1}|^2 + |{c_1}|^2 + |{d_1}|^2}\  \ .
$$

Exemplos:

$$
\begin{split}
& \left( \frac{\bra{0} + \bra{1}}{\sqrt{2}} \right)_{A} \bra{1}_{B}\  \ket{0}_A \left(\frac{\ket{0}-i\ket{1}}{\sqrt{2}} \right)_B \\
&\ = \ \  \left( \frac{\braket{0 | 0} + \braket{1 | 0}}{\sqrt{2}} \right)_A \left( \frac{\braket{1 | 0} -i \braket{1 | 1}}{\sqrt{2}} \right)_B \\
&\ = \ \  \frac{1+0}{\sqrt{2}} \cdot \frac{0 - i}{\sqrt{2}} = \frac{-i}{2}
\end{split}
$$

$$
||{\ket{01}|| + i \ket{10}} = \sqrt{|{1}|^2 + |{i}|^2} = \sqrt{2} \ .
$$
:::

## Operadores

Sejam $A$ um operador em $V$ e $B$ um operador em $W$. É possível definir um operador em $V\otimes W$, denotado por $A\otimes B$ de forma que

$$
(A \otimes B) (\ket{v} \otimes \ket{w}) = A\ket{v} \otimes B\ket{w} \ .
$$

Todo operador em $V \otimes W$ pode ser decomposto em uma combinação linear de operadores da forma apresentada anteriormente.

Pode-se mostrar que a composição, ou produto, de dois operadores $A \otimes B$ e $A' \otimes B'$ é dada por:

$$
(A \otimes B) (A' \otimes B') = AA' \otimes BB' \ .
$$

:::{admonition} Exemplo
:class: tip

Sejam $X$ e $H$ operadores no espaço de 1 qubit dados por

$$
\begin{array}{ll}
  \begin{matrix}
  X\ket{0} = \ket{1} \\
  X\ket{1} = \ket{0}
\end{matrix}
&
X = \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}
\\ & \\
  \begin{matrix}
  H\ket{0} = \frac{1}{\sqrt{2}} \ket{0} + \frac{1}{\sqrt{2}} \ket{1} \\
  H\ket{1} = \frac{1}{\sqrt{2}} \ket{0} - \frac{1}{\sqrt{2}} \ket{1}
\end{matrix}
&
H = \frac{1}{\sqrt{2}} \begin{bmatrix} 1 & 1 \\ 1 & -1 \end{bmatrix} \ .
\end{array}
$$

Esses operadores foram utilizados em vários dentre os exemplos anteriores.

O operador $H \otimes X$ atua no espaço de 2 qubits como no exemplo abaixo.

$$
\begin{split}
  &H\otimes X \big(\ket{0} \otimes (\ket{0} + i \ket{1} ) \big) \\
  &\ \ = H\ket{0} \otimes \big(X(\ket{0} + i \ket{1} ) \big) \\
  &\ \ = \left(\frac{\ket{0} + \ket{1}}{\sqrt{2}} \right) \otimes \big( \ket{1} + i \ket{0} \big) \\
  &\ \ = \frac{i}{\sqrt{2}}\ket{00} + \frac{1}{\sqrt{2}}\ket{01} + \frac{i}{\sqrt{2}}\ket{10} + \frac{1}{\sqrt{2}}\ket{11} \ .
\end{split}
$$

Se forem usados rótulos $1$ e $2$ para as entradas tensoriais, a conta do exemplo acima poderia ser reescrita como

$$
\begin{split}
  &H_1 X_2 \ket{0}_1  (\ket{0} + i \ket{1} )_2  \\
  &\ \ = H_1 \ket{0}_1  X_2(\ket{0} + i \ket{1} )_2 \\
  &\ \ = \left(\frac{\ket{0}_1 + \ket{1}_1}{\sqrt{2}} \right) \big( \ket{1}_2 + i \ket{0}_2 \big) \\
  &\ \ = \frac{i}{\sqrt{2}}\ket{00}_{12} + \frac{1}{\sqrt{2}}\ket{01}_{12} + \frac{i}{\sqrt{2}}\ket{10}_{12} + \frac{1}{\sqrt{2}}\ket{11}_{12} \ .
\end{split}
$$

Mais detalhes sobre a notação encontram-se na seção [Produto Tensorial: Notação](cap2produto-tensorial-notacao).
:::

## Produto de Kronecker

Até então, o conceito de produto tensorial foi apresentado de maneira abstrata. É possível abordar esse conceito de maneira matricial também. Fixadas bases para $V$ e $W$, os vetores $\ket{v}$ e $\ket{w}$ desses espaços podem ser representados como vetores coluna.
O vetor $\ket{v} \otimes \ket{w}$ também pode ser representado como vetor coluna fazendo-se o *produto de Kronecker*.

$$
\ket{v} \otimes \ket{w} = \begin{bmatrix} a_0 \\ a_1 \\ \vdots \\ a_{n-1} \end{bmatrix} \otimes \begin{bmatrix} b_0 \\ b_1 \\ \vdots \\ b_{m-1} \end{bmatrix} =  \begin{bmatrix} a_0 \ket{w} \\ a_1 \ket{w} \\ \vdots \\ a_{n-1} \ket{w} \end{bmatrix}  = \begin{bmatrix} a_0 b_0 \\ a_0 b_1 \\ \vdots \\ a_0 b_{m-1} \\ a_1 b_0 \\ a_1 b_1 \\ \vdots \\ a_{n-1} b_{m-1} \end{bmatrix}
$$

Essa operação é mais facilmente compreendida por meio de um exemplo.

:::{admonition} Exemplo
:class: tip

$$
\begin{bmatrix} 1 \\ 2 \end{bmatrix} \otimes \begin{bmatrix} 3 \\ 4 \\ 5 \end{bmatrix} = \begin{bmatrix} 1 \begin{bmatrix} 3 \\ 4 \\ 5 \end{bmatrix} \\ \\ 2 \begin{bmatrix} 3 \\ 4 \\ 5 \end{bmatrix} \end{bmatrix} = \begin{bmatrix} 3 \\ 4 \\ 5 \\ 6 \\ 8 \\ 10 \end{bmatrix}
$$
:::

O produto tensorial de operadores em $V$ e $W$ também pode ser obtido matricialmente por meio do produto de Kronecker.

$$
A \otimes B = \begin{bmatrix} a_{0,0} & \cdots & a_{0,n-1} \\ a_{1,1} & & a_{1,n-1} \\ \vdots & & \vdots \\ a_{n-1,0} & \cdots & a_{n-1,n-1} \end{bmatrix}  \otimes B = \begin{bmatrix} a_{0,0}B & \cdots & a_{0,n-1}B \\ a_{1,1}B & & a_{1,n-1}B \\ \vdots & & \vdots \\ a_{n-1,0}B & \cdots & a_{n-1,n-1}B \end{bmatrix}
$$

:::{admonition} Exemplo
:class: tip

$$
\begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix} \otimes \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix} = \begin{bmatrix} 0 \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix} & 1 \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix} \\ \\ 1 \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}  & 0 \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}  \end{bmatrix} = \begin{bmatrix} 0 & 0 & 1 & 2 \\ 0 & 0 & 3 & 4 \\ 1 & 2 & 0 & 0 \\ 3 & 4 & 0 & 0 \end{bmatrix}
$$
:::

O produto de Kronecker, em geral, não é comutativo.

Se $A \in M(m_A,n_A)$ e $B \in M(m_B, n_B)$, então a matriz $A \otimes B$ tem $m_Am_B$ linhas e $n_An_B$ colunas, ou seja, $A\otimes B \in M(m_Am_B,n_An_B)$. Uma forma geral de escrever o elemento $j,k$ da matriz $A\otimes B$ é

$$
( A\otimes B )_{j,k} = a_{\text{quoc}(j,m_B),\text{quoc}(k,n_B)}\  b_{\text{resto}(j,m_B),\text{resto}(k,n_B)} \ \ ,
$$

em que

$$
\begin{split}
  j &= 0 , 1 , \ldots , m_A m_B - 1 \\
  k &= 0 , 1 , \ldots , n_A n_B - 1
\end{split}
$$

e, para $x,y$ inteiros,

$$
\begin{split}
    \text{quoc}(x,y) \ \ &\text{é o quociente da divisão $x / y$} \\
    \text{resto}(x,y) \ \ &\text{é o resto da divisão $x / y$} \ .
\end{split}
$$

:::{admonition} Exemplo
:class: tip

$A_{2\times2}$ , $B_{3\times2}$. O elemento $4,2$ da matriz $A\otimes B$ pode ser obtido por:

$$
   (A \otimes B)_{4,2} = a_{\text{quoc}(4,3),\text{quoc}(2,2)}\  b_{\text{resto}(4,3),\text{resto}(2,2)} = a_{1,1} b_{1,0} \ .
$$

A matriz $A\otimes B*$ está representada abaixo, destacando-se o elemento $4,2$:


$$
A \otimes B = \begin{bmatrix} a_{0,0} B & a_{0,1} B \\ a_{1,0} B & a_{1,1} B \end{bmatrix} =   \begin{bmatrix} a_{0,0} \begin{bmatrix} b_{0,0} & b_{0,1} \\ b_{1,0} & b_{1,1} \\ b_{2,0} & b_{2,1} \end{bmatrix} & a_{0,1} \begin{bmatrix} b_{0,0} & b_{0,1} \\ b_{1,0} & b_{1,1} \\ b_{2,0} & b_{2,1} \end{bmatrix} \\ & \\ a_{1,0} \begin{bmatrix} b_{0,0} & b_{0,1} \\ b_{1,0} & b_{1,1} \\ b_{2,0} & b_{2,1} \end{bmatrix} & \boxed{a_{1,1}} \begin{bmatrix} b_{0,0} & b_{0,1} \\ \boxed{b_{1,0}} & b_{1,1} \\ b_{2,0} & b_{2,1} \end{bmatrix} \end{bmatrix}   \ .
$$
:::

## Produto Tensorial de Vários Espaços Vetoriais

O produto tensorial de vários espaços vetoriais segue a mesma ideia do caso de dois espaços, apresentado anteriormente. A dimensão será o produto das dimensões de cada espaço. O produto tensorial é associativo, então não é necessário usar parênteses num produto tensorial de vários espaços. Não é possível comutar os fatores do produto tensorial.

(cap2produto-tensorial-notacao)=

## Notação

Em situações práticas, costuma-se usar índices em cada fator do produto tensorial para evitar confusões. Também há variantes que deixam a notação mais curta. Alguns comentários a respeito dessas variantes são abordados nesta seção. Para tratar disso, considere um exemplo em $V\otimes W \otimes U$.

Pode-se denotar um elemento da forma $\ket{v} \otimes \ket{w} \otimes \ket{u}$ omitindo-se o símbolo $\otimes$: $\ket{v}  \ket{w}  \ket{u}$. Nesse caso, deve-se tomar cuidado para não confundir essa justaposição com o produto matricial; nas situações de interesse, normalmente o produto matricial não será possível e há menos risco de confusão.

Costuma-se atribuir índices aos fatores: $\ket{v} \otimes \ket{w} \otimes \ket{u} = \ket{v}_V \otimes \ket{w}_W \otimes \ket{u}_U  =  \ket{v}_V \ket{w}_W  \ket{u}_U$. Ainda, pode-se escrever esse elemento como: $\ket{v}_1 \ket{w}_2 \ket{u}_3$, ou $\ket{v \, w \, u}_{VWU}$, ou, ainda, qualquer notação equivalente, que evidencie a que espaço cada ket pertence. Com a identificação por índices, é possível até trocar a ordem em que são escritos; não deve ser confundido com a comutatividade dos fatores, que não é permitida em geral. Assim, pode-se escrever: $\ket{u}_3 \ket{w}_2 \ket{v}_1$.

Os bras também podem ser rotulados com índices. Por exemplo, escreve-se $\big( \ket{v}_1 \ket{w}_2 \ket{u}_3\big)^\dagger =  {}_1\bra{v} {}_2\bra{w} {}_3\bra{u}$, ou $\ket{v \, w \, u}_{VWU}^{\ \ \dagger} = {}_{VWU}\bra{v \, w \, u}$.

Considere, agora, os operadores da forma $A\otimes B\otimes C$, com $A$, $B$ e $C$ operadores nos espaços $V$, $W$ e $U$, respectivamente. É possível também atribuir índices nos operadores para lembrar em que espaço cada um deles atua. Por exemplo, pode-se denotar: $A_1\otimes B_2\otimes C_3$.

Há situações em que se deseja operar apenas em uma das entradas do produto tensorial. Assim, por exemplo, $A\ket{v} \otimes \ket{w}\otimes \ket{u} = A_1 \big( \ket{v} \otimes \ket{w}\otimes \ket{u} \big)$. Formalmente, $A_1 = A \otimes I \otimes I$, nesse caso. O produto (ou composição) dos operadores $A_1 B_2 C_3$ significa $(A\otimes I \otimes I) (I \otimes B \otimes I)(I \otimes I \otimes C) = AII \otimes IBI \otimes IIC = A\otimes B \otimes C$. Dessa forma, com os índices, pode-se escrever $A_1 B_2 C_3 = A \otimes B \otimes C$ sem perigo de confusão com o produto matricial de $A$, $B$ e $C$; Pode-se até mesmo trocar a ordem de como são escritos:
$B_2 A_1 C_3 = A\otimes B \otimes C$.

Outra notação bastante utilizada é quando se deseja realizar o produto tensorial entre $n$ cópias de um vetor $\ket{\psi}$. Define-se

$$
\ket{\psi}^{\otimes n} = \underbrace{\ket{\psi} \otimes \ket{\psi}}_{\text{$n$ vezes}} \ .
$$

Essa notação pode ser utilizada para bras e para operadores: $\bra{\psi}^{\otimes n}$, $A^{\otimes n }$. Também é possível usar uma notação análoga ao produtório para denotar, por exemplo,

$$
\bigotimes_{i=1}^{n} A_i \ket{0}_i = A_1 \ket{0}_1 \otimes \ldots \otimes A_n \ket{0}_n = A_1 \ldots A_n \ket{0\ldots 0} \ .
$$

Há, pois, diversas maneiras de se denotar os mesmos vetores ou operadores. Essa variedade é útil para permitir a escrita de expressões compactas em diversas situações em que o produto tensorial aparece.
