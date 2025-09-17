# Autovalores, Autovetores e Operadores

## Autovalores, Autovetores e Decomposição Espectral

### Autovalores e Autovetores

Seja $A$ um operador linear, com matriz na base computacional também representada por $A$. Os *autovalores* de $A$ são os números complexos $\lambda$ que satisfazem

$$
A \ket{v} = \lambda \ket{v} \ \  \text{para algum $\ket{v} \neq 0$ .}
$$

Os vetores não nulos $\ket{v}$ que satisfazem a equação acima são chamados *autovetores* de $A$ associados ao autovalor $\lambda$.

(cap2ex-autovalores-z)=

:::{admonition} Exemplo
:class: tip

O operador linear em 1 qubit $Z$ definido pela matriz

$$
Z = \begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix}
$$

possui:

- autovalor $1$, pois o vetor não nulo $\ket{0}$ é tal que $Z \ket{0} = 1 \cdot \ket{0}$;
- autovalor $-1$, pois o vetor não nulo $\ket{1}$ satisfaz $Z \ket{1} = -1 \cdot \ket{1}$.
:::

### Cálculo de Autovalores

A equação de autovalores $A \ket{v} = \lambda \ket{v}$ é equivalente a $\big(A-\lambda I \big) \ket{v} = 0$, com $\ket{v} \neq 0$, e isso é equivalente a dizer que a matriz de $A-\lambda I$ é singular. Por sua vez, isso equivale à equação

$$
\det (A-\lambda I ) = 0 \  .
$$

Com a equação acima, consegue-se encontrar os autovalores $\lambda$ do operador $A$ encontrando-se as raízes do *polinômio característico* $(A-\lambda I)$. Esse polinômio têm grau $n$ e, como estamos buscando raízes nos números complexos, admite $n$ raízes (pode acontecer que sejam repetidas). Dessa forma, todo operador admite um autovalor (isso não é necessariamente válido para espaços vetoriais reais).

:::{admonition} Exemplo
:class: tip

Os autovalores da matriz

$$
A = \begin{bmatrix} 0 & 2 \\ -1 & i \end{bmatrix}
$$

podem ser obtidos por:

$$
\begin{array}{rcl}
& & \det (A-\lambda I ) = 0 \\
& & \det \begin{bmatrix} 0 - \lambda & 2 \\ -1 & i-\lambda \end{bmatrix} = 0 \\
& & -\lambda(i-\lambda) - 2 \cdot -1 = 0\\
& & \lambda^2 - i \lambda + 2 = 0 \\
& & \lambda = \dfrac{i \pm \sqrt{i^2 - 4 \cdot 1 \cdot 2}}{2\cdot 1} \\
& & \lambda = -i \ \text{ ou } \  \lambda = 2i \ .
\end{array}
$$

Os autovalores podem ser números complexos. Como a matriz é $2\times2$, foi obtido um polinômio característico de grau 2 e foram obtidas 2 raízes.
:::

### Cálculo de Autovetores

Uma vez descobertos os autovalores $\lambda$, retorna-se à equação $A \ket{v} = \lambda \ket{v}$, ou melhor, à equação

$$
\big(A-\lambda I \big) \ket{v} = 0
$$

para encontrar todos os autovetores $\ket{v} \neq 0$ satisfazendo essa equação. Como a matriz $A-\lambda I$ é singular (essa é a condição para se encontrar $\lambda$), a equação em questão admite infinitas soluções $\ket{v}$, formando um sistema linear possível e indeterminado.

Em algumas situações é possível montar uma base para o espaço composta por autovetores do operador $A$. Há condições sobre o operador que revelam se é possível obter uma base ortonormal de autovetores. Isso será visto na seção [Tipos Especiais de Operadores](cap2tipos-especiais-de-operadores). A obtenção de uma base de autovetores permite escrever a matriz $A$ nessa base como uma matriz diagonal, o que se prova útil em diversas circunstâncias.

(cap2ex-autovetores-x)=

:::{admonition} Exemplo
:class: tip

Dada a matriz

$$
X = \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix} \ ,
$$

os autovalores e autovetores são encontrados a seguir.

- **Autovalores:** Resolvendo $\det(X - \lambda I) = 0$, obtém-se:

  $$
  \begin{array}{rcl}
  & & \det(X - \lambda I) = 0 \\
  & &  \det \begin{bmatrix} -\lambda & 1 \\ 1 & -\lambda \end{bmatrix} = 0 \\
  & &  \lambda^2 - 1 = 0  \\
  & &  \lambda = \pm 1 \ .
  \end{array}
  $$

- **Autovetores:** Para cada autovalor $\lambda$, deve-se resolver

  $$
  \big(X-\lambda I \big) \ket{v} = 0 \ ,
  $$

  obtendo-se o vetor $\ket{v}$.

  Para $\lambda = -1$:

  $$
  \begin{array}{rcl}
  \big(X-\lambda I \big) \ket{v} &=& 0 \\
  \begin{bmatrix} -1 & 1 \\ 1 & -1 \end{bmatrix} \begin{bmatrix} a_0 \\ a_1\end{bmatrix} &=& \begin{bmatrix} 0 \\ 0 \end{bmatrix}
  \end{array}
  $$

  $$
  \begin{cases}
    -a_0 + a_1 = 0 \\ \phantom{-}a_0 - a_1 = 0
  \end{cases}
  $$

  O sistema resultante, como esperado, é possível e indeterminado. Resolvendo o sistema, tem-se:

  $$
  \begin{cases}
  a_0 = a_1 \\
  a_1 \in \mathbb{C} \ .
  \end{cases}
  $$

  Os autovetores associados ao autovalor $\lambda = -1$ são:

  $$
  \ket{v} = \begin{bmatrix} a_1 \\ a_1 \end{bmatrix} = a_1 \begin{bmatrix} 1 \\ 1 \end{bmatrix}  \ \ \text{ com } a_1 \in \mathbb{C}, a_1 \neq 0
  $$

  O autoespaço associado a $\lambda = -1$ é o subespaço vetorial:

  $$
  V_{-1} = \left\lbrace a_1 \begin{bmatrix} 1 \\ 1 \end{bmatrix}  \colon a_1 \in \mathbb{C} \right\rbrace \ = \text{span}\left\lbrace \begin{bmatrix} 1 \\ 1 \end{bmatrix} \right\rbrace .
  $$

Para $\lambda = 1$:

$$
\begin{array}{rcl}
  \big(X-\lambda I \big) \ket{v} &=& 0 \\
  \begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix} \begin{bmatrix} a_0 \\ a_1\end{bmatrix} &=& \begin{bmatrix} 0 \\ 0 \end{bmatrix}
\end{array}
$$

$$
\begin{cases}
  a_0 + a_1 = 0 \\ a_0 + a_1 = 0
\end{cases}
$$

O sistema é possível e indeterminado, e, resolvendo o sistema, tem-se:

$$
\begin{cases}
a_0 \in \mathbb{C}  \\
a_1 = - a_0 \ .
\end{cases}
$$

Os autovetores associados ao autovalor $\lambda = 1$ são:

$$
\ket{v} = \begin{bmatrix} a_0 \\ - a_0 \end{bmatrix} = a_0 \begin{bmatrix}\phantom{-} 1 \\ - 1 \end{bmatrix}  \ \ \text{ com } a_0 \in \mathbb{C}, a_0 \neq 0
$$

O autoespaço associado a $\lambda = 1$ é o subespaço vetorial:

$$
V_{1} = \left\lbrace a_0 \begin{bmatrix} \phantom{-}1 \\ -1 \end{bmatrix}  \colon a_0 \in \mathbb{C} \right\rbrace \ = \text{span}\left\lbrace \begin{bmatrix} \phantom{-}1 \\ -1 \end{bmatrix} \right\rbrace .
$$
:::

## Operadores

### Diagonalização de Operadores

Uma vez encontrados os autovalores $\lambda_j$ e uma base de autovetores $\mathcal{V} = \{ \ket{v_j} , j=0, \ldots , n-1 \}$, com $\ket{v_j}$ associado ao autovalor $\lambda_j$, o operador linear $A$ pode ser escrito na base $\mathcal{V}$ como uma matriz diagonal. Defina as matrizes:

$$
\begin{array}{rcl}
  D &=& \begin{bmatrix}  \ \lambda_0 \  & & \\  & \ \ddots \ & \\ & & \ \lambda_{n-1}  \, \, \end{bmatrix} \text{(matriz diagonal dos autovalores)} \\
  M &=& \begin{bmatrix} | & & | \\ \ket{v_0} & \cdots & \ket{v_{n-1}} \\  | & & |  \end{bmatrix}  \text{(matriz de mudança de base: $\mathcal{I} \ \rightarrow  \ \mathcal{V}$)} \ .
\end{array}
$$

A matriz de $A$ na base $\mathcal{V}$ é dada por:

$$
\begin{array}{rcl}
    [A]_{\mathcal{V}}
    &=&
    \begin{bmatrix} | & & | \\ {[A\ket{v_0}]_{\mathcal{V}}} \ \  & \cdots & \ \ \ \  {[A\ket{v_{n-1}}]_{\mathcal{V}}}\,  \\ | &  & | \end{bmatrix} \\
    &=&
  \begin{bmatrix} | & & | \\ {[\lambda_0\ket{v_0}]_{\mathcal{V}}}  & \cdots & {[\lambda_{n-1}\ket{v_{n-1}}]_{\mathcal{V}}} \\ | &  & | \end{bmatrix} \\
    &=&
  \begin{bmatrix}  \lambda_0  & & \\  & \ddots & \\ & & \lambda_{n-1} \end{bmatrix} = D
\end{array}
$$

A matriz $M$ nada mais é que a matriz de mudança de base $M=[I]^{\mathcal{I}}_{\mathcal{V}}$. Conforme a seção [Matriz de Mudança de Base](cap2matriz-de-mudanca-de-base) , pode-se escrever:

$$
D = [A]_\mathcal{V} = [I]^{\mathcal{V}}_{\mathcal{I}} [A] [I]_{\mathcal{V}}^{\mathcal{I}} = M^{-1} A M \ .
$$

Ainda, se a base $\mathcal{V}$ for ortonormal, conforme [Base Ortonormal](cap2base-ortonormal), pode-se escrever

$$
D = M^\dagger A M \ .
$$

Nessas expressões, usa-se $A$ para denotar a matriz $[A]$ do operador $A$ na base computacional, o que simplifica a notação quando não houver risco de confusão.

Portanto, de posse dos autovalores e de uma base ortonormal, é possível escrever o operador $A$ como uma matriz diagonal.

O operador $A$ também pode ser representado na notação do produto exterior da seguinte forma. Como $\mathcal{V}$ forma uma base ortonormal, vale a relação de completude $I = \sum_k \ket{v_k}\bra{v_k}$ para essa base. Aplicando-se essa relação a $A$, obtém-se

$$
A = AI = \sum_k A \ket{v_k}\bra{v_k} = \sum_k \lambda_k \ket{v_k}\bra{v_k} \ .
$$

(cap2ex-diagonalizacao-x)=

:::{admonition} Exemplo
:class: tip

No exemplo [Autovetores X](cap2ex-autovetores-X) foram calculados os autovalores e autovetores da matriz

$$
X = \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix} \ ,
$$

obtendo-se:

- $\lambda = 1\phantom{-}$ , $\ket{v} = a \begin{bmatrix} 1 \\ 1 \end{bmatrix}$ $\phantom{-}$ $(`a \in \mathbb{C}, a \neq 0$)$
- $\lambda = -1$ , $\ket{v} = a \begin{bmatrix}\phantom{-}1 \\ -1 \end{bmatrix}$ ($a \in \mathbb{C}, a \neq 0$)

Pretende-se extrair uma base ortonormal de autovetores para escrever $X$ na forma diagonal. Nesse caso (Todos os autoespaços de dimensão 1.), basta normalizar os autovetores obtidos.

- Para $\lambda = -1$:

  $$
  \Big|\Big|{a \begin{bmatrix} 1 \\ 1 \end{bmatrix} }\Big|\Big| = 1 \implies |{a}| \sqrt{1^2 + 1^2} = 1 \implies |{a}| = \frac{1}{\sqrt{2}} \ .
  $$

  Há várias opções para $a$ que satisfazem essa condição. Pode-se escolher apenas uma delas para fazer a diagonalização, por exemplo: $a = \frac{1}{\sqrt{2}}$. O autovetor normalizado é, portanto,

  $$
  \ket{v} = \frac{1}{\sqrt{2}} \begin{bmatrix} 1 \\ 1 \end{bmatrix} = \frac{1}{\sqrt{2}} \ket{0} + \frac{1}{\sqrt{2}} \ket{1} \ .
  $$

- Para $\lambda = 1$:

  $$
  \Big|\Big|{a \begin{bmatrix} \phantom{-}1 \\ -1 \end{bmatrix} }\Big|\Big| = 1 \implies |{a}| \sqrt{1^2 + (-1)^2} = 1 \implies |{a}| = \frac{1}{\sqrt{2}} \ .
  $$

  Do mesmo modo, pode-se escolher $a = \frac{1}{\sqrt{2}}$, e o autovetor normalizado é:

  $$
  \ket{v} = \frac{1}{\sqrt{2}} \begin{bmatrix}\phantom{-} 1 \\ -1 \end{bmatrix} = \frac{1}{\sqrt{2}} \ket{0} - \frac{1}{\sqrt{2}} \ket{1} \ .
  $$

- **Base ortonormal de autovetores:**

  $$
  \underbrace{\ket{v_0} = \frac{1}{\sqrt{2}} \begin{bmatrix} 1 \\ 1 \end{bmatrix}}_{\lambda = 1} \ \ , \ \ \underbrace{\ket{v_1} = \frac{1}{\sqrt{2}} \begin{bmatrix}\phantom{-} 1 \\ -1 \end{bmatrix}}_{\lambda = -1}
  $$

- **Diagonalização da matriz:**

  Matriz de $X$ na forma diagonal:

  $$
  X_D = \begin{bmatrix}\lambda_0 & \\ & \lambda_1\end{bmatrix} =  \begin{bmatrix}1 & \\ & -1 \end{bmatrix}
  $$

  Matriz de mudança de base:

  $$
  M = \begin{bmatrix} | & | \\ \ket{v_0}  & \ket{v_{1}} \\ | & | \end{bmatrix} = \begin{bmatrix} \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} \\ & \\ \phantom{-}\frac{1}{\sqrt{2}} & -\frac{1}{\sqrt{2}} \end{bmatrix} = \frac{1}{\sqrt{2}} \begin{bmatrix} 1 & \phantom{-}1 \\ 1 & -1 \end{bmatrix}
  $$

- **Operador na forma diagonal:** Na notação de produto exterior, tem-se:

$$
X = \sum_k \lambda_k \ket{v_k}\bra{v_k} = 1 \cdot \ket{v_0}\bra{v_0} - 1 \cdot \ket{v_1}\bra{v_1}
$$
:::

(funcao-de-operadores)=
### Função de Operadores

Como podemos calcular $f(A)$, em que $A$ é um operador? Vamos utilizar a série de Taylor

$$
f(x) = \sum_{n=0}^{\infty} \frac{(x - x_{0})^{n}}{n!} \frac{d^{n}f}{dx^{n}} \bigg\rvert_{x = x_0}
$$

onde $x_0$ é o ponto onde queremos expandir a função.

:::{admonition} Exemplo
:class: tip
$e^{x}$ = ?; $x_0 = 0$

$$
e^{x} = \sum\limits_{n=0}^{\infty}  \frac{x^{n}}{n!} \underbrace{\frac{d^{n}(e^{x})}{dx^{n}} \bigg\lvert_{x=0}}_{?}
$$

$$
\begin{cases} 
\frac{d(e^{x})}{dx} = e^{x} \\
\quad \vdots \\
\frac{d^{n}(e^{x})}{dx^{n}} = e^{x}
\end{cases} \implies \frac{d^{n}(e^{x})}{dx^{n}}\bigg\vert_{x=0} = 1
$$

$$
\therefore e^{x} = \sum\limits_{n=0}^{\infty} \frac{x^{n}}{n!}
$$

Expansão em série de Taylor para $e^x$

No caso onde $x$ é um operador $A$, temos:

$$
e^A = \sum_{n=0}^{\infty} \frac{A^n}{n!}
$$

Usando a decomposição espectral do operador $A$:

$$
A = \sum_{i} a_i \ket{a_i}\bra{a_i}; \quad A\ket{a_i} = a_i \ket{a_i}
$$

$$
\Rightarrow A^2 = \left( \sum_i a_i \ket{a_i} \bra{a_i} \right) \left( \sum_j a_j \ket{a_j} \bra{a_2} \right)
$$

$$
= \sum_{i,j} a_i a_j \ket{a_i} \underbrace{\braket a_i | a_j}_{\delta_ij} \bra{a_j}
$$

$$
= \sum_{i,j} a_i a_j \delta_{ij} \ket{a_i} \bra{a_j}
$$

$$
= \sum_{i} a_{i}^{2} \ket{a_i} \bra{a_i}
$$

$$
\therefore A^{2} = \sum_{i} a_{i}^{2} \ket{a_i} \bra{a_i} \implies A^{n} = \sum_{i} a_{i}^{n} \ket{a_i} \bra{a_i}
$$

Voltando para $e^A$

$$
e^{A} = \sum_{n=0}^{\infty} \frac{A^n}{n!} = \sum_{n=0}^{\infty} \frac{1}{n!} \left( \sum_{i} a_{i}^{n} \ket{a_i} \bra{a_i} \right)
$$

$$
= \sum_{i} \left( \sum_{n=0}^{\infty} \frac{a_{i}^{n}}{n!} \right) \ket{a_i} \bra{a_i}
$$

$$
e^{A} = \sum_{i} e^{a_i} \ket{a_i} \bra{a_i}
$$

:::

Portanto, de maneira geral, se $f(x)$ puder ser expandida em série de Taylor, então

$$
f(A) = \sum_{i} f(a_i) \ket{a_i} \bra{a_i}
$$


(cap2tipos-especiais-de-operadores)=

### Tipos Especiais de Operadores

Nesta seção, alguns operadores com propriedades especiais serão apresentados. Os operadores normais, hermitianos, unitários, positivos e projetivos participam da base da Mecânica Quântica.

(cap2operador-adjunto)=

#### Operador Adjunto

Seja $A$ um operador linear. Em Álgebra Linear, é possível demonstrar que existe um único operador linear, denotado por $A^{\dagger}$ e chamado *operador adjunto* de $A$, que satisfaz a seguinte propriedade:

- **(OA1)** $\big( \ket{\phi} , A\ket{\psi} \big) = \big( A^{\dagger}\ket{\phi} , \ket{\psi} \big)$
  Para qualquer base $\beta$, a matriz do operador $A^{\dagger}$ está relacionada com a matriz de $A$ por
- **(OA2)** $[A^\dagger ]_\beta = [A]_\beta^{\ \dagger} = \big( [A]_\beta^{\ *}\big)^{T}$
  isto é, a matriz $[A]_\beta^{\ \dagger}$ é obtida de $[A]_\beta$ conjugando suas entradas e tomando a transposta.

Algumas propriedades da adjunta estão dispostas na seguinte lista:

- $\big( A^\dagger \big)^\dagger = A$ (Involução)
- $\displaystyle \left( \sum_k a_k A_k \right)^{\dagger} = \sum_k a_k^{\ *} A_k^{\ \dagger}$  (Antilinearidade)

:::{admonition} Exemplo
:class: tip

A matriz adjunta de

$$
A = \begin{bmatrix} 2 & 1+i \\ -1 & 5i \end{bmatrix}
$$

é a matriz conjugada transposta

$$
A^\dagger = \begin{bmatrix} 2 & -1 \\ 1-i & -5i\end{bmatrix} \ .
$$
:::

#### Operadores Normais

Um operador é dito *normal* se comuta com seu operador adjunto:

- **(ON)** $A \cdot A^{\dagger} = A^{\dagger} \cdot A$

```{admonition} Exemplo
:class: tip

O operador definido pela matriz

$$
A = \begin{bmatrix} 1+i & -1 \\ 1 & 1-i \end{bmatrix}
$$
```

é normal, pois satisfaz $A A^\dagger = A^\dagger A$. De fato,

$$
A^\dagger = \begin{bmatrix} 1-i & 1 \\ -1 & 1+i \end{bmatrix}
$$

e tem-se que

$$
A A^\dagger = \begin{bmatrix} 1+i & -1 \\ 1 & 1-i \end{bmatrix} \begin{bmatrix} 1-i & 1 \\ -1 & 1+i \end{bmatrix} = \begin{bmatrix} 3 & 0 \\ 0 & 3 \end{bmatrix}
$$

$$
A^\dagger A = \begin{bmatrix} 1-i & 1 \\ -1 & 1+i \end{bmatrix} \begin{bmatrix} 1+i & -1 \\ 1 & 1-i \end{bmatrix} = \begin{bmatrix}3 & 0 \\ 0 & 3 \end{bmatrix}
$$

A importância do operador normal decorre do seguinte teorema:

(cap2teorema-espectral-op-normal)=

:::{admonition} Teorema Espectral
:class: seealso

Um operador é normal se, e somente se, for diagonalizável.
:::

Dessa forma, basta checar se um operador é normal para se saber se ele admite uma base de autovetores e uma representação por matriz diagonal.

(cap2op-hermitianos)=

#### Operadores Hermitianos ou Autoadjuntos

Um operador $H$ é dito *hermitiano*, ou *autoadjunto* se valer a seguinte propriedade:

- **(OH)**  $H^{\dagger} =  H$

:::{admonition} Exemplo
:class: tip

O operador dado por

$$
A = \begin{bmatrix}1 & -i \\ i & 1 \end{bmatrix}
$$

é autoadjunto, pois

$$
A^\dagger = \begin{bmatrix}1 & -i \\ i & 1\end{bmatrix} = A \ .
$$
:::

Os operadores hermitianos estão relacionados com a evolução no tempo de um sistema quântico fechado e com a medida de um observável.

Um operador hermitiano é, automaticamente, um operador normal, tendo em vista que $H H^\dagger = H^2 = H^\dagger H$. Conforme o teorema [Teorema Espectral: Operador Normal](cap2teorema-espectral-op-normal), todo operador hermitiano é, pois, diagonalizável. Além disso, há um teorema que permite tirar conclusões a respeito dos autovalores de uma matriz hermitiana.

(cap2teorema-espectral-op-hermitiano)=

:::{admonition} Teorema Espectral para Matrizes Hermitianas
:class: seealso

Um operador normal é hermitiano se, e somente se, todos os seus autovalores são reais.
:::

(cap2operadores-unitarios)=

#### Operadores Unitários

Um operador $U$ é dito *unitário* se satisfizer alguma das condições equivalentes:

- **(OU1)** $U^{\dagger} =  U^{-1}$.
- **(OU2)** As linhas ou as colunas de $[U]_\beta$ são vetores ortonormais em $\mathbb{C}^n$, para alguma base $\beta$.
- **(OU3)** $U$ é uma isometria, isto é, preserva o produto interno entre vetores (e em consequência, preserva também a distância entre vetores): $\big( U\ket{\phi} , U\ket{\psi} \big) = \big( \ket{\phi} , \ket{\psi} \big)$.

(cap2ex-operador-unitario)=

:::{admonition} Exemplo
:class: tip

O operador definido pela matriz

$$
H = \frac{1}{\sqrt{2}}\begin{bmatrix}1 & \phantom{-}1 \\ 1 & -1 \end{bmatrix}
$$

é unitário, pois as colunas $\ket{c_0} = \frac{1}{\sqrt{2}}\begin{bmatrix} 1 \\ 1\end{bmatrix}$ e $\ket{c_1} = \frac{1}{\sqrt{2}} \begin{bmatrix}\phantom{-}1 \\ -1 \end{bmatrix}$ são vetores ortonormais:

$$
\begin{array}{rcl}
||{\ket{c_0}||} &=& ||{ \frac{1}||{\sqrt{2}}\begin{bmatrix} 1 \\ 1\end{bmatrix}} = \frac{1}{\sqrt{2}} \sqrt{1^2 + 1^2} = 1 \\
||{\ket{c_0}||} &=& ||{ \frac{1}||{\sqrt{2}}\begin{bmatrix} \phantom{-}1 \\ -1\end{bmatrix}} = \frac{1}{\sqrt{2}} \sqrt{1^2 + (-1)^2} = 1 \\
\braket{c_0 | c_1} &=& \begin{bmatrix} 1 & 1 \end{bmatrix} \begin{bmatrix}\phantom{-}1 \\ -1 \end{bmatrix} = 1 - 1 = 0
\end{array}
$$
:::

O produto de dois operadores unitários é unitário:

$$
(U_1 U_2)^\dagger = U_2^\dagger U_1^\dagger = U_2^{-1} U_1^{-1} = (U_1 U_2)^{-1} \ .
$$

A condição de um operador ser unitário também implica normalidade, visto que $U U^\dagger = I = U^\dagger U$. De acordo com o teorema [Teorema Espectral: Operador Normal](cap2teorema-espectral-op-normal), todo operador unitário é, então, diagonalizável. Pode-se mostrar o seguinte teorema.

(cap2teorema-espectral-op-unitario)=

:::{admonition} Teorema Espectral para Operadores Unitários
:class: seealso

Seja $U$ uma matriz normal. $U$ é uma matriz unitária se, e somente se, os seus autovalores são números complexos de módulo 1, logo exprimíveis na forma $\lambda = e^{i\theta}$ para algum $\theta \in \mathbb{R}$.
:::

#### Operadores Positivos

Um operador é dito *positivo* quando satisfaz a seguinte propriedade:

- **(OPos)**  $\bra{\psi}P\ket{\psi} \geq 0 \ , \ \ \forall \ket{\psi}$.

  É possível demonstrar que um operador positivo é, automaticamente, hermitiano, e, portanto, todos os seus autovalores são reais. Além disso, a propriedade (OPos) é equivalente a dizer que todos os autovetores de $P$ são números reais não-negativos $\lambda \geq 0$.

Diz-se que um operador é *positivo definido* quando satisfaz a condição seguinte, mais rigorosas que (OPos):

- **(OPosDef)** $\bra{\psi}P\ket{\psi} > 0 \ , \ \ \forall \ket{\psi}\neq 0$

  Essa condição é equivalente a afirmar que todos os autovalores de $P$ são números reais positivos $\lambda >0$.

:::{admonition} Exemplo
:class: tip

O operador definido pela matriz

$$
A = \begin{bmatrix} 1 & -2 \\ 0 & 2 \end{bmatrix}
$$

é positivo. De fato, por se tratar de uma matriz triangular, os autovalores podem ser obtidos diretamente da diagonal: $\lambda = 1$ e $\lambda = 2$. Seus autovalores são todos não negativos, do que decorre que $A$ é positivo. Como nenhum autovalor é nulo, o operador é também positivo definido.
:::

#### Operadores de Projeção

Um *operador de projeção* é um operador $P$ que satisfaz:

- **(OProj)** $P^2 =  P$.

Os autovalores de $P$ podem assumir os valores $\lambda = 0$ ou $\lambda = 1$. De fato, se $\lambda$ é um autovalor com autovetor $\ket{v}\neq 0$ associado, tem-se $P\ket{v} = \lambda \ket{v} \implies \lambda \ket{v} = P\ket{v} = PP\ket{v} = \lambda P\ket{v} = \lambda^2 \ket{v}$, logo, $(\lambda^2 - \lambda)\ket{v} = 0$ e, como $\ket{v} \neq 0$, tem-se $\lambda^2 - \lambda = 0$ e, por fim, $\lambda = 0$ ou $\lambda = 1$. Isso prova, em virtude dos teoremas [Teorema Espectral: Operador Hermitiano](cap2teorema-espectral-op-hermitiano) e [Teorema Espectral: Operador Unitário](cap2teorema-espectral-op-unitario), que todo operador de projeção é hermitiano e positivo.

Considere o subspaço vetorial de dimensão finita $W = P(V)$ (imagem de $P$). Seja $k=\dim W$ e tome uma base ortonormal $\big\{ \ket{v_0}, \ldots , \ket{v_{k-1}} \big\}$ de $P(V)$. Estendendo-se a $\big\{ \ket{v_0}, \ldots , \ket{v_{k-1}}, \ket{v_k} , \ldots , \ket{v_{n-1}} \big\}$ base ortonormal do espaço $V$, é possível escrever o operador $P$ como

$$
P = \text{Proj}_W = \sum_{j=0}^{k-1} \ket{v_j}\bra{v_j} \ .
$$

O operador

$$
Q = I - P = \text{Proj}_{W^\perp} =  \sum_{j=k}^{n-1} \ket{v_j}\bra{v_j}
$$

é um operador de projeção no subespaço $W^{\perp}$.

Tem-se que $\text{Proj}_W + \text{Proj}_{W^\perp} = I$ e portanto, todo vetor $\ket{\psi}$ pode ser decomposto na soma de projeções em $W$ e em $W^{\perp}$:

$$
\ket{\psi} = \underbrace{\text{Proj}_W(\ket{\psi})}_{\in W} + \underbrace{\text{Proj}_{W^\perp}(\ket{\psi})}_{\in W^{\perp}} \ .
$$

:::{admonition} Exemplo
:class: tip

Os operadores no espaço de estados de 1 qubit

$$
\begin{array}{rcl}
  \ket{0}\bra{0} &=& \begin{bmatrix}1 & 0 \\ 0 & 0 \end{bmatrix} \\
  \ket{1}\bra{1} &=& \begin{bmatrix}0 & 0 \\ 0 & 1 \end{bmatrix}  \ ,
\end{array}
$$

são as projeções na direção dos vetores $\ket{0}$ e $\ket{1}$, respectivamente. Tem-se que

$$
I =  \ket{0}\bra{0} + \ket{1}\bra{1} \ ,
$$

que é a relação de completude.

Se denotarmos por $W = \text{span}\{\ket{0} \}$ o subespaço gerado por $\ket{0}$, tem-se que $W^\perp = \text{span}\{ \ket{1} \}$, $\ket{0}\bra{0} = \text{Proj}_W$, $\ket{1}\bra{1} = I - \ket{0}\bra{0} = \text{Proj}_{W^\perp}$ e qualquer vetor $\ket{\psi}$ pode ser escrito como

$$
\begin{array}{rcl}
  \ket{\psi}
  &=& I \ket{\psi} = (\ket{0}\bra{0} + \ket{1}\bra{1}) \ket{\psi} \\
  &=& \ \ket{0}\bra{0} \ket{\psi} \ + \  \ket{1}\bra{1}\ket{\psi} \\
  &=& \text{Proj}_W \ket{\psi} + \text{Proj}_{W^\perp} \ket{\psi} \ .
\end{array}
$$

Se $\ket{\psi} = a \ket{0} + b \ket{1}$, então

$$
\begin{array}{rcl}
\text{Proj}_W\ket{\psi}
&=& \ket{0}\bra{0}(a \ket{0} + b \ket{1}) = \ket{0}a\underbrace{\braket{0 | 0}}_{=1} + \ket{0}b\underbrace{\braket{0 | 1}}_{=0} = a \ket{0} \\
\text{Proj}_{W^\perp}\ket{\psi}
&=& \ket{1}\bra{1}(a \ket{0} + b \ket{1}) = \ket{1}a\underbrace{\braket{1 | 0}}_{=0} + \ket{1}b\underbrace{\braket{1 | 1}}_{=1} = b \ket{1} \ . \\
\end{array}
$$
:::

### Resumo

A figura abaixo traz um quadro resumo dos operadores especiais abordados neste capítulo.

:::{figure} /images/algebra/operators.png
:class: no-scaled-link
:width: 100%

Relação entre os operadores especiais estudados neste capítulo. Fonte: [Slides de Álgebra Linear, UFSM](https://sites.google.com/site/jonasmaziero/home/edu/topicos-em-ciencia-da-informacao-quantica).
:::

```{csv-table} Resumo das propriedades dos operadores especiais estudados neste capítulo
:delim: '&'
:header-rows: 1

Operador& Propriedade
Normal& $N N^\dagger = N^\dagger N$
Autoadjunto ou Hermitiano& $H^\dagger = H$
Unitário& $U^{-1} = U^\dagger$
Projetor& $P^2 = P$
Positivo& $\bra{\psi}P\ket{\psi} \geq 0 \ , \ \ \forall \ket{\psi}$
Positivo definido& $\bra{\psi}P\ket{\psi} > 0 \ , \ \ \forall \ket{\psi}\neq 0$
```
