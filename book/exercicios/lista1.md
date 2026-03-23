# Exercícios para Consolidação

```{note}
Material extraído das listas de exercício da matéria FSC7152 – Computação Quântica I ministradas pelo Prof. Dr. Eduardo Inacio Duzzioni.
```

## 1. Considere os estados genéricos de um qubit

$$
\ket{\psi} = \alpha \ket{0} + \beta \ket{1}
$$

$$
\ket{\phi} = \gamma \ket{0} + \delta \ket{1}
$$

em que $\alpha, \beta, \gamma, \delta \in \mathbb{C}$, verifique as desigualdades abaixo:

### a) Desigualdade de Cauchy-Schwarz:

$$
\left| \bra{\psi}\ket{\phi} \right| \leq | \ket{\psi} | \cdot | \ket{\phi} |
$$

### b) Desigualdade triangular:

$$
| \ket{\psi} + \ket{\phi} | \leq | \ket{\psi} | + | \ket{\phi} |
$$

---

## 2. Ache um estado ortogonal a:

$$
\ket{\psi} = \cos\left(\frac{\theta}{2}\right)\ket{0} + \sin\left(\frac{\theta}{2}\right)e^{i\phi}\ket{1}
$$

onde $0 \leq \theta \leq \pi$ e $0 \leq \phi < 2\pi$.

---

## 3. Demonstre as seguintes propriedades:

### a)

$$
(A^\dagger)^\dagger = A
$$

### b)

$$
(\lambda A)^\dagger = \lambda^* A^\dagger
$$

### c)

$$
(A + B)^\dagger = A^\dagger + B^\dagger
$$

### d)

$$
(AB)^\dagger = B^\dagger A^\dagger
$$

### e)

$$
(\ket{\psi}\bra{\phi})^\dagger = \ket{\phi}\bra{\psi}
$$

---

## 4. Escreva as matrizes de Pauli ${X, Y, Z}$ e o operador identidade $I$ utilizando a representação de produto externo usando a base canônica:

$$
\ket{0} =
\begin{bmatrix}
1 \
0
\end{bmatrix}
\quad
\ket{1} =
\begin{bmatrix}
0 \
1
\end{bmatrix}
$$

### a)

$$
X =
\begin{bmatrix}
0 & 1 \
1 & 0
\end{bmatrix}
$$

### b)

$$
Y =
\begin{bmatrix}
0 & -i \
i & 0
\end{bmatrix}
$$

### c)

$$
Z =
\begin{bmatrix}
1 & 0 \
0 & -1
\end{bmatrix}
$$

### d)

$$
I =
\begin{bmatrix}
1 & 0 \
0 & 1
\end{bmatrix}
$$

---

## 5. Sendo $P$ um projetor, mostre que:

### a)

$$
Q = 1 - P
$$

também é um projetor.

### b)

$$
[Q, P] = 0
$$

### c)

$$
P \ket{\phi} \perp Q \ket{\phi}
$$

### d) Interprete o resultado.

---

## 6. Ache os autovetores e autovalores das matrizes.

### a) Porta lógica de Hadamard

$$
H = \frac{1}{\sqrt{2}}
\begin{bmatrix}
1 & 1 \
1 & -1
\end{bmatrix}
$$

### b) Porta lógica $X$

$$
X =
\begin{bmatrix}
0 & 1 \
1 & 0
\end{bmatrix}
$$

### c) Porta lógica $Y$ (Pauli $Y$)

$$
Y =
\begin{bmatrix}
0 & -i \
i & 0
\end{bmatrix}
$$

### d) Porta lógica $Z$ (Pauli $Z$)

$$
Z =
\begin{bmatrix}
1 & 0 \
0 & -1
\end{bmatrix}
$$

### e) Porta lógica CNOT

$$
CNOT =
\begin{bmatrix}
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & 0 & 1 \\
0 & 0 & 1 & 0
\end{bmatrix}
$$

---

## 7. Considere duas bases ortonormais definidas por:

$$
{\ket{u_i}} \quad \text{e} \quad {\ket{v_j}}, \quad i, j = 1, \dots, n
$$

Mostre que o operador

$$
M = \sum_{k=1}^{n} \ket{u_k}\bra{v_k}
$$

é unitário e responsável pela mudança da base ${\ket{v_i}}$ para a base ${\ket{u_j}}$.

---

## 8. Mostre que os estados de Bell, descritos abaixo, formam uma base para um espaço vetorial de 4 dimensões.

$$
\ket{\Phi^+} = \frac{1}{\sqrt{2}}(\ket{00} + \ket{11})
$$

$$
\ket{\Phi^-} = \frac{1}{\sqrt{2}}(\ket{00} - \ket{11})
$$

$$
\ket{\Psi^+} = \frac{1}{\sqrt{2}}(\ket{01} + \ket{10})
$$

$$
\ket{\Psi^-} = \frac{1}{\sqrt{2}}(\ket{01} - \ket{10})
$$

---

## 9. Calcule as matrizes e vetores resultantes das operações de produto tensorial:

### a) Produto tensorial de matrizes:

i.

$$
X \otimes I
$$

ii.

$$
X \otimes X
$$

iii.

$$
H \otimes I
$$

iv.

$$
H \otimes H
$$

v.

$$
I \otimes Z
$$

vi.

$$
Z \otimes Z
$$

vii.

$$
I \otimes Z \otimes Z
$$

viii.

$$
\ket{0}\bra{0} \otimes \ket{0}\bra{0}
$$

ix.

$$
\ket{0}\bra{0} \otimes \ket{1}\bra{1}
$$

x.

$$
I \otimes \ket{0}\bra{0}
$$

### b) Produto tensorial de vetores:

$$
{\ket{0}, \ket{1}} \otimes {\ket{0}, \ket{1}} \otimes {\ket{0}, \ket{1}}
$$

---

## 10. Obtenha a expressão matricial para os seguintes operadores:

### a)

$$
\sqrt{Y}
$$

em que $Y$ é a porta lógica definida no exercício acima.

### b)

$$
e^{i\theta X}
$$

em que $X$ é a porta lógica definida no exercício acima.

### c)

$$
\sqrt{SWAP}
$$

em que

$$
SWAP =
\begin{bmatrix}
1 & 0 & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}
$$