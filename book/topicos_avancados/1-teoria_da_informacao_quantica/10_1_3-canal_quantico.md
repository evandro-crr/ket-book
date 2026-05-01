# Canais Quânticos

Na prática, sistemas quânticos raramente evoluem de forma perfeitamente isolada. Interações com o ambiente, ruído experimental e imperfeições de hardware fazem com que os estados quânticos sofram transformações não ideais. A teoria de **canais quânticos** fornece o formalismo matemático utilizado para descrever essas transformações.

Um **canal quântico** representa a evolução mais geral possível de um estado quântico físico. Diferentemente das evoluções unitárias ideais usadas em circuitos quânticos, os canais quânticos permitem modelar processos como **decoerência, dissipação, perda de informação e ruído**.

Essa estrutura é fundamental em diversas áreas da computação quântica e da teoria da informação quântica, incluindo **comunicação quântica, correção de erros quânticos, caracterização de hardware e capacidade de transmissão de informação**.

## Definição

Um **canal quântico** é uma aplicação linear

$$
\Phi : \rho \rightarrow \Phi(\rho)
$$

que transforma uma matriz densidade $\rho$ em outra matriz densidade válida.

Para que essa transformação represente um processo físico possível, ela deve satisfazer duas propriedades fundamentais:

**Preservação do traço**

$$
\mathrm{Tr}(\Phi(\rho)) = 1
$$

Isso garante que o estado resultante continua sendo um estado físico válido.

**Completamente positiva**

A aplicação deve ser positiva mesmo quando estendida para sistemas maiores. Essa propriedade garante que o canal permanece físico mesmo quando o sistema está **entrelaçado com outros sistemas**.

Transformações que satisfazem essas duas propriedades são chamadas de **mapas completamente positivos que preservam o traço (CPTP maps)**.

## Representação de Kraus

Uma forma muito comum de representar canais quânticos é através da **representação de Kraus**. Nesse formalismo, um canal quântico pode ser escrito como

$$
\Phi(\rho) = \sum_k K_k \rho K_k^\dagger
$$

onde os operadores $K_k$ são chamados de **operadores de Kraus**.

Para que o canal preserve o traço, os operadores devem satisfazer

$$
\sum_k K_k^\dagger K_k = I
$$

Essa representação é extremamente útil porque permite modelar muitos processos físicos comuns em sistemas quânticos.

## Exemplos de canais quânticos

### Canal unitário

O caso mais simples de canal quântico corresponde a uma evolução unitária. Nesse caso,

$$
\Phi(\rho) = U \rho U^\dagger
$$

onde $U$ é um operador unitário.

Esse tipo de canal descreve a evolução ideal de um sistema quântico isolado, como a aplicação de portas quânticas em um circuito.

### Canal de despolarização

O **canal despolarizante** modela um tipo de ruído em que o estado quântico é parcialmente substituído por um estado maximamente misto.

$$
\Phi(\rho) = (1-p)\rho + p\frac{I}{2}
$$

onde $p$ representa a probabilidade de ocorrência do ruído.

Quando $p=1$, o estado final torna-se completamente misto.

### Canal de damping de amplitude

Esse canal modela processos físicos de **perda de energia**, como a emissão espontânea de um fóton.

Ele pode ser descrito por operadores de Kraus da forma

$$
K_0 =
\begin{pmatrix}
1 & 0 \\
0 & \sqrt{1-\gamma}
\end{pmatrix}
$$

$$
K_1 =
\begin{pmatrix}
0 & \sqrt{\gamma} \\
0 & 0
\end{pmatrix}
$$

onde $\gamma$ representa a probabilidade de decaimento.

Esse canal é frequentemente usado para modelar **relaxação em qubits físicos**.

## Interpretação física

Uma forma intuitiva de compreender canais quânticos é imaginar que o sistema quântico interage com um **ambiente externo**.

Inicialmente, o sistema pode estar em um estado $\rho$, enquanto o ambiente está em algum estado $\ket{e_0}$. O sistema conjunto evolui de forma unitária:

$$
U(\rho \otimes \ket{e_0}\bra{e_0})U^\dagger
$$

Se ignorarmos o ambiente (realizando o traço parcial), obtemos a evolução efetiva do sistema:

$$
\Phi(\rho) = \mathrm{Tr}_E\left(U(\rho \otimes \ket{e_0}\bra{e_0})U^\dagger\right)
$$

Esse procedimento mostra que **qualquer canal quântico pode ser interpretado como uma interação unitária com um ambiente seguida do descarte desse ambiente**.

## Importância na teoria da informação quântica

Os canais quânticos desempenham um papel central em diversas áreas da informação quântica.

Na **comunicação quântica**, eles modelam os meios físicos usados para transmitir informação, como fibras ópticas ou canais atmosféricos.

Na **computação quântica**, são utilizados para descrever ruído em dispositivos NISQ e para desenvolver técnicas de **mitigação e correção de erros**.

Além disso, a análise de canais quânticos permite estudar **limites fundamentais de transmissão de informação**, incluindo a capacidade de transmitir informação clássica e quântica de forma confiável.

Assim, a teoria de canais quânticos constitui uma das estruturas matemáticas mais importantes para compreender **como a informação evolui e se degrada em sistemas quânticos reais**.