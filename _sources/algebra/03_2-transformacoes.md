# Transformações Lineares

## Transformações Lineares

### Transformação Linear e Operador Linear

Uma *transformação linear* é uma aplicação $T \colon \mathbb{C}^n \to \mathbb{C}^m$ que respeita a soma e a multiplicação por escalar, ou seja, tal que valem:

- **(TL1)** Preservação da soma:

  $$
  T(\ket{\phi} + \ket{\psi}) = T\ket{\phi} + T\ket{\psi}
  $$

- **(TL2)** Preservação do produto por escalar:

  $$
  T( z\ket{\psi} ) = z \cdot T\ket{\psi} \ .
  $$

Um *operador linear* é uma transformação linear $A \colon \mathbb{C}^n \to \mathbb{C}^n$ ($m=n$).

(cap2ex-verificar-transformacao-linear)=

:::{admonition} Exemplo
:class: tip

A função $H \colon \mathbb{C}^2 \to \mathbb{C}^2$ dada por

$$
H \left( a_0 \ket{0} + a_1 \ket{1} \right) = \frac{a_0 + a_1}{\sqrt{2}} \ket{0} + \frac{a_0-a_1}{\sqrt{2}}
$$

é uma transformação linear. De fato, as propriedades de transformação linear se verificam para $H$.

- **Preservação da soma:** Sejam $\ket{\phi} = a_0 \ket{0} + a_1 \ket{1}$ e $\ket{\psi} = b_0 \ket{0} + b_1 \ket{1}$.

  $$
  \begin{array}{rcl}
    H(\ket{\phi} + \ket{\psi})
    &=& H \left( a_0 \ket{0} + a_1 \ket{1} + b_0 \ket{0} + b_1 \ket{1} \right)  \\
    &=& H\left( (a_0 + b_0) \ket{0} + (a_1 + b_1) \ket{1} \right) \\
    &=& \frac{(a_0 + b_0) + (a_1 + b_1)}{\sqrt{2}} \ket{0} + \frac{(a_0 + b_0) - (a_1 + b_1)}{\sqrt{2}}   \\
    &=& \frac{a_0 + a_1}{\sqrt{2}} \ket{0} + \frac{a_0-a_1}{\sqrt{2}} + \frac{b_0 + b_1}{\sqrt{2}} \ket{0} + \frac{b_0-b_1}{\sqrt{2}}  \\
    &=& H \ket{\phi} + H \ket{\psi}
  \end{array}
  $$

- **Preservação do produto por escalar:** Sejam $z \in \mathbb{C}$ e $\ket{\psi} = a_0 \ket{0} + a_1 \ket{1}$.

  $$
  \begin{array}{rcl}
    H(z \ket{\psi})
    &=& H \big( z(a_0 \ket{0} + a_1 \ket{1}) \big) \\
    &=&  H \left( za_0 \ket{0} + za_1 \ket{1}) \right) \\
    &=& \frac{za_0 + za_1}{\sqrt{2}} \ket{0} + \frac{za_0-za_1}{\sqrt{2}} \\
    &=& z \left( \frac{a_0 + a_1}{\sqrt{2}} \ket{0} + \frac{a_0-a_1}{\sqrt{2}} \right) \\
  &=& z\cdot  H \ket{\psi}
  \end{array}
  $$
:::

### Funcional Linear

Um *funcional linear* é uma transformação linear $f \colon \mathbb{C}^n \to \mathbb{C}$ ($m=1$). O bra $\bra{\phi}$ pode ser pensado como um funcional linear que pode atuar em um vetor coluna $\ket{\psi}$ para resultar no número complexo $\braket{\phi | \psi}$. Pode-se verificar que todo funcional linear é da forma $\bra{\phi} = \braket{\phi | \cdot}$ para algum $\ket{\phi}$.

:::{admonition} Exemplo
:class: tip

O bra $\bra{0}$ é um funcional linear que leva $\ket{\psi}$ no coeficiente $\braket{0 | \psi}$ da projeção na direção $\ket{0}$. Igualmente, o bra $\bra{1}$ é um funcional linear que leva $\ket{\psi}$ no coeficiente $\braket{1 | \psi}$ da projeção na direção $\ket{1}$.
:::

### Projeção e Relação de Completude

Se $\ket{u}$ for unitário, o funcional linear $\bra{u}$ leva um ket $\ket{\psi}$ em $\braket{u | \psi}$, que corresponde ao coeficiente da projeção de $\ket{\psi}$ na direção de $\ket{u}$.

O vetor $\braket{u | \psi}\ket{u}$ é a projeção de $\ket{\psi}$ na direção do vetor unitário $\ket{u}$. Movendo-se o número $\braket{u | \psi}$ para a direita, pode-se escrever essa projeção como $\text{proj}_{\ket{u}} \ket{\psi} = \ket{u}\bra{u}\ket{\psi}$. O operador $\ket{u}\bra{u}$ é, então, chamado operador projeção na direção de $\ket{u}$

Se $\beta = \{\ket{b_0}, \ldots, \ket{b_{n-1}} \}$ é uma base ortonormal, pode-se escrever qualquer vetor $\ket{\psi}$ como soma das suas projeções ortogonais sobre as direções definidas pelos vetores da base. Dessa forma, tem-se

$$
\ket{\psi} = \sum_{k=0}^{n-1} \braket{b_k | \psi} \ket{b_k} =  \sum_{k=0}^{n-1} \ket{b_k}\braket{b_k | \psi}  \ \ .
$$

Segue que

$$
\sum_{k=0}^{n-1} \ket{b_k}\bra{b_k} = I  \ ,
$$

expressão conhecida como *relação de completude*.

:::{admonition} Exemplo
:class: tip

A projeção ortogonal da direção do vetor $\ket{0}$ é o operador $\ket{0}\bra{0}$, visto que sua ação em um ket $\ket{\psi}$ é dada por $\ket{0}\bra{0} \ket{\psi} = \braket{0 | \psi} \ket{0}$ e a projeção ortogonal na direção de $\ket{1}$ é o operador de projeção $\ket{1}\bra{1}$, pois $\ket{1}\bra{1} \ket{\psi} = \braket{1 | \psi} \ket{1}$.

A relação de completude no espaço vetorial dos estados de 1 qubit, $\mathbb{C}^2$, é dada por

$$
I = \ket{0}\bra{0} + \ket{1}\bra{1} \ .
$$
:::

(cap2sec-def-tl-nos-elementos-da-base)=

### Definição de uma Transformação Linear nos Elementos da Base

Para definir uma transformação linear, basta que se forneça como ela atua nos elementos de uma base. Isto é, dada $\beta = \{\ket{b_0}, \ldots, \ket{b_{n-1}} \}$ base de $\mathbb{C}^n$, pode-se obter $T\ket{\psi}$ conhecendo-se $T\ket{b_k}$ para todo $k$. De fato, como $\beta$ base, pode-se escrever $\ket{\psi}$ como combinação linear

$$
\ket{\psi} = \sum_k a_k \ket{b_k} \ \ .
$$

Aplicando-se a transformação $T$ e usando a linearidade, obtém-se

$$
T\ket{\psi} = \sum_k a_k T\ket{b_k}  \ \ ,
$$

e dessa forma, $T\ket{\psi}$ pode ser obtido a partir dos $T\ket{b_k}$'s.

(cap2ex-transformacao-linear-nos-elementos-da-base)=

:::{admonition} Exemplo
:class: tip

Considere o operador linear em 1 qubit $X \colon \mathbb{C}^2 \to \mathbb{C}^2$ definido nos vetores da base computacional por

$$
\begin{array}{l}
  X\ket{0} = \ket{1} \\
  X \ket{1} = \ket{0}
\end{array}
$$

O operador $X$ está bem definido em todo $\ket{\psi} = a \ket{0} + b \ket{1}$ graças à sua linearidade:

$$
X\ket{\psi} = X\big(a \ket{0} + b \ket{1}\big) = a X\ket{0} + b X \ket{1} = a \ket{1} + b \ket{0} \ .
$$
:::

(cap2sec-matriz-tl)=

### Matriz de uma Transformação Linear

Seja $T  \colon U= \mathbb{C}^n \to V=\mathbb{C}^m$  uma transformação linear. Sejam $\beta_U = \{\ket{u_0}, \ldots, \ket{u_{n-1}} \}$ base de $U$ e $\beta_V = \{ \ket{v_0} , \ldots , \ket{v_{n-1}} \}$ base de $V$. Quando fixadas bases para os espaços vetoriais do domínio e do contradomínio de $T$, é possível representar a transformação $T$ por uma matriz, de forma que a atuação de $T$ sobre um vetor $\ket{\psi}$ é equivalente ao produto matriz-vetor coluna.

A matriz da transformação linear $T$ nas bases $\beta_U$ e $\beta_V$ é dada por:

$$
[T]^{\beta_U}_{\beta_V} = \left[ \begin{matrix} | & & | \\ [T(u_0)]_{\beta_V} & \cdots & [T(u_{n-1})]_{\beta_V} \\  | & & | \end{matrix} \right]  \in M(m,n)
$$

Definida dessa forma, vale que:

$$
[T\ket{\psi}]_{\beta_V} = [T]^{\beta_U}_{\beta_V} \cdot [\ket{\psi}]_{\beta_U} \ \ ,
$$

portanto, a atuação da matriz de $T$ sobre um ket é equivalente à multiplicação matriz-vetor coluna levando-se em consideração as bases previamente fixadas.

Considere que as bases $\beta_U$ e $\beta_V$ sejam ortonormais. Cada vetor $T\ket{u_k}$ pode ser escrito na base $\beta_V$ da seguinte forma:

$$
[T\ket{u_k}]_{\beta_V} = \begin{bmatrix} \braket{v_0 | Tu_k} \\  \braket{v_1 | Tu_k} \\ \vdots \\  \braket{v_{m-1}}{Tu_k} \end{bmatrix}_{\beta_V} \ ,
$$

tendo em vista que a $l$-ésima entrada do vetor é o coeficiente da projeção de $\ket{Tu_k}$ na direção do $l$-ésimo vetor da base em $V$. Assim, a entrada de linha $l$ e coluna $k$ da matriz $[T]^{\beta_U}_{\beta_V}$ é $\braket{v_l | Tu_k}$, com $l = 0, \ldots , m-1$ e $k=0, \ldots , n-1$ e consequentemente

$$
[T]^{\beta_U}_{\beta_V} =
\begin{bmatrix} \braket{v_0 | Tu_0} & \braket{v_0 | Tu_1} & \ldots & \braket{v_0 | Tu_{n-1}} \\
        \braket{v_1 | Tu_0} & \braket{v_1 | Tu_1} & \ldots & \braket{v_1 | Tu_{n-1}} \\
        \vdots & \vdots & \ddots & \vdots \\
        \braket{v_{m-1}}{Tu_0} & \braket{v_{m-1}}{Tu_1} & \ldots & \braket{v_{m-1}}{Tu_{n-1}} \end{bmatrix} \ .
$$

No caso de um operador linear, tem-se $U=V$ ($m=n$), e é possível escolher a mesma base $\beta = \{\ket{b_0}, \ldots, \ket{b_{n-1}} \}$ para o domínio e o contradomínio da transformação. Essa é uma situação bastante frequente, e a matriz associada ao operador linear é montada da seguinte forma: as colunas da matriz são os vetores $\ket{Tb_k}$ escritos como vetores coluna na base $\beta$. Portanto:

$$
[T]_{\beta} = [T]^{\beta}_{\beta} = \left[ \begin{matrix} | & & | \\ \big[\ket{Tb_0}\big]_{\beta} & \cdots & \big[\ket{Tb_{n-1}}\big]_{\beta} \\  | & & | \end{matrix} \right]
$$

Se a base $\beta$ for ortonormal, obtém-se que

$$
[T]_{\beta} =
\begin{bmatrix} \braket{b_0 | Tb_0} & \braket{b_0 | Tb_1} & \ldots & \braket{b_0 | Tb_{n-1}} \\
        \braket{b_1 | Tb_0} & \braket{b_1 | Tb_1} & \ldots & \braket{b_1 | Tb_{n-1}} \\
        \vdots & \vdots & \ddots & \vdots \\
        \braket{b_{n-1}}{Tb_0} & \braket{b_{n-1}}{Tb_1} & \ldots & \braket{b_{n-1}}{Tb_{n-1}} \end{bmatrix} \ .
$$

:::{admonition} Exemplo
:class: tip

Um operador linear $A$ sobre um qubit pode ser escrito como uma matriz (na base computacional) $2\times2$ com coeficientes complexos da seguinte forma:

$$
[A] = \left[ \begin{matrix} | & | \\ \big[ A\ket{0}\big]  & \big[ A\ket{1}\big] \\  | & | \end{matrix} \right] =
\begin{bmatrix} \phantom{\Big(} \! \! \! \bra{0}A\ket{0} & \bra{0}A\ket{1} \ \ \\
        \phantom{\Big(}\! \! \! \bra{1}A\ket{0} & \bra{1}A\ket{1} \ \  \end{bmatrix}
      \ \ ,
$$

com $[\cdot]$ significando que os vetores em questão estão escritos como vetores coluna na base computacional. É frequente denotar a matriz do operador $A$ pelo mesmo símbolo $A$, quando está implícito qual base é considerada.
:::

(cap2ex-matriz-da-transformacao-linear)=

:::{admonition} Exemplo
:class: tip

A matriz da transformação linear do exemplo [Transformação Linear nos Elementos da Base](cap2ex-transformacao-linear-nos-elementos-da-base), na base computacional, é obtida escrevendo-se a ação de $X$ sobre os vetores da base.

$$
\begin{array}{l}
  X\ket{0} = \ket{1} = \begin{bmatrix} 0 \\ 1 \end{bmatrix} \\ \\
  X \ket{1} = \ket{0} = \begin{bmatrix} 1 \\ 0 \end{bmatrix} \ .
\end{array}
$$

Em seguida, monta-se a matriz fazendo

$$
X = \left[ \begin{matrix} | & | \\  X\ket{0}  &  X\ket{1} \\  | & | \end{matrix} \right] = \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix} \ .
$$
:::

(cap2ex-matrizes-de-pauli)=

:::{admonition} Matrizes de Pauli
:class: tip

As matrizes

$$
X = \begin{bmatrix}0 & 1 \\ 1 & 0 \end{bmatrix} \ \ , \ \ \ Y = \begin{bmatrix} 0 & -i \\ i & \phantom{-}0 \end{bmatrix} \ \ \text{e} \ \ \ Z =  \begin{bmatrix} 1 & \phantom{-}0 \\ 0 & -1 \end{bmatrix}
$$

são conhecidas como *matrizes de Pauli*. Essas são representações na base computacional dos operadores $X$, $Y$ e $Z$. Usa-se, costumeiramente, a mesma notação para se referir ao operador e à sua matriz na base computacional.

Em determinadas situações, a matriz identidade $I$ também é chamada matriz de Pauli, e usa-se a notação alternativa

$$
I = \sigma_0 \ \ , \ \ \ X = \sigma_x = \sigma_1 \ \ , \ \ \ Y = \sigma_y = \sigma_2 \ \ \text{e} \ \ \ Z = \sigma_z = \sigma_3 \ .
$$
:::

### Matriz da Composição de Transformações Lineares

A composição de transformações lineares $T \colon U \to V$ e $R \colon V \to W$ é a transformação linear denotada por $R T = R \circ T \colon U \to W$ e tal que $RT(\ket{\psi}) = R \Big( T\big(\ket{\psi}\big) \Big)$ para todo $\ket{\psi}$. A matriz dessa transformação linear pode ser obtida pela multiplicação matricial das matrizes de $R$ e de $T$:

$$
[RT]^{\beta_U}_{\beta_W} = [R]^{\beta_U}_{\beta_V} \cdot [T]^{\beta_V}_{\beta_W} \ ,
$$

em que $\beta_U$, $\beta_V$ e $\beta_W$ são bases de $U$, $V$ e $W$, respectivamente.

### Mudança de Base

Para escrever a matriz de uma transformação linear $T\colon U \to V$ em novas bases $\beta_U^\prime$ e $\beta_V^\prime$ basta aplicar matrizes de mudança de base de maneira apropriada.

$$
[T]^{\beta_U^\prime}_{\beta_V^\prime} = [I]^{\beta_U^\prime}_{\beta_U} [T]^{\beta_U}_{\beta_V} [I]^{\beta_V}_{\beta_V^\prime} \ .
$$

No caso de um operador linear $A \colon V \to V$, pode-se usar a mesma base nos espaços vetoriais do domínio e do contradomínio da função. A mudança de base nesse caso fica:

$$
[A]^{\beta_U^\prime}_{\beta_U^\prime} = [I]^{\beta_U^\prime}_{\beta_U} [A]^{\beta_U}_{\beta_U} [I]^{\beta_U}_{\beta_U^\prime}
  = \big( [I]^{\beta_U}_{\beta_U^\prime} \big)^{-1} [A]^{\beta_U}_{\beta_U} \big( [I]^{\beta_U}_{\beta_U^\prime} \big) \ .
$$

A transformação matricial $[A] \to [A]^\prime = [M]^{-1} [A] [M]$ é conhecida como *transformação de similaridade*. Duas transformações conectadas dessa forma são ditas *matrizes semelhantes*. As matrizes semelhantes são representantes de um mesmo operador linear escrito em bases diferentes.

Se as bases $\beta_U$ e $\beta_U^\prime$ forem ortonormais, a fórmula para mudança de base fica:

$$
[A]^{\beta_U^\prime}_{\beta_U^\prime} = [I]^{\beta_U^\prime}_{\beta_U} [A]^{\beta_U}_{\beta_U} [I]^{\beta_U}_{\beta_U^\prime}
  = \big( [I]^{\beta_U}_{\beta_U^\prime} \big)^{\dagger} [A]^{\beta_U}_{\beta_U} \big( [I]^{\beta_U}_{\beta_U^\prime} \big) \ ,
$$

em que a operação simbolizada por $\dagger$ é a transposição e conjugação da matriz. Essa operação será introduzida formalmente na seção [Operador Adjunto](cap2operador-adjunto).

(cap2ex-matriz-hadamard-mudanca-base-x)=

:::{admonition} Matrizes de Pauli
:class: tip

Considere as bases $\mathcal{I}$ e $\mathcal{X}$ apresentadas no exemplo [Base para 1 qubit].
A matriz de mudança de base de $\mathcal{I}$ para $\mathcal{X}$ e vice-versa é a matriz de Hadamard $H$, como visto no exemplo [Matrix Mudança de Base](cap2ex-matrix-mudanca-de-base). O operador $X$, visto no exemplo [Matrizes de Pauli](cap2ex-matrizes-de-pauli), cuja matriz na base computacional é

$$
X = [X]_{\mathcal{I}} =  \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}
$$

pode ser representado na base $\mathcal{X}$ por

$$
\begin{split}
  [X]_{\mathcal{X}}
  &= [I]^{\mathcal{I}}_{\mathcal{X}} [X]_\mathcal{I} [I]^{\mathcal{X}}_{\mathcal{I}} \\
  &= H X H \\
  &= \frac{1}{\sqrt{2}}\begin{bmatrix} 1 & 1 \\ 1 & -1 \end{bmatrix} \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix} \frac{1}{\sqrt{2}}\begin{bmatrix} 1 & 1 \\ 1 & -1 \end{bmatrix}  \\
  &= \begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix} \\
  &= Z \ .
\end{split}
$$
:::

