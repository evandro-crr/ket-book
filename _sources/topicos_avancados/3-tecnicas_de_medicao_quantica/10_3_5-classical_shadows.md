# Classical Shadows

:::{admonition} Referências
Material adaptado da dissertação [*Classical Shadows para algoritmos quânticos de feedback*](https://repositorio.ufsc.br/handle/123456789/265955) de Leticia Bertuzzi, desenvolvida no Programa de Pós-Graduação em Física da Universidade Federal de Santa Catarina.
:::

## Introdução

Em algoritmos quânticos, especialmente algoritmos variacionais e procedimentos de otimização, grande parte das informações úteis do sistema é obtida através de medições. Entretanto, medir um estado quântico é um processo delicado: ao realizar uma medida, a função de onda colapsa e parte da informação do sistema é perdida. Esse problema se torna ainda mais relevante quando desejamos caracterizar estados quânticos complexos compostos por muitos qubits. 

Na tentativa de reconstruir ou estimar propriedades de sistemas quânticos, diversas técnicas de tomografia quântica foram desenvolvidas, como a tomografia de estados tradicional, Local Quantum Overlapping Tomography (LQOT) e métodos baseados em redes neurais. Entre essas abordagens, destaca-se a técnica de **Classical Shadows (CS)**, proposta por Huang, Kueng e Preskill em 2020. 

A principal motivação do protocolo de Classical Shadows é reduzir drasticamente o número de medições necessárias para estimar propriedades de um sistema quântico. Em vez de reconstruir completamente a matriz densidade do sistema — tarefa exponencialmente custosa — o protocolo busca armazenar apenas informações suficientes para prever observáveis específicos com alta precisão. 

Uma das características mais importantes do método é que sua complexidade amostral cresce apenas de forma logarítmica com o número de observáveis que desejamos estimar. Isso representa uma vantagem significativa em comparação com métodos tradicionais de tomografia quântica, cuja complexidade cresce exponencialmente com o número de qubits. 

## Motivação Física

A tomografia quântica tradicional busca reconstruir completamente a matriz densidade de um sistema quântico. Para isso, é necessário preparar o mesmo estado diversas vezes e realizar medições em diferentes bases. O problema é que a quantidade de coeficientes necessários para descrever a matriz densidade cresce exponencialmente com o número de qubits. Consequentemente, o custo experimental e computacional rapidamente se torna inviável para sistemas maiores. 

O protocolo de Classical Shadows surge justamente para contornar essa limitação. A ideia central não é reconstruir integralmente o estado quântico, mas sim gerar uma representação clássica compacta contendo informação suficiente para estimar múltiplos observáveis posteriormente. Essa representação é chamada de **sombra clássica** (*classical shadow*). 

O aspecto revolucionário do método está no fato de que o mesmo conjunto de medições pode ser reutilizado para prever diferentes propriedades do sistema. Assim, uma única aquisição experimental pode servir para calcular fidelidade, correlações, observáveis locais, energia de Hamiltonianos e propriedades de emaranhamento sem necessidade de repetir completamente o experimento. 

## Ideia Central do Protocolo

O protocolo de Classical Shadows pode ser entendido como um procedimento dividido em três etapas principais:

1. Aplicação de rotações aleatórias;
2. Medição do estado quântico;
3. Pós-processamento clássico para reconstrução das sombras.

Inicialmente, escolhe-se aleatoriamente uma base de medição. Para medições de Pauli, utiliza-se o conjunto:

$$
U \in \\{H, HS^\dagger, I\\},
$$

onde:

* $H$ é a porta de Hadamard;
* $S$ é a porta de fase;
* $I$ é a identidade.

Essas operações realizam mudanças de base para os autovetores dos operadores de Pauli $X$, $Y$ e $Z$. 

As matrizes correspondentes são:

$$
H=\frac{1}{\sqrt{2}}\begin{pmatrix}1&1\\1&-1\end{pmatrix},\quad S=\begin{pmatrix}1&0\\0&i\end{pmatrix}
$$

Após aplicar uma rotação aleatória ao estado quântico $\rho$, realiza-se uma medição na base computacional. O resultado da medida corresponde a uma string binária, como por exemplo:

$$
\ket{010101}.
$$

Essa sequência representa o colapso do sistema após a medição projetiva. 

### Fotografias Clássicas

Depois da medição, aplica-se a rotação inversa ao estado colapsado:

$$
\rho'' = U^{\dagger}\ket{\hat{b}}\bra{\hat{b}}U
$$

Essa matriz recebe o nome de **fotografia clássica** (*classical snapshot*). Ela representa uma descrição clássica parcial do estado quântico original. 

O termo “clássico” aparece porque o resultado final das medições é armazenado como dados clássicos — bits — que posteriormente são processados computacionalmente.

O procedimento completo pode ser interpretado formalmente como um canal quântico:

$$
\mathcal{M}(\rho)=\mathbb{E}\left[U^{\dagger}\ket{\hat{b}}\bra{\hat{b}}U\right]
$$

A partir da inversão desse canal, obtemos um estimador para a matriz densidade:

$$
\hat{\rho}=\mathcal{M}^{-1}\left(U^{\dagger}\ket{\hat{b}}\bra{\hat{b}}U\right)
$$

A média desses estimadores permite reconstruir propriedades estatísticas do sistema original. 

## Classical Shadows para Medições de Pauli

No caso específico de medições de Pauli, a expressão para a reconstrução de um qubit é particularmente simples:

$$
\hat{\rho}=3U^{\dagger}\ket{\hat{b}}\bra{\hat{b}}U-I
    $$

onde $I$ representa a matriz identidade $2\times2$. 

Para sistemas de múltiplos qubits, generaliza-se o procedimento utilizando produtos tensoriais:

$$
\hat{\rho}^{(m)}=\bigotimes_{j=1}^{n}\left(3U_j^{(m)\dagger}\ket{b_j^{(m)}}\bra{b_j^{(m)}}U_j^{(m)}-I\right)
$$

Cada repetição do experimento produz uma nova fotografia clássica. Repetindo o procedimento $N$ vezes, obtemos a sombra clássica:

$$
S(\rho;N)={\hat{\rho}_1,\ldots,\hat{\rho}_N}
$$

## Estimativa de Observáveis

Após construir as sombras clássicas, podemos estimar observáveis do sistema quântico.

Seja $O_j$ um observável qualquer. Seu valor esperado pode ser calculado através da média:

$$
\langle O_j\rangle=\frac{1}{N}\sum_{m=1}^{N}\mathrm{Tr}(O_j\hat{\rho}^{(m)})
$$

Assim, utilizando apenas um único conjunto de sombras clássicas, conseguimos prever simultaneamente vários observáveis diferentes do sistema. 

Isso é uma das maiores vantagens do protocolo: o reaproveitamento das medições para múltiplas estimativas.

### Complexidade Amostral

A quantidade de medições necessárias para obter boas estimativas é chamada de **complexidade amostral**.

Para observáveis de Pauli, ela pode ser escrita como:

$$
N=\mathcal{O}\left(\frac{3^w\log(L)}{\varepsilon^2}\right)
$$

onde:

* $L$ é o número de observáveis;
* $\varepsilon$ é o erro máximo permitido;
* $w$ é a localidade do operador.



A localidade $w$ corresponde ao número de matrizes de Pauli não triviais presentes no operador. Quanto menor a localidade, mais eficiente o protocolo se torna.

Esse resultado mostra que o número de medições cresce apenas logaritmicamente com o número de observáveis, característica fundamental do Classical Shadows. 

Para observáveis mais gerais, existe ainda uma formulação mais ampla da complexidade amostral:

$$
N=2\log\left(\frac{2L}{\delta}\right)\frac{34}{\varepsilon^2}\max_{1\leq i\leq L}\left|O_i-\frac{\mathrm{Tr}(O_i)}{2^n}I\right|_{shadow}^2
$$

onde $\delta$ representa a probabilidade de falha da estimativa. 

## Versões do Protocolo

Atualmente existem diferentes variantes da técnica de Classical Shadows.

### Classical Shadows Randomizado

Na versão tradicional, as unitárias são escolhidas aleatoriamente do conjunto:

$$
{H, HS^\dagger, I}.
$$

Essa é a abordagem utilizada na maior parte dos trabalhos introdutórios. 

### Derandomized Classical Shadows

Na versão *derandomized*, as direções de medição são escolhidas de maneira estratégica em vez de puramente aleatória. Isso pode reduzir o número de medições necessárias em alguns problemas específicos. 

### Locally-Biased Classical Shadows

A versão enviesada localmente (*Locally-Biased Classical Shadows — LBCS*) modifica a distribuição de probabilidade das medições.

Por exemplo, se os observáveis de interesse dependem apenas das direções $X$ e $Z$, então medições na direção $Y$ podem ser removidas do protocolo, reduzindo custos experimentais. 

## Aplicações de Classical Shadows

### Fidelidade Quântica

Uma das aplicações mais importantes é a estimativa de fidelidade entre estados quânticos.

A fidelidade entre dois estados $\rho$ e $\sigma$ é definida por:

$$
F(\rho,\sigma)=\mathrm{Tr}\sqrt{\rho\sigma\rho}
$$

Experimentos numéricos mostraram que Classical Shadows consegue estimar fidelidades de estados GHZ com alta precisão mesmo conforme o número de qubits cresce. 

### Química Quântica

Classical Shadows também possui aplicações relevantes em algoritmos variacionais como o VQE (*Variational Quantum Eigensolver*). 

Em problemas de química quântica, Hamiltonianos moleculares podem ser decompostos em operadores de Pauli, permitindo que a técnica seja utilizada para estimar energias moleculares com menos medições.

Estudos envolvendo moléculas como:

* $H_2$
* $LiH$
* $BeH_2$
* $H_2O$
* $NH_3$

demonstraram redução significativa da variância utilizando versões enviesadas do protocolo. 

### Estimativa de Propriedades Globais

Outro tema recente envolve o uso de Classical Shadows para estimar propriedades globais como:

* entropia;
* pureza;
* emaranhamento.

Embora o protocolo seja eficiente para observáveis locais, estimar propriedades globais ainda é desafiador devido ao custo de pós-processamento. Novas técnicas baseadas em *Approximate Factorization Conditions (AFCs)* vêm sendo investigadas para tornar esse procedimento viável em dispositivos NISQ. 

### Implementações Experimentais

A técnica também já foi implementada experimentalmente em processadores quânticos fotônicos de múltiplos qubits. Os resultados mostraram que o protocolo é robusto mesmo em dispositivos ruidosos da era NISQ, indicando forte potencial para aplicações práticas em hardware quântico real. 

## Considerações Finais

Classical Shadows representa uma das técnicas mais promissoras da teoria da informação quântica moderna. Seu principal diferencial é permitir a estimativa eficiente de muitas propriedades físicas utilizando um número relativamente pequeno de medições.

Ao evitar a reconstrução completa da matriz densidade, o protocolo reduz drasticamente custos experimentais e computacionais, tornando-se especialmente relevante para sistemas quânticos de larga escala.

Além disso, a possibilidade de reutilizar o mesmo conjunto de medições para estimar múltiplos observáveis faz do método uma ferramenta extremamente poderosa para algoritmos variacionais, química quântica, caracterização de estados e aplicações futuras em dispositivos NISQ. 
