# Algoritmo de Deutsch-Jozsa

```{note}
Material extraído do TCC [*Computação Quântica: Uma abordagem para estudantes de graduação em Ciências Exatas*](./tcc-giovani.pdf), de Giovani Goraiebe Pollachini.
```

O Algoritmo de Deutsch-Jozsa é um algoritmo quântico projetado para resolver o Problema de Deutsch-Jozsa. Esse problema não tem especial ênfase em aplicações, mas torna-se laboratório interessante para investigar técnicas e possíveis vantagens da Computação Quântica. A principal referência para esta seção é o livro {cite}`nielsen_quantum_2010`.

 ## Problema de Deutsch-Jozsa

Antes de enunciar o problema de Deutsch-Jozsa é conveniente escrever algumas definições.

**Definição 1:** Função constante e função balanceada.

A função booleana $f \colon \{ 0,1 \}^n \to \{0,1\}$ é dita \emph{constante} se $f$ assume o mesmo valor em todas as entradas:

```{math}
\begin{array}{ll}
       f(x) = 0 \ , \ \ \forall x \in  \{ 0,1 \}^n &  \text{ ou} \\
        f(x) = 1 \ , \ \ \forall x \in  \{ 0,1 \}^n &  \ .
      \end{array} 
```

A função $f$ é dita balanceada se admite o valor $0$ em metade das suas entradas e admite $1$ na metade complementar das entradas.

**Exemplos:**
- A função booleana $f(x) = 1$ é constante.
- Denote $x \in \{ 0,1 \}^n $ por $x = x_{n-1} \ldots x_1 x_0$. A função booleana $f(x) = x_0$ é balanceada, pois para exatamente metade das entradas $x$ tem-se $x_0 = 0$ e para a outra metade, tem-se $x_0 = 1$.
- Considere a função booleana com entradas de $n=2$ bits dada por $f(a,b) = a\cdot b$, em que, lembrando, $\cdot$ representa a porta AND. A tabela verdade dessa função é representada abaixo.
  ```{math}
  \begin{array}
    a & b & f(a,b) = a \cdot b \\ \hline
    0 & 0 & 0 \\
    0 & 1 & 0 \\
    1 & 0 & 0 \\
    1 & 1 & 1 
   \end{array}
  ```
Essa função não é balanceada nem constante.
O problema desta seção tem o seguinte enunciado:

**Problema de Deutsch-Jozsa**

Seja uma função booleana $f \colon \{ 0,1 \}^n \to \{0,1\}$ que pode ser apenas ou constante ou balanceada. Decidir se $f$ é constante ou balanceada. 

Deseja-se, dada uma função $f$ considerada como caixa preta, e com o compromisso de ser ou constante ou balanceada, decidir qual dos dois casos mutuamente excludentes é verdadeiro.

## Algoritmo de Deutsch-Jozsa

Para resolver o problema de Deutsch-Jozsa com um algoritmo quântico, é necessário ter uma versão quântica da função booleana $f$, dada como oráculo, isto é, dada como uma caixa preta em que não se pode visualizar a subrotina que calcula $f$. 

Considere que $f$ seja dada por meio do oráculo de fase. O algoritmo de Deutsch-Jozsa para decidir se $f$ é constante ou balanceada é dado pelo procedimento abaixo.


$\textbf{Entrada:}$ $O_\text{F}(f) = O$ \ \ (oráculo de fase associado à função booleana $f$)

**Procedimento:**
```{math}
\begin{array}
   \text{etapa 0:} & \ket{0}^{\otimes n} & \text{preparação do estado inicial} \\
   \text{etapa 1:} & \ket{+}^{\otimes n} & \text{superposição de estados com $H^{\otimes n}$} \\
   \text{etapa 2:} & O_\text{F}\ket{+}^{\otimes n} & \text{aplicação de $f$ (oráculo de fase)} \\
   \text{etapa 3:} & \bra{+}^{\otimes n}O_\text{F}\ket{+}^{\otimes n} & \text{testar para $\ket{+}^{\otimes n}$ (base girada $\mathcal{X}$)} \\
  \end{array}
```
```{math}
\textbf{Saída:} Probabilidade da medida de $\ket{\psi_2}$ resultar em  $\ket{+}^{\otimes n}$ é 
```
```{math}
\begin{cases}
   1 & \text{se $f$ é constante} \\
   0 & \text{se $f$ é balanceada}
   \end{cases}
```
Portanto, se o estado após a medida na base $\mathcal{X}$ for $\ket{+}^{\otimes n}$, então decide-se que $f$ é constante. E se o estado após a medida for qualquer outro, decide-se que $f$ é balanceada.

**Circuito**
Notação compacta:

![Screenshot 2024-10-21 at 21-36-58 tcc-giovani pdf](https://github.com/user-attachments/assets/c87b9623-6b93-42f4-8d8b-e0523541e220)

Notação expandida:

![Screenshot 2024-10-21 at 21-39-14 tcc-giovani pdf](https://github.com/user-attachments/assets/40deec9d-429e-4905-a41b-25602d6257f8)

Observação: A porção destacada na figura corresponde à medição na base $\mathcal{X}$ feita a partir da medição na base computacional. De fato, o operador de Hadamard realiza mudança de base de $\mathcal{X}$ (base girada) para $\mathcal{I}$ (base computacional), de forma que o resultado medido na base computacional corresponde a uma medição na base $\mathcal{X}$. A figura ilustra a medição na base girada feita em função da medição na base computacional.  

![Screenshot 2024-10-21 at 21-40-04 tcc-giovani pdf](https://github.com/user-attachments/assets/1725d836-df4b-41c7-886a-f4c0273d5178)


Análise detalhada do algoritmo:

Na etapa 1, aplica-se $H$ para cada qubit de entrada, resultando em:

```{math}
\begin{split}
    \ket{\psi_1} 
    &= H^{\otimes n} \ket{0}^{\otimes n} \\
    &= \ket{+}^{\otimes n} \\
    &= \left(\frac{\ket{0} + \ket{1}}{\sqrt{2}} \right) \ldots \left(\frac{\ket{0} + \ket{1}}{\sqrt{2}} \right) \\
    &= \frac{1}{\sqrt{2^n}} \sum_{x \in \mathbb{B}_n} \ket{x} \ ,
   \end{split}
```
em que $\mathbb{B}_n$ representa o conjunto de todas as palavras de $n$ bits. Isto é, 

```{math}
\begin{split}
       \mathbb{B}_n 
       &= \{ 0\ldots 00 \, , \, \, 0 \ldots 01 \, , \, \, 0\ldots 10 \, , \, \, 0 \ldots 11 \, , \, \, \ldots \, , \, \, 1 \ldots 11 \}  \\
       &= \{ 0, 1, 2, 3, \ldots, 2^n-1 \}  \ .
     \end{split}
```
Observação: or vezes é útil fazer a identificação entre vetores de bits e números inteiros sem sinal, para simplificar a notação. Por exemplo, $0 = 0\ldots000$, $1 = 0\ldots001$, $2 = 0\ldots010$, $3 = 0\ldots011$ e assim por diante, até $2^n-1 = 1 \ldots 111$. Essa identificação consta na tabela \ref{cap1:tab_vetor_bits_representacao_nros_inteiros} do apêndice \ref{cap1_comp_classica}.

A aplicação do oráculo na etapa 2 fornece:

```{math}
\begin{split}
    \ket{\psi_2} 
    &= O_\text{F} \ket{\psi_1}  \\
    &= \frac{1}{\sqrt{2^n}} \sum_{x \in \mathbb{B}_n} O \ket{x} \\
    &= \frac{1}{\sqrt{2^n}} \sum_{x \in \mathbb{B}_n} (-1)^{f(x)} \ket{x} \ .
    \end{split} 
```
 Se a função for constante, o fator $(-1)^{f(x)}$ se tornará um sinal global $+$ ou $-$, que essencialmente não altera o estado anterior. 
    
A última etapa consiste na medição na base girada $\mathcal{X}$. Para realizar essa medida, pode-se aplicar $H$ a todos os qubits e medir na base computacional. Calculando a probabilidade de se obter $\ket{+}^{\otimes n}$, consegue-se:

```{math}
\begin{split}
    \bra{+}^{\otimes n} \ket{\psi_2}
    &= \left( \frac{1}{\sqrt{2^n}} \sum_{y \in \mathbb{B}_n} \bra{y} \right) \frac{1}{\sqrt{2^n}} \sum_{x \in \mathbb{B}_n} (-1)^{f(x)} \ket{x} \\
    &= \frac{1}{2^n} \sum_{x \in \mathbb{B}_n} \sum_{y \in \mathbb{B}_n} (-1)^{f(x)}  \bra{y}\ket{x} \\
    &= \frac{1}{2^n} \sum_{x \in \mathbb{B}_n} \sum_{y \in \mathbb{B}_n} (-1)^{f(x)}  \delta_{x,y} \\
    &= \frac{1}{2^n} \sum_{x \in \mathbb{B}_n}  (-1)^{f(x)} \ .
    \end{split}
```

Caso a função seja constante, a última equação fornece
```{math}
\frac{1}{2^n} \sum_{x \in \mathbb{B}_n}  (-1)^{f(x)} =   \pm \frac{1}{2^n} 2^n = \pm 1
```
E caso a função seja balanceada, metade das parcelas contribui com $1$ e a outra metade com $-1$, portanto
```{math}
\frac{1}{2^n} \sum_{x \in \mathbb{B}_n}  (-1)^{f(x)} =    \frac{1}{2^n} 0 = 0
```
A probabilidade $P$ de se obter $\ket{+}^{\otimes n}$ é dada pelo módulo ao quadrado do resultado obtido, logo
```{math}
P = |\bra{+}^{\otimes n} \ket{\psi_2}|^2 = \begin{cases}
   1 & \text{se $f$ é constante} \\
   0 & \text{se $f$ é balanceada} \ .
   \end{cases}
```
Dessa forma, decide-se por '$f$ é constante' se a medida resultar no estado $\ket{+}^{\otimes n}$ e por `$f$ é balanceada', se resultar em um estado diferente. Esse teste é realizado no algoritmo por uma mudança de base, realizada pela porta Hadamard, e uma medição na base computacional.

## Algorítimo clássico

Agora considere o problema de Deutsch-Jozsa no contexto clássico. Tem-se $f$ dada como uma caixa preta e se quer decidir se $f$ é constante ou balanceada. A seguir serão vistas brevemente as abordagens clássicas determinística e aleatória para o problema. 

### Algoritmo Clássico Determinístico

A Computação Clássica Determinística é um tipo de computação em que se busca algoritmos que não façam uso de recursos probabilísticos para resolver um problema. Os algoritmos determinísticos são tais que, ao serem executados diversas vezes para uma mesma entrada, produz-se sempre a mesma saída. Para que se resolva o problema nesse tipo de computação, é necessário realizar aplicações sucessivas de $f$ para diversas entradas até se ter certeza de qual opção é válida (se $f$ é constante ou balanceada). Por exemplo\footnote{Nesta parte, usou-se a notação que confunde uma palavra de bits com sua representação por número inteiro sem sinal. Ver observação \ref{cap5:rmk_notacao_vetor_bits_nro_inteiro}.}, calcula-se $f(0)$, $f(1)$, $f(2)$, $\ldots$ e se verifica se $f(1) = f(0)$, $f(2) = f(1)$, $\ldots$ ou não. Caso ocorra $f(j) \neq f(i)$, então a opção certa é `$f$ é balanceada', e caso isso não ocorra, a opção correta é ``$f$ é constante''. 
  
Para se distinguir com certeza as duas opções, deve-se aplicar $f$ a metade das entradas possíveis mais uma, ou seja, a $2^n/2 + 1$ entradas. Isso porque, na pior das hipóteses, a função era balanceada e, obteve-se um mesmo resultado, por azar, para as $2^n/2$ entradas testadas, impedindo que se faça a escolha com certeza.
  
Dessa forma, o custo computacional desse algoritmo é de $2^n/2 + 1$ aplicações de $f$.

### Algoritmo Clássico Probabilístico

Um algoritmo probabilístico utiliza a probabilidade como recurso computacional. Para esse tipo de computação, é possível que entradas iguais produzam saídas diferentes, e que a máquina passe por estados diferentes durante a computação, em função de fatores probabilísticos presentes no algoritmo. 

Nesse contexto, se for permitida uma probabilidade de erro $\varepsilon$ na decisão e o uso de sorteios aleatórios em certas etapas, é possível reduzir o custo computacional do algoritmo clássico determinístico. 
  
Primeiramente, permite-se que as entradas $i$ sejam tiradas aleatoriamente, cada uma com mesma probabilidade $p(i) = 1/2^n$. Por exemplo, se $f$ for constante $1$ ($f(i) = 1 \forall j$), a probabilidade de resultar $1$ é $1 = 100\%$ e a de resultar $0$ é $0 = 0\%$. Se $f$ for balanceada, a probabilidade de resultar $1$ é $0,\!5 = 50\%$ e o mesmo vale para o resultado $0$. Supõe-se, para simplificar a discussão, que o sorteio das entradas é feito sem memória\footnote{Para um número de bits $n$ grande, esse caso é semelhante ao caso com memória, em que não se permite repetir as entradas no sorteio.}, isto é, com chance de se sortear duas entradas iguais.

![Screenshot 2024-10-21 at 21-41-59 tcc-giovani pdf](https://github.com/user-attachments/assets/db2e48e7-6a00-41a1-8905-aa12cfd7a000)

A primeira avaliação $f(i_1)$ não traz mais informação para distinguir entre constante e balanceada. 

![Screenshot 2024-10-21 at 21-42-54 tcc-giovani pdf](https://github.com/user-attachments/assets/b84e214a-ce17-42ac-a00a-5210411439f1)

A segunda aplicação, se resultar $f(i_2) \neq f(i_1)$, já resolve com certeza que $f$ é balanceada. 

![Screenshot 2024-10-21 at 21-43-27 tcc-giovani pdf](https://github.com/user-attachments/assets/0d8acb32-9101-4791-a3b7-d0d791d49616)

Se o resultado for $f(i_2) = f(i_1)$, tende-se a pensar que $f$ seria constante e a probabilidade de se estar errado é a probabilidade de tirar duas saídas iguais aleatoriamente numa função balanceada, ou seja, $P_e = 1 \cdot 0,\!5 = 0,\!5$. 

![Screenshot 2024-10-21 at 21-43-57 tcc-giovani pdf](https://github.com/user-attachments/assets/747d0bce-4668-4868-ad81-ef6920f350a6)


Na terceira etapa, caso $f(i_3) \neq f(i_2)$, resolve-se com certeza que $f$ é balanceada e caso $f(i_3) = f(i_2)$, conclui-se pela opção constante com probabilidade de erro igual a $P_e = 1 \cdot 0,\!5 \cdot 0,\!5 = 0,\!25$, correspondente à probabilidade de que, numa função balanceada, tenha-se o mesmo resultado para 3 entradas sorteadas aleatoriamente com igual probabilidade. 

![Screenshot 2024-10-21 at 21-45-05 tcc-giovani pdf](https://github.com/user-attachments/assets/a6fd247c-5616-4402-bc15-1c66f27633e0)

![Screenshot 2024-10-21 at 21-45-29 tcc-giovani pdf](https://github.com/user-attachments/assets/2d7eee0d-5c3c-4535-a1fc-77ad08208010)

Seguindo essa ideia, na $m$-ésima aplicação de $f$, se ocorrer $f(i_m) \neq f(i_{m-1})$, conclui-se com certeza a opção `$f$ é balanceada' e se $f(i_m) = f(i_{m-1})$, pode-se concluir que ``$f$ é constante'' com probabilidade de erro 

```{math}
P_e = 1 \cdot 0,\!5 \cdot \ldots \cdot 0,\!5 = (0,\!5)^{m-1} = 1/2^{m-1}
```

Para uma probabilidade de erro  $P_e < 1/2$ na decisão, deve-se repetir o algoritmo até que a probabilidade de erro $P_{e,m} = 1/2^{m-1}$ satisfaça

```{math}
\frac{1}{2^{m-1}} < \frac{1}{2} \implies 2^m > 2^2 \implies m >2 \implies m \geq 3
```

Se forem $m=3$ aplicações, a probabilidade de erro será limitada por $\varepsilon = 1/2^{m-1} = 0,\!25 < 0,\!5$, como visto anteriormente.

## Comparação de desempenho 

A tabela abaixo traz a comparação entre o desempenho dos algoritmos clássico determinístico, clássico probabilístico e quântico. 

![Screenshot 2024-10-21 at 21-46-13 tcc-giovani pdf](https://github.com/user-attachments/assets/ddbc9d1b-c6fd-44aa-b022-9df9fa7db288)

Essa comparação entre o desempenho clássico e quântico, no entanto, não pode ser considerada muito seriamente. Há que se levar em conta que são arquiteturas diferentes: aplicar uma operação $f$ clássica (correspondente a chamar uma subrotina ``caixa preta'') e aplicar o oráculo de fase $O_\text{F}(f)$ em um circuito quântico são coisas distintas. Não é claro que essas operações têm custo computacional equivalente para que sejam comparadas diretamente como na tabela apresentada. Por outro lado, como comparação simplificada, essa análise serve para se ter uma noção dos ganhos que a Computação Quântica poderia trazer em relação a Computação Clássica. 

Em relação ao algoritmo clássico determinístico, o algoritmo quântico apresenta ganho exponencial em desempenho. Já em relação ao algoritmo clássico probabilístico, o desempenho é semelhante.
