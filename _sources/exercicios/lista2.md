# 2a Lista de Exercícios

```{note}
Material extraído das listas de exercício da matéria FSC5172 – Computação Quântica I ministradas pelo Prof. Dr. Eduardo Inacio Duzzioni.
```

### 1. Uma rotação do estado de um qubit por um ângulo $\phi$ em torno de um eixo apontando na direção $\hat{n}$ é dada por

$$
R_{\hat{n}}(\phi) = e^{-i\phi \vec{\sigma} \cdot \hat{n}/2}
$$

em que

$$
\hat{n} = (n_x, n_y, n_z)
$$

é um vetor unitário

$$
n_x^2 + n_y^2 + n_z^2 = 1
$$

e o vetor cujas entradas são matrizes de Pauli é escrito como

$$
\vec{\sigma} = (\sigma_x, \sigma_y, \sigma_z).
$$

Sendo assim,

$$
\vec{\sigma} \cdot \hat{n} = n_x\sigma_x + n_y\sigma_y + n_z\sigma_z.
$$

Agora vamos conectar a rotação com uma evolução unitária na mecânica quântica.

#### a)

Utilizando a expansão em série de Taylor de $R_{\hat{n}}(\phi)$, primeiro mostre que

$$
(\vec{\sigma} \cdot \hat{n})^2 = 1
$$

para em seguida concluir que

$$
R_{\hat{n}}(\phi) =
\cos(\phi/2)1 - i\vec{\sigma}\cdot\hat{n}\sin(\phi/2).
$$

---

#### b)

Considere um hamiltoniano que descreve um sistema quântico de dois níveis (qubit) qualquer

$$
H =
\begin{bmatrix}
h_{00} & h_{01} \
h_{01}^* & h_{11}
\end{bmatrix}
$$

em que

$$
h_{01} = h_R + ih_I
$$

e

$$
h_{00}, h_{11}, h_R, h_I \in \mathbb{R}.
$$

Escreva este hamiltoniano em função das matrizes de Pauli e da identidade

$$
{1, \sigma_x, \sigma_y, \sigma_z}.
$$

---

#### c)

Mostre que o operador descrito na equação anterior é um operador unitário.

---

#### d)

Um operador unitário $U$ pode ser escrito como

$$
U = e^{i\alpha}R_{\hat{n}}(\phi),
$$

onde

$$
\alpha \in \mathbb{R}.
$$

Considere agora que o operador de evolução em questão é o operador de evolução temporal

$$
U(t,0) = e^{-iHt/\hbar}.
$$

Encontre a correspondência entre os parâmetros do hamiltoniano

$$
{h_{00}, h_{11}, h_R, h_I},
$$

$t$ e $\hbar$ com os parâmetros da rotação

$$
\phi, n_x, n_y, n_z
$$

e $\alpha$.

```{hint}
Utilize a forma do hamiltoniano descrita no item b e lembre que qualquer vetor unitário pode ser escrito como

$$
\hat{r} = \frac{\vec{r}}{||\vec{r}||}.
$$
```

---

#### e)

Quais as condições sobre os parâmetros do hamiltoniano para que tenhamos rotações em cada um dos eixos $x$, $y$ e $z$?

---

#### f)

Encontre as relações entre os parâmetros do hamiltoniano e o tempo de evolução para que as portas lógicas quânticas $H$ (Hadamard) e $Y$ sejam implementadas.

---

### 2. Considere o seguinte estado quântico

$$
\ket{\psi(\theta,\phi)} =
\cos(\theta/2)\ket{0} +
e^{i\phi}\sin(\theta/2)\ket{1}.
$$

#### a)

Quais são as probabilidades de encontrar o estado do sistema nos autoestados dos observáveis $X$, $Y$ e $Z$ após a medida destes observáveis?

---

#### b)

Calcule o valor esperado dos operadores $X$, $Y$ e $Z$.

---

#### c)

A relação de incerteza Robertson-Heisenberg é dada por

$$
\Delta A \cdot \Delta B \geq
\frac{|\bra{\psi}[A,B]\ket{\psi}|}{2},
$$

em que $A$ e $B$ são dois operadores hermitianos.

Verifique a validade desta relação para

$$
A = X
$$

e

$$
B = Y.
$$

Para qual ou quais valores de $\theta$ o produto das incertezas é máximo?

---

### 3. Considere que o sistema quântico encontre-se no estado de Bell

$$
\ket{\psi^-} =
\frac{\ket{01} - \ket{10}}{\sqrt{2}}.
$$

Calcule o valor esperado do seguinte operador

$$
Z_1 \otimes \frac{Z_2 - X_2}{\sqrt{2}}.
$$

---