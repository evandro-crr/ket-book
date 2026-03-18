# Entropia de von Neumann

A **entropia de von Neumann** é uma das quantidades mais fundamentais da teoria da informação quântica. Ela generaliza a entropia de Shannon, usada na teoria da informação clássica, para sistemas descritos pela mecânica quântica. Sua função principal é quantificar a **quantidade de incerteza, desordem ou informação contida em um estado quântico**.

Em sistemas clássicos, a entropia mede a incerteza associada a uma distribuição de probabilidades. No contexto quântico, porém, os estados de um sistema podem estar em **superposição** e apresentar **entrelaçamento**, exigindo uma formulação mais geral para medir informação. A entropia de von Neumann surge exatamente como essa extensão natural, sendo definida para estados descritos por **matrizes densidade**.

Essa medida desempenha um papel central em diversos resultados fundamentais da teoria da informação quântica, incluindo compressão de informação quântica, limites de comunicação e análise de correlações entre sistemas quânticos.

## Definição

Considere um sistema quântico descrito por uma matriz densidade $ \rho $. A **entropia de von Neumann** é definida como

$$
S(\rho) = - \mathrm{Tr}(\rho \log \rho)
$$

onde $ \mathrm{Tr} $ representa o traço da matriz.

Se $ \lambda_i $ são os autovalores da matriz densidade $ \rho $, a entropia pode ser escrita de forma equivalente como

$$
S(\rho) = - \sum_i \lambda_i \log \lambda_i
$$

Essa expressão evidencia a forte relação com a **entropia de Shannon**, pois os autovalores da matriz densidade formam uma distribuição de probabilidades.

Em muitas aplicações utiliza-se o logaritmo na base 2, fazendo com que a entropia seja medida em **bits**.

## Estados puros e estados mistos

Uma das interpretações mais importantes da entropia de von Neumann é sua capacidade de distinguir **estados puros** de **estados mistos**.

Um estado quântico puro é descrito por uma matriz densidade da forma

$$
\rho = \ket{\psi}\bra{\psi}
$$

Nesse caso, a matriz densidade possui apenas um autovalor igual a 1 e os demais iguais a 0. Como consequência,

$$
S(\rho) = 0
$$

Isso significa que **não há incerteza intrínseca no estado quântico**.

Por outro lado, um **estado misto** representa uma distribuição estatística de estados quânticos. Nesse caso, a matriz densidade possui múltiplos autovalores diferentes de zero, e a entropia torna-se positiva. Quanto maior a mistura do estado, maior será sua entropia.

Assim, a entropia de von Neumann mede o **grau de mistura de um estado quântico**.

## Exemplos

### Exemplo 1 — Estado puro

Considere o estado quântico

$$
\rho =
\begin{pmatrix}
1 & 0 \\
0 & 0
\end{pmatrix}
$$

Os autovalores dessa matriz são

$$
\lambda_1 = 1, \quad \lambda_2 = 0
$$

Aplicando a definição da entropia:

$$
S(\rho) = - (1 \log 1 + 0 \log 0)
$$

Como $ \log 1 = 0 $, obtemos

$$
S(\rho) = 0
$$

Esse resultado mostra que **estados puros possuem entropia zero**, pois não há incerteza sobre o estado do sistema.

### Exemplo 2 — Estado maximamente misto

Considere agora o estado

$$
\rho =
\frac{1}{2}
\begin{pmatrix}
1 & 0 \\
0 & 1
\end{pmatrix}
$$

Os autovalores são

$$
\lambda_1 = \frac{1}{2}, \quad \lambda_2 = \frac{1}{2}
$$

Calculando a entropia:

$$
S(\rho) =
- \left(
\frac{1}{2}\log_2\frac{1}{2} +
\frac{1}{2}\log_2\frac{1}{2}
\right)
$$

Como $ \log_2 \frac{1}{2} = -1 $, obtemos

$$
S(\rho) = 1
$$

Esse estado é chamado de **estado maximamente misto**, pois representa a maior incerteza possível para um único qubit.

### Exemplo 3 — Estado parcialmente misto

Considere o estado

$$
\rho =
\begin{pmatrix}
0.8 & 0 \\
0 & 0.2
\end{pmatrix}
$$

Os autovalores são $0.8$ e $0.2$. A entropia é

$$
S(\rho) =
-(0.8 \log_2 0.8 + 0.2 \log_2 0.2)
$$

Calculando aproximadamente,

$$
S(\rho) \approx 0.72
$$

Esse valor mostra que o estado possui **incerteza intermediária**: ele não é puro, mas também não é completamente misto.

## Entropia em sistemas compostos

A entropia de von Neumann também desempenha um papel fundamental no estudo de **sistemas quânticos compostos**.

Considere um sistema formado por duas partes $A$ e $B$, descrito por uma matriz densidade conjunta $ \rho_{AB} $. Podemos definir as matrizes densidade reduzidas

$$
\rho_A = \mathrm{Tr}_B(\rho_{AB})
$$

$$
\rho_B = \mathrm{Tr}_A(\rho_{AB})
$$

A entropia dessas matrizes fornece informações importantes sobre as **correlações entre os subsistemas**.

Um resultado particularmente interessante ocorre quando o estado total $ \rho_{AB} $ é puro, mas os subsistemas possuem entropia positiva. Isso acontece quando os sistemas estão **entrelaçados**.

### Exemplo — Estado de Bell

Considere o estado entrelaçado

$$
\ket{\Phi^+} =
\frac{1}{\sqrt{2}}(\ket{00} + \ket{11})
$$

O estado total possui entropia

$$
S(\rho_{AB}) = 0
$$

pois é um estado puro.

No entanto, a matriz densidade reduzida de cada qubit é

$$
\rho_A =
\frac{1}{2}
\begin{pmatrix}
1 & 0 \\
0 & 1
\end{pmatrix}
$$

Assim,

$$
S(\rho_A) = 1
$$

Isso mostra que **cada subsistema individualmente parece completamente misto**, mesmo que o sistema total esteja em um estado puro. Esse fenômeno é uma assinatura do **entrelaçamento quântico**.

## Papel na teoria da informação quântica

A entropia de von Neumann aparece em diversos resultados centrais da teoria da informação quântica.

Ela é fundamental na formulação do **teorema de compressão quântica de Schumacher**, que mostra como estados quânticos podem ser comprimidos de forma eficiente quando existe redundância estatística.

Também aparece em resultados relacionados à **capacidade de canais quânticos**, determinando limites fundamentais para a transmissão de informação. Um exemplo importante é o **teorema de Holevo**, que estabelece limites para a quantidade de informação clássica que pode ser extraída de estados quânticos.

Além disso, a entropia de von Neumann é amplamente utilizada no estudo de **entrelaçamento quântico**, correlações quânticas e termodinâmica quântica.

## Importância

A entropia de von Neumann é considerada uma das quantidades centrais da teoria da informação quântica. Ela fornece uma forma natural de quantificar informação, incerteza e correlações em sistemas quânticos.

Seu papel vai além da computação quântica, sendo também essencial em áreas como **comunicação quântica, física da matéria condensada, termodinâmica quântica e teoria de campos quânticos**.

Assim como a entropia de Shannon revolucionou a teoria da informação clássica, a entropia de von Neumann tornou-se uma ferramenta fundamental para compreender **os limites e possibilidades da informação no mundo quântico**.