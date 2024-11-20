# Algoritmo de Simon

```{note}
Material extraído do TCC [*Computação Quântica: Uma abordagem para estudantes de graduação em Ciências Exatas*](./tcc-giovani.pdf), de Giovani Goraiebe Pollachini.
```

Assim como no caso do Algoritmo de Deutsch-Jozsa, o Algoritmo de Simon é um algoritmo quântico projetado para resolver o Problema de Simon. Esse problema também tem propósito de funcionar como laboratório de testes para a Computação Quântica, não apresentando aplicações conhecidas.  

## Problema de Simon 

O problema de Simon é um problema de promessa, em que é dada uma função booleana $f \colon \{ 0,1 \}^n \to  \{ 0,1 \}^n$ que pode ser ou 1-para-1 ou 2-para-1. Esses termos serão definidos e acompanhados de exemplos para melhor entendimento. Em seguida, o enunciado do problema de Simon será escrito formalmente. 

**Definição 1: Função 1-para-1 e 2-para-1**
Seja $f \colon \{ 0,1 \}^n \to  \{ 0,1 \}^n$ uma função booleana de $n$ para $n$ bits.
    
A função $f$ é dita 1-para-1 se é uma bijeção. Nesse caso, isso significa que cada resultado $y \in  \{ 0,1 \}^n$ é obtido por exatamente uma entrada $x_1$, ou seja, $f(x_1) = y$. Cada duas entradas distintas $x_1 \neq x_2$ geram resultados diferentes $f(x_1) \neq f(x_2)$.
    
A função $f$ é dita 2-para-1 se cada resultado $y \in  \{ 0,1 \}^n$ é obtido por exatamente duas entradas $x_1$ e $x_2$, isto é, $f(x_1) = f(x_2) = y$.

O problema de Simon requer um compromisso para a função booleana de entrada. A propriedade que a função deve satisfazer é chamada, no presente trabalho, de propriedade de Simon.

**Definição 2: Propriedade de Simon**

Sejam $f \colon \{ 0,1 \}^n \to  \{ 0,1 \}^n$ uma função booleana de $n$ para $n$ bits e $c \in  \{ 0,1 \}^n$.
    
Diz-se que $f$ satisfaz a propriedade de Simon se 

```{math}
f(x_1) = f(x_2) \Longleftrightarrow x_2 = x_1 \oplus c
```

em que a operação $\oplus$ é a XOR (ou seja, adição módulo 2) realizada bit a bit nos dois vetores de bits. 

**Exemplos:**
-  A função booleana $f \colon \{ 0,1 \}^2 \to  \{ 0,1 \}^2$ definida pela tabela abaixo é 1-para-1.
```{math}
\begin{array}{c|c}
     x & f(x) \\ \hline 
     00  & 10 \\
     01  & 11 \\
     10  & 00 \\
     11  & 01
    \end{array}
```

- A função booleana $f \colon \{ 0,1 \}^2 \to  \{ 0,1 \}^2$ definida pela tabela abaixo é 2-para-1.

```{math}
\begin{array}{c|c}
     x   & f(x) \\ \hline 
     00  & 10 \\
     01  & 01 \\
     10  & 10 \\
     11  & 01
    \end{array}
```
Essa função também satisfaz a propriedade de Simon com $c = 10$. De fato, 

```{math}
\begin{array}{lll}
        10 = 00 \oplus 10 & & f(00) = f(10) = 10  \\
        11 = 01 \oplus 10 & & f(01) = f(11) = 01 \ .
       \end{array} 
```

Observação 1: Nem toda função booleana 2-para-1 satisfaz a propriedade de Simon. De fato, a função $f \colon \{ 0,1 \}^3 \to  \{ 0,1 \}^3$ dada por

```{math}
\begin{array}{c|cccc|c}
     x    & f(x) & & & x & f(x) \\ -  1-2  - 5-6
     000  & 2 & & & 100  & 2 \\
     001  & 5 & & & 101  & 3 \\
     010  & 1 & & & 110  & 1 \\
     011  & 5 & & & 111  & 3
    \end{array}
```
Essa função é 2-para-1. Se satisfizesse a propriedade de Simon, existiria $c$ satisfazendo $f(x\oplus c ) = f(x)$ para todo $x$. No entanto,

```{math}
f(000) = f(100), 100 = 000 \oplus 100 \implies c = 100
```
E tem-se que

```{math}
f(000) = f(100), 100 = 000 \oplus 100 \implies c = 100
```

Essa contradição significa que a propriedade de Simon não é satisfeita.

Observação 2: Se $f$ satisfaz a propriedade de Simon com $c=0\ldots0$, então $f$ é 1-para-1. E se $f$ satisfaz a propriedade de Simon com $c\neq 0\ldots0$, então $f$ é 2-para-1.

De posse dessas definições, o problema de Simon tem o seguinte enunciado.

**Problema de Simon**

Dada uma função booleana $f\colon \{ 0,1 \}^n \to  \{ 0,1 \}^n$ satisfazendo a propriedade de Simon, distinguir se $f$ é 1-para-1 ou se é 2-para-1 e encontrar o período $c$.

## Algorítmo de Simon

O algoritmo a ser apresentado pressupõe que a função booleana $f$ seja dada como um oráculo XOR. Também são necessários 2 registradores de $n$ qubits. O algoritmo descreve uma subrotina a ser repetida da ordem de $n$ vezes. Em cada iteração, obtém-se um pouco de informação, que será processada classicamente para obter como saída o valor de $c$ e a decisão se $f$ é 1-para-1 ou 2-para-1.

**Procedimento:**

```{math}
\begin{array}
   \text{etapa 0:} & \ket{0}\ket{0} & \text{\small{preparação do estado inicial}} \vspace{2pt} \\ 
   \text{etapa 1:} &\displaystyle \tfrac{1}{\sqrt{2^n}} \sum_{x\in\mathbb{B}_n} \ket{x}\ket{0} & \text{\small{$H^{\otimes n}$ no registrador 1}} \vspace{2pt} \\ 
   \text{etapa 2:} &\displaystyle \tfrac{1}{\sqrt{2^n}} \sum_{x\in\mathbb{B}_n} \ket{x}\ket{f(x)} & \text{\small{aplicação de $f$ (oráculo XOR)}} \vspace{2pt} \\ 
   \text{etapa 3:} &\displaystyle \tfrac{1}{2^n} \sum_{x\in\mathbb{B}_n}\sum_{y\in\mathbb{B}_n} \ket{y}\ket{f(x)} & \text{\small{$H^{\otimes n}$ no registrador 1}} \vspace{2pt} \\ 
   \text{etapa 4:} \text{Medição. Obtém informação sobre a resposta} \\ 
   \text{etapa 5:} \text{Repetir etapas 0-4 da ordem de n vezes} \\ 
   \text{etapa 6:} \text{Computar a resposta classicamente com as informações obtidas} 
  \end{array}
```

**Saída:** Após processamento clássico final, valor do período $c$ e decisão se $f$ é 1-para-1 ou 2-para-1.

**Circuito**

Notação compacta:

![Screenshot 2024-10-22 at 18-39-26 tcc-giovani pdf](https://github.com/user-attachments/assets/c73a022d-14cc-43e8-8b37-5af760d98348)

Notação expandida:

![Screenshot 2024-10-22 at 18-40-22 tcc-giovani pdf](https://github.com/user-attachments/assets/28886f3d-3a48-4970-a909-30b4e7ab1306)

**Contas auxiliares**

**Definição 3:** Usa-se a seguinte notação, com o intuito de simplificar algumas expressões:

```{math}
\begin{split} 
       \tilde{0} &= +  \\
       \tilde{1} &= - \ . 
       \end{split}
```

Dado um vetor de bits $x \in \mathbb{B}_n$, escreve-se $\ket{\tilde{x}} = \ket{\tilde{x}_0 \tilde{x}_1 \ldots \tilde{x}_{n-1} }$ para designar um produto tensorial de estados $\ket{+}$ e $\ket{-}$. Por exemplo,

```{math}
\ket{x} = \ket{0110} \Longleftrightarrow \ket{\tilde{x}} = \ket{+--+}
```

**Definição 4:** $\mathbb{B}_n$ é o conjunto de todos os vetores de $n$ bits. 

**Proposição 1:** Vale que 
```{math}
H^{\otimes n} = \sum_{y \in \mathbb{B}_n} \ket{\tilde{y}}\bra{y}
```

**Demonstração:**
Prova-se por indução em $n$. 
    
Vale para $n=1$ qubit, já que $H$ pode ser escrito como
```{math} 
H = \ket{+}\bra{0} + \ket{-}\bra{1}
```
    
Vale para $n=2$ qubits, pois
```{math}
\begin{split} 
       H^{\otimes 2} 
       &= H \otimes H \\
       &=  \ket{+}\bra{0} + \ket{-}\bra{1} \otimes \ket{+}\bra{0} + \ket{-}\bra{1}  \\
       &= \ket{++}\bra{00} + \ket{+-}\bra{01} + \ket{-+}\bra{10} + \ket{--}\bra{11} \\
       &= \sum_{y \in \mathbb{B}_2}\ket{\tilde{y}}\bra{y} \ . 
       \end{split}
```
    
Supõe-se, então, que seja válido para $n$ qubits. Verifica-se o caso $n+1$:

![Screenshot 2024-10-22 at 18-43-09 tcc-giovani pdf](https://github.com/user-attachments/assets/258c5cd4-b3ca-4c41-bf50-23874f87a522)

Isso conclui a indução em $n$.

**Proposição 2:**
Vale que:

```{math}
\ket{\tilde{x}} = \frac{1}{\sqrt{2^n}} \sum_{y\in\mathbb{B}_n} (-1)^{x\cdot y} \ket{y}
```

em que $x \cdot y = x_0 y_0 + x_1 y_1 + \ldots + x_{n-1}y_{n-1}$.

**Demonstração: **
Mostra-se por indução em $n$. 
    
Para $n=1$ qubit, tem-se que
```{math}
    \begin{split}
        \ket{\tilde{0}} &= \ket{+} = \frac{1}{\sqrt{2}} \big( \ket{0} + \ket{1} \big) \\
        \ket{\tilde{1}} &= \ket{-} = \frac{1}{\sqrt{2}} \big( \ket{0} - \ket{1} \big) \ .
       \end{split}
```
       
   Para $n=2$ qubits, tem-se que 
   ```{math}
   \begin{split}
        \ket{\tilde{0} \tilde{0} } &= \ket{++} =  \frac{1}{\sqrt{2^2}} \big( \ket{00} + \ket{01} + \ket{10} + \ket{11} \big) \\
        \ket{\tilde{0} \tilde{1} } &= \ket{+-} =  \frac{1}{\sqrt{2^2}} \big( \ket{00} - \ket{01} + \ket{10} - \ket{11}\big) \\ 
        \ket{\tilde{1} \tilde{0} } &= \ket{-+} =  \frac{1}{\sqrt{2^2}} \big( \ket{00} + \ket{01} - \ket{10} - \ket{11} \big) \\ 
        \ket{\tilde{1} \tilde{1} } &= \ket{--} =  \frac{1}{\sqrt{2^2}} \big( \ket{00} - \ket{01} - \ket{10} + \ket{11} \big) \ ,
       \end{split}
```
   que pode ser resumido em
   ```{math}
    \ket{\tilde{x}} = \frac{1}{\sqrt{2^2}} \sum_{y\in\mathbb{B}_n} (-1)^{x\cdot y} \ket{y}
```
   
   Assume-se que o enunciado seja válido para $n$ qubits. O caso $n+1$ fica como a seguir.
   ```{math}
    \ket{\tilde{x}_0 \tilde{x}_1 \ldots \tilde{x}_{n-1} \tilde{x}_n } = \ket{\tilde{x}_0 \tilde{x}_1 \ldots \tilde{x}_{n-1}} \otimes \ket{\tilde{x}_n }
```
   Caso $\tilde{x}_n = +$, tem-se
   ```{math}
    \begin{split}
      &\ket{\tilde{x}_0 \tilde{x}_1 \ldots \tilde{x}_{n-1} + } \\
      \phantom{x}  &= \ket{\tilde{x}_0 \tilde{x}_1 \ldots \tilde{x}_{n-1}} \otimes \ket{+} \\
       &=  \left(\frac{1}{\sqrt{2^n}} \sum_{y\in\mathbb{B}_n} (-1)^{(x_0 \ldots x_{n-1})\cdot y} \ket{y} \right) \otimes \ket{+}  \\
       &=  \frac{1}{\sqrt{2^n}} \sum_{y\in\mathbb{B}_n} (-1)^{(x_0 \ldots x_{n-1})\cdot y} \ket{y_0 \ldots y_{n-1}}  \otimes \frac{1}{\sqrt{2}} \big( \ket{0} + \ket{1} \big) \\
       &=  \frac{1}{\sqrt{2^{n+1}}} \sum_{y\in\mathbb{B}_n} (-1)^{(x_0 \ldots x_{n-1})\cdot y} \big( \underbrace{\ket{y_0 \ldots y_{n-1} 0}}_{y_n = 0} +  \underbrace{\ket{y_0 \ldots y_{n-1} 1}}_{y_n = 1} \big) \\
       &=  \frac{1}{\sqrt{2^{n+1}}} ( \sum_{y\in\mathbb{B}_n} (-1)^{(x_0 \ldots x_{n-1})\cdot y + 0 \cdot 0} \underbrace{\ket{y_0 \ldots y_{n-1} 0}}_{y_n = 0} \ + \\
       & \qquad \qquad \qquad \qquad \qquad +\ (-1)^{(x_0 \ldots x_{n-1})\cdot y + 0 \cdot 1} \underbrace{\ket{y_0 \ldots y_{n-1} 1}}_{y_n = 1} ) \\
       &= \frac{1}{\sqrt{2^{n+1}}} \sum_{y\in\mathbb{B}_{n+1}} (-1)^{(x_0 \ldots x_{n-1}0)\cdot y} \ket{y_0 \ldots y_{n-1} y_n } \ .
      \end{split}
```
   No caso $\tilde{x}_n = -$, tem-se
   ```{math}
    \begin{split}
      &\ket{\tilde{x}_0 \tilde{x}_1 \ldots \tilde{x}_{n-1} - } \\
      \phantom{x}  &= \ket{\tilde{x}_0 \tilde{x}_1 \ldots \tilde{x}_{n-1}} \otimes \ket{-} \\
       &=  \left(\frac{1}{\sqrt{2^n}} \sum_{y\in\mathbb{B}_n} (-1)^{(x_0 \ldots x_{n-1})\cdot y} \ket{y} \right) \otimes \ket{-}  \\
       &=  \frac{1}{\sqrt{2^n}} \sum_{y\in\mathbb{B}_n} (-1)^{(x_0 \ldots x_{n-1})\cdot y} \ket{y_0 \ldots y_{n-1}}  \otimes \frac{1}{\sqrt{2}} \big( \ket{0} - \ket{1} \big) \\
       &=  \frac{1}{\sqrt{2^{n+1}}} \sum_{y\in\mathbb{B}_n} (-1)^{(x_0 \ldots x_{n-1})\cdot y} \big( \underbrace{\ket{y_0 \ldots y_{n-1} 0}}_{y_n = 0} -  \underbrace{\ket{y_0 \ldots y_{n-1} 1}}_{y_n = 1} \big) \\
       &=  \frac{1}{\sqrt{2^{n+1}}} \sum_{y\in\mathbb{B}_n} (-1)^{(x_0 \ldots x_{n-1})\cdot y + 1 \cdot 0} \underbrace{\ket{y_0 \ldots y_{n-1} 0}}_{y_n = 0} \ + \\
       & \qquad \qquad \qquad \qquad \qquad + \ (-1)^{(x_0 \ldots x_{n-1})\cdot y + 1 \cdot 1} \underbrace{\ket{y_0 \ldots y_{n-1} 1}}_{y_n = 1} \\
       &= \frac{1}{\sqrt{2^{n+1}}} \sum_{y\in\mathbb{B}_{n+1}} (-1)^{(x_0 \ldots x_{n-1}1)\cdot y} \ket{y_0 \ldots y_{n-1} y_n } \ .
      \end{split}
```
      
Isso conclui a demonstração.

**Proposição 3:** O produto tensorial de $n$ operadores de Hadamard é dado por

```{math}
H^{\otimes n} = \frac{1}{\sqrt{2^n}} \sum_{x,y \in \mathbb{B}_n} (-1)^{x \cdot y} \ket{x}\bra{y}
```

**Demonstração:**

Usando as proposições do produto tenosrial de H1 e a do produto tensorial entre estados, temos que:

```{math}
H^{\otimes n} = \sum_{y \in \mathbb{B}_n} \ket{\tilde{y}}\bra{y} = \sum_{y \in \mathbb{B}_n} \frac{1}{\sqrt{2^n}} \sum_{x\in\mathbb{B}_n} (-1)^{x\cdot y}\ket{x}\bra{y} 
```

**Proposição 4:**
A aplicação de $H^{\otimes n}$ a um estado $\ket{x} = \ket{x_{0} x_1 \ldots x_{n-1}}$ na base computacional é dada por 
```{math}
H^{\otimes n} \ket{x} = \frac{1}{\sqrt{2^n}} \sum_{y\in\mathbb{B}_n} (-1)^{x\cdot y} \ket{y}
```
 em que $x \cdot y = x_0 y_0 + x_1 y_1 + \ldots + x_{n-1}y_{n-1}$

**Demonstração:**
Usando proposições vistas anteriormente temos que:
```{math}
\begin{split}
        H^{\otimes n} \ket{x} 
        &= \frac{1}{\sqrt{2^n}} \sum_{y,z\in\mathbb{B}_n} (-1)^{y\cdot z} \ket{y}\bra{z} \ket{x} \\
        &= \frac{1}{\sqrt{2^n}} \sum_{y,z\in\mathbb{B}_n} (-1)^{y\cdot z} \ket{y} \delta_{z,x} \\
        &= \frac{1}{\sqrt{2^n}} \sum_{y \in\mathbb{B}_n} (-1)^{y\cdot x} \ket{y} \ . 
       \end{split}
```

Observação: A soma e o produto em 
  ```{math}
   x \cdot y = x_0 y_0 + x_1 y_1 + \ldots + x_{n-1}y_{n-1} \tag{int}
``` 
  podem ser entendidos como operações com números ou como operações com bits
  ```{math}
    x \cdot y = x_0 y_0 \oplus x_1 y_1 \oplus \ldots \oplus x_{n-1}y_{n-1} \tag{bit}
```
  em que o produto é dado pela AND e a soma $\oplus$ é dada pela XOR. Ambas as expressões resultam no mesmo sinal $(-1)^{x\cdot y}$, pois a expressão (bit) corresponde a (int) módulo 2, visto que a AND se comporta como um produto e a XOR, como uma adição módulo 2. 

## Etapas da subrotina de Simon

As etapas da subrotina quântica são mostradas em detalhes no texto que segue. Inicialmente, aplica-se $H^{\otimes n}$ ao primeiro registrador, obtendo-se 
```{math}
   \ket{\psi_1} = \frac{1}{\sqrt{2^n}} \sum_{x\in\mathbb{B}_n} \ket{x}\ket{0}
```
   
em que o primeiro ket engloba $n$ qubits e representa o primeiro registrador, e o segundo ket contém $n$ bits e representa o segundo registrador. 
   
A aplicação do oráculo na etapa 2 mantém o primeiro registrador e faz a XOR bit a bit de $0$ com $f(x)$:
   ```{math}
    \begin{split}
       \ket{\psi_2} 
       &= O_{\text{XOR}} \ket{\psi_1} \\
       &= \frac{1}{\sqrt{2^n}} \sum_{x\in\mathbb{B}_n} O_{\text{XOR}} \ket{x}\ket{0} \\
       &= \frac{1}{\sqrt{2^n}} \sum_{x\in\mathbb{B}_n} \ket{x}\ket{f(x)} \ .
      \end{split}
```
   
   Na etapa 3, aplica-se novamente $H^{\otimes n}$ ao primeiro registrador:
   ```{math}
   \begin{split} 
       \ket{\psi_3} 
       &= \frac{1}{\sqrt{2^n}} \sum_{x\in\mathbb{B}_n} \big(H^{\otimes n}\ket{x}\big)\ket{f(x)} \\
       &= \frac{1}{\sqrt{2^n}} \sum_{x\in\mathbb{B}_n}\frac{1}{\sqrt{2^n}} \sum_{y\in\mathbb{B}_n} (-1)^{x\cdot y} \ket{y}\ket{f(x)} \\
       &= \frac{1}{2^n} \sum_{x\in\mathbb{B}_n} \sum_{y\in\mathbb{B}_n} (-1)^{x\cdot y} \ket{y}\ket{f(x)} \ . 
      \end{split} 
```
      
  É conveniente passar o somatório em $x$ para o segundo registrador, ficando com:
  ```{math}
  \begin{split}
       \ket{\psi_3} 
       &= \frac{1}{2^n} \sum_{y\in\mathbb{B}_n} \ket{y}\left( \sum_{x\in\mathbb{B}_n} (-1)^{x\cdot y}  \ket{f(x)} \right) \ .
       \end{split}
```
       
  A medida na base computacional, na etapa 4, faz o estado do sistema colapsar em $\ket{y}\ket{z}$, com $z=f(x)$. Como $f$ tem a propriedade de Simon, os únicos valores que resultam em $z$ pela aplicação de $f$ são
  ```{math}
 z = f(x_1) = f(x_2) \ , \ \ x_2 = x_1 \oplus c
```

## Probabilidades nas medições

Caso $c \neq 0$, o coeficiente multiplicando o estado $\ket{y}\ket{z}$ em ($\ast$) é dado por
```{math}
 \begin{split} 
     a_{y,z}
     &= \frac{1}{2^n} \big( (-1)^{x_1 \cdot y} + (-1)^{x_2 \cdot y} \big) \\
     &= \frac{1}{2^n} \big( (-1)^{x_1 \cdot y} + (-1)^{(x_1 \oplus c) \cdot y} \big) \\
     &= \frac{1}{2^n} \big( (-1)^{x_1 \cdot y} + (-1)^{(x_1 \cdot y) \oplus (c \cdot y)} \big) \\
     &= \frac{1}{2^n} \big( (-1)^{x_1 \cdot y} + (-1)^{x_1 \cdot y} (-1)^{ c \cdot y} \big) \\
     &= \frac{1}{2^n} (-1)^{(x_1 \cdot y)} \big( 1 + (-1)^{ c \cdot y} \big) \\
     &= \begin{cases} 
         0 & \ \ \   c\cdot y = 1 \ , \\
         (-1)^{(x_1 \cdot y)} \frac{2}{2^n} & \ \ \   c \cdot y = 0 \ .
        \end{cases}
     \end{split}
```
  A probabilidade de se encontrar o sistema no estado $\ket{y}\ket{z}$ é, então,
  ```{math}
   \begin{split}
      p_{y,z} 
      &= |a_{y,z}|^2 = \begin{cases} 
         0 & \ \ \  c\cdot y = 1 \\
         \frac{2^2}{2^{2n}} & \ \ \  c \cdot y = 0
        \end{cases}
     \end{split}
```
 Assim, a medida só fornece vetores de bits $y$ perpendiculares a $c$. A informação que se ganha para encontrar $c$ é a equação
 ```{math}
  c \cdot y = c_1 y_1 \oplus c_1 y_1 \oplus \ldots \oplus c_n y_n = 0
```
 
 Caso $c = 0$, o coeficiente em ($\ast$) fica apenas
```{math}
    a_{y,z}
      = \frac{1}{2^n} (-1)^{x_1 \cdot y}
```
 e a probabilidade de se encontrar o sistema em $\ket{y}\ket{z}$ é
```{math}
     p_{y,z}
     =  |a_{y,z}|^2 = 2^{-2n}
```
Logo, qualquer vetor de bits $y$ pode sair como resultado da medição.

## Encontrando o valor do período c -- exemplo

Primeiramente, apresenta-se o processamento para encontrar o período $c$ em um exemplo, com o objetivo de facilitar a compreensão do método no caso geral.
     
Encontrando período $c$ com o algoritmo de Simon 
      
Seja $n = 4$ bits. Aplica-se a primeira iteração da subrotina quântica do algoritmo de Simon. Suponha que se obteve o resultado $y^{(1)} = 0111$. Esse resultado gera a equação
```{math}      
y^{(1)} \cdot c = 0 \implies c_2 \oplus c_3 \oplus c_4 = 0 \implies c_2 = c_3 \oplus c_4
```
Continua-se aplicando a subrotina até se obter $n-1 = 3$ equações LI.
      
A segunda iteração fornece $y^{(2)} = 1001$. Esse resultado corresponde à equação
```{math}
       y^{(2)} \cdot c = 0 \implies c_1 \oplus c_4 = 0  \ 
      \text{e o sistema, após simplificação, fica}
       \begin{cases}
           c_2 = c_3 \oplus c_4 \\
           c_1 = c_4 \ .
         \end{cases}
```
Como ainda não são 3 equações LI, continua-se a iteração.
      
Na terceira iteração, o resultado é $y^{(3)} = 1110$. A equação correspondente é
```{math}
       y^{(3)} \cdot c = 0 \implies c_1 \oplus c_2 \oplus c_3 = 0  \implies c_4 \oplus (c_3 \oplus c_4)\oplus c_3 = 0 \implies 0 = 0
```
e essa equação não fornece informação útil. O sistema continua sendo de 2 equações LI:
```{math}
        \begin{cases}
           c_2 = c_3 \oplus c_4 \\
           c_1 = c_4 \ .
         \end{cases}
```
         
Na quarta iteração obtém-se $y^{(4)} = 0001$, e a equação que esse resultado gera é
```{math}
 y^{(4)} \cdot c = 0 \implies c_4 = 0  
     \text{O sistema fica}
      \begin{cases}
           c_2 = c_3 \\
           c_1 = 0  \\
           c_4 = 0  \ .
         \end{cases}
```

Agora são $3 = n-1$ equações LI. As soluções são $c' = 0000$ e $c'' = 0110$. Poder-se-ia concluir que $f$ é 2-para-1 com período $c=0110$. No entanto, a probabilidade de se estar errado nesse caso é a probabilidade de se obter 4 resultados no mesmo subespaço de dimensão 3, sendo que $f$ seria 1-para-1 e os $2^n = 2^4$ resultados seriam equiprováveis: 
```{math}
 \varepsilon_4 \lesssim 1 \cdot 1 \cdot 1 \cdot \frac{2^3}{2^4} = \frac{1}{2}
```
     
Para reduzir a probabilidade de erro, aplica-se a subrotina novamente. Suponha que obtém-se $y^{(5)} = 1111$. Verifica-se se  $y^{(5)} \perp c''$ ou não. Caso não fosse, concluir-se-ia que haveria mais uma equação independente e o sistema só teria solução $c'=0$. Não é esse o caso aqui, pois 
```{math}
 y^{(5)} \cdot c'' = 1111 \cdot 0110 = 0 \oplus 1 \oplus 1 \oplus 0 = 0 \implies y^{(5)} \perp c
```
Poderia concluir-se, nessa etapa, que $f$ é 2-para-1 com probabilidade de erro igual à probabilidade de se sortear aleatoriamente 5 vetores e todos cairem no mesmo subespaço vetorial de dimensão 3:
```{math}
\varepsilon_5 \lesssim 1 \cdot 1 \cdot 1 \cdot \frac{2^3}{2^4}\cdot \frac{2^3}{2^4} = \frac{1}{4}
```
     
Terminando o algoritmo na iteração 5, tem-se que $f$ é 2-para-1 e que o período é $c = 0110$. 
     
A título de curiosidade, a $f$ utilizada neste exemplo é disposta na tabela abaixo, em que $A, B, C, D, E, F, G$ e $H$ denotam 8 palavras distintas de 4 bits.
```{math}
    \begin{array}{c|cccc|c}
     x    & f(x) & & & x & f(x) \\ 1-2 - 5-6
     0000  & A & & & 1000  & E \\
     0001  & B & & & 1001  & F \\
     0010  & C & & & 1010  & G \\
     0011  & D & & & 1011  & H \\
     0100  & C & & & 1100  & G \\
     0101  & D & & & 1101  & H \\
     0110  & A & & & 1110  & E \\
     0111  & B & & & 1111  & F
    \end{array}
```
Repare que, de fato, $f$ é 2-para-1 com $c = 0110$.

## Encontrando o valor do período c -- caso geral

Repetindo a subrotina $m$ vezes, obtém-se os resultados $y^{(1)}, \ldots, y^{(m)}$ das medidas no registrador 1 e o sistema de equações lineares na incógnita $c = c_1 c_2 \ldots c_n$:
```{math}
\begin{cases}
   \ y^{(1)} \cdot c = 0\\
   \ y^{(2)} \cdot c = 0\\
   \ \phantom{y^{(1)} \cdot c} \vdots \\
   \ y^{(m)} \cdot c = 0
  \end{cases} 
```
Esse sistema sempre admite a solução $c = 0$. Supõe-se que se tenha obtido, após a aplicação da subrotina por um número suficiente de vezes, um sistema linear com um número suficiente de equações linearmente independentes (ficará mais claro o que significaria ``suficiente'' nesse contexto). 

Observaçaõ
Para analisar esse sistema, é interessante considerar $\mathbb{B}_n$ como espaço vetorial sobre os escalares $\mathbb{B} = \{ 0,1 \}$ e com a soma de vetores dada pela XOR bit a bit $\oplus$. É possível verificar que esse espaço satisfaz os axiomas de espaço vetorial. Além disso, é possível imitar o produto interno em $\mathbb{R}^n$ ou $\mathbb{C}^n$ com a operação $r\cdot s = r_1 s_1 \oplus \ldots \oplus r_n s_n$. 

O espaço $\mathbb{B}_n$ tem dimensão $n$ e contém $2^n$ vetores. A maioria dos resultados de Álgebra Linear se mantém para esse caso, exceto que esses espaços vetoriais têm um número finito de vetores e que é possível ter $x \neq 0$ e $x \cdot x = 0$, de forma que o produto $\cdot$ não é um produto interno em $\mathbb{B}_n$. Os subespaços de $\mathbb{B}_n$ têm dimensão $2^m, m\leq n$. O subespaço gerado por $c \neq 0$ é $\{0,c\}$ e tem dimensão 1. Se $W$ é um subespaço, então o conjunto $W^\perp$ dos vetores perpendiculares a $W$ é também um subespaço, e vale que $\dim W + \dim W^\perp = \dim \mathbb{B}_n = n$.

Os livros de Códigos Corretores de Erros (da Computação Clássica) costumam denotar $\mathbb{B}$ por $GF(2)$, chamado campo de Galois (Galois field) de dois elementos. 

Se $f$ for 1-para-1, espera-se que o sistema admita apenas a solução trivial $c=0$. Os valores $y^{(1)}, \ldots, y^{(m)}$ podem ser quaisquer dos $2^n$ vetores de bits em $\mathbb{B}_n$, por causa da equação (p2). Como a dimensão de $\mathbb{B}_n$ é $n$, há no máximo $n$ vetores de bits LI nesse espaço. Isso significa que o sistema acima é equivalente a um sistema de $n$ equações LI, e que só admite a solução trivial $c=0$, como esperado.

Por outro lado, se $f$ for 2-para-1, espera-se que o sistema tenha duas soluções: $0$ e $c\neq 0$. Nesse caso, os valores $y^{(1)}, \ldots, y^{(m)}$ são, obrigatoriamente, perpendiculares ao vetor $c$. Se $W$ é o subespaço gerado por $c$, tem-se que  $y^{(1)}, \ldots, y^{(m)} \in W^\perp$ e que $\dim W = 1$ e $\dim W^\perp = n-1$, de forma que $\dim W + \dim W^\perp = \dim \mathbb{B}_n$. Assim, há no máximo $n-1$ vetores LI e perpendiculares a $c$. O sistema (s) é equivalente a um sistema de $n-1$ equações LI, e apresenta uma variável livre $c_j$, que pode assumir os valores 0 ou 1, gerando as soluções $0$ e $c\neq 0$, como era esperado. 

Resumindo, se as $m$ repetições da subrotina quântica do algoritmo de Simon produzirem um sistema de equações com o máximo possível de equações LI, a solução do sistema fornecerá $c$ e, dependendo se há apenas a solução nula ou se, além dessa, há uma solução $c \neq 0$, pode-se distinguir os casos `$f$ é 1-para-1' ou ``$f$ é 2-para-1''. O número de repetições $m$ requerido é proporcional a $n$.

```{note}
Na primeira iteração, o número de vetores que acrescentam informação é $2^n - 1$ dentre os $2^n$ possíveis (apenas o vetor nulo seria útil). Após obter um vetor não nulo, a próxima iteração tem a chance de $2^{n-1} - 1$ entre $2^n$ de resultar num vetor que seja LI com o anterior. 
```

## Probabilidade de erro

Em relação à probabilidade de erro no caso geral, tem-se o seguinte. A partir de um número de iterações suficientemente grande (da ordem de $n$), a cada nova iteração, ou se descobre que $f$ é 1-para-1 (resultado cada vez mais improvável) ou se escolhe que $f$ é 2-para-1 com probabilidade de erro:
```{math}
\varepsilon_m \lesssim \underbrace{1  \ldots  1}_{n-1 \text{ vezes}} \cdot \underbrace{ \frac{2^{n-1}}{2^n} \ldots \frac{2^{n-1}}{2^n}}_{m-(n-1) \text{ vezes}} = \frac{1}{2^{m-n+1}}
```
Essa estimativa não é exata, pois está considerando o caso em que $n-1$ resultados forneceram vetores de bits não-nulos e LI, e os outros resultados cairam no subespaço gerado pelos $n-1$ vetores LI. Poderia ter acontecido de se obter menos vetores LI e os outros cairem no subespaço gerado por eles, apesar de parecer menos provável. Essa estimativa, contudo, serve para dar uma pista quanto à quantidade de iterações do algoritmo quântico. Dessa forma, se o número de iterações $m$ for da ordem de $n$, a probabilidade de erro pode ser feita menor que $1/2$.

## Algoritmo Clássico

### Algorítmo clássico determinístico

Um algoritmo clássico para o Problema de Simon consiste em escolher entradas $x$ em $\mathbb{B}_n$, calcular $f(x)$ e comparar com os outros valores já obtidos, até que se encontre um par de vetores distintos $x_{(1)}$ e $x_{(2)}$ com $f(x_{(1)}) = f(x_{(2)})$ ou até que se possa concluir que $f$ é 1-para-1. 
   
Supondo que seja possível armazenar todas as entradas testadas e seus resultados pela aplicação da $f$, na pior das hipóteses, deve-se calcular $f$ para metade das entradas mais uma, isto é, $2^{n}/2 + 1$ vezes. Caso $f$ seja 1-para-1, todos os resultados seriam distintos, e caso $f$ seja 2-para-1, na pior das hipóteses, na tentativa de número $2^{n}/2 + 1$ será obtido um valor repetido após aplicação da função. 

### Algoritmo Clássico Probabilístico

 Para melhorar o desempenho do algoritmo determinístico acima, pode-se relaxar o desempenho, permitindo-se uma probabilidade de erro $\varepsilon$ na escolha. Sorteia-se aleatoriamente $x$ dentre o conjunto de entradas não testadas ainda, calcula-se $f(x)$ e compara-se o valor obtido com o fornecido pelas entradas já testadas. Repete-se por um número suficiente de tentativas ou até algum par ser encontrado; se nenhum par foi encontrado, decide-se por `$f$ é 1-para-1' e se for encontrado, decide-se por ``$f$ é 2-para-1'' e utiliza-se o par $x_{(1)}, x_{(2)}$ encontrado para calcular $c = x_{(1)}\oplus x_{(2)}$.
      
Após $m$ iterações, o número de pares já testados é $N_{\text{ob}}$, em que
```{math}
N_{\text{ob}} = \binom{m}{2} = \frac{m(m-1)}{2}
```
isto é, o número de pares que se pode formar dentre $m$ elementos distintos sem importar a ordem em que se encontram no par.
   
Caso $f$ seja 2-para-1, o número de pares desejado (ou seja, que resultam no mesmo valor após aplicação de $f$) é $N_{\text{des}}$ dado por
```{math}
N_{\text{des}} = \frac{2^n}{2}
```
   
A probabilidade de pelo menos um par desejado ter sido obtido após $k$ iterações é
```{math}
p_m = \frac{N_{\text{ob}}}{N_{\text{des}}} = \frac{m(m-1)}{2^n}
```
   
Caso nenhum par desejado tenha sido encontrado, opta-se por ``$f$ é 1-para-1'' com probabilidade de erro dada por 
```{math}   
\varepsilon_m = 1 - p_m = 1 - \frac{m(m-1)}{2^n}
```
Para que a probabilidade de erro seja $\varepsilon < 1/2$, deve-se ter
```{math}
\varepsilon_m < \frac{1}{2} \implies  \frac{m(m-1)}{2^n} > \frac{1}{2} \implies m^2 - m - 2^{n-1} > 0
```
Resolvendo para $m > 0$, deve-se ter 
```{math}
m > \frac{1 + \sqrt{1 + 2^{n+1}}}{2}
```
logo $m$ deve ser da ordem de $2^{n/2}$ iterações. 

## Comparação de Desempenho
O desempenho dos algoritmos clássico determinístico, clássico probabilístico e quântico são resumidos na tabela abaixo.

![Screenshot 2024-10-22 at 18-43-52 tcc-giovani pdf](https://github.com/user-attachments/assets/14e9865f-639c-4561-b967-053d35203acc)

Da mesma forma como no problema de Deutsch-Jozsa, essa comparação tem limitações, mas serve como laboratório para testar em que situações a Computação Quântica pode trazer vantagem computacional em relação à Computação Clássica. Em particular, esse é um exemplo em que o algoritmo quântico apresenta ganho exponencial em desempenho em relação aos algoritmos clássicos existentes. 

