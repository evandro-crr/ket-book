# Compressão Quântica de Informação

A **compressão quântica de informação** estuda como representar estados quânticos utilizando a menor quantidade possível de recursos, preservando a informação essencial. Esse problema é a extensão natural da compressão de dados clássica para o contexto quântico.

Enquanto na teoria clássica a compressão busca reduzir o número de bits necessários para representar uma fonte de informação, na teoria quântica o objetivo é minimizar o número de **qubits** necessários para representar estados provenientes de uma fonte quântica.

O resultado central dessa área é o **teorema de compressão de Schumacher**, que estabelece o limite fundamental para a compressão de informação quântica.

## O problema da compressão quântica

Considere uma fonte quântica que emite estados $\ket{\psi_i}$ com probabilidades $p_i$. Essa fonte pode ser descrita por uma matriz densidade

$$
\rho = \sum_i p_i \ket{\psi_i}\bra{\psi_i}
$$

O objetivo da compressão quântica é:

- codificar sequências de estados emitidos pela fonte
- utilizando o menor número possível de qubits
- permitindo recuperar os estados originais com alta fidelidade

Diferentemente do caso clássico, não podemos simplesmente "ler" os estados para comprimi-los, pois a **medida quântica destrói informação**. Assim, a compressão deve ser feita diretamente sobre os estados quânticos.

## Teorema de Schumacher

O **teorema de Schumacher** é o análogo quântico do teorema de compressão de Shannon.

Ele afirma que:

> É possível comprimir a saída de uma fonte quântica para aproximadamente $S(\rho)$ qubits por estado, onde $S(\rho)$ é a entropia de von Neumann da fonte.

Mais precisamente:

- para sequências longas de estados (regime assintótico),
- existe um esquema de compressão que utiliza cerca de

$$
n S(\rho)
$$

qubits para representar $n$ estados,
- com erro arbitrariamente pequeno.

Esse resultado mostra que a **entropia de von Neumann mede a quantidade mínima de recursos necessários para armazenar informação quântica**.

## Subespaço típico

A ideia central por trás da compressão quântica é o conceito de **subespaço típico**.

Para uma sequência de muitos estados emitidos pela fonte, a maior parte da probabilidade está concentrada em um subespaço do espaço de Hilbert cujo tamanho é aproximadamente

$$
2^{n S(\rho)}
$$

Isso significa que:

- embora o espaço total tenha dimensão exponencial maior,
- os estados relevantes ocupam apenas uma fração pequena desse espaço.

A compressão consiste em:

1. projetar o estado no subespaço típico  
2. codificar apenas essa parte relevante  
3. descartar o restante  

Como a probabilidade de sair desse subespaço é muito pequena, a informação é preservada com alta fidelidade.

## Interpretação intuitiva

A compressão quântica pode ser entendida como uma forma de remover **redundância quântica**.

Se uma fonte gera estados com estrutura ou correlação, então nem todos os graus de liberdade do sistema são igualmente relevantes. A entropia de von Neumann quantifica exatamente essa redundância.

- baixa entropia → alta redundância → maior compressão  
- alta entropia → pouca redundância → menor compressão  

No caso extremo:

- se $S(\rho)=0$, o estado é puro → não há incerteza → compressão máxima  
- se $S(\rho)=1$ (para um qubit), o estado é maximamente misto → nenhuma compressão possível  

## Exemplo simples

Considere uma fonte que emite:

- $\ket{0}$ com probabilidade $0.9$
- $\ket{1}$ com probabilidade $0.1$

A matriz densidade é

$$
\rho = 0.9 \ket{0}\bra{0} + 0.1 \ket{1}\bra{1}
$$

A entropia de von Neumann é

$$
S(\rho) = - (0.9 \log_2 0.9 + 0.1 \log_2 0.1) \approx 0.47
$$

Isso significa que, em média, cada estado pode ser comprimido para cerca de **0.47 qubits**, no regime assintótico.

Esse resultado é análogo à compressão clássica, mas aqui ocorre **sem medir os estados**.

## Diferenças em relação à compressão clássica

Embora exista uma forte analogia com a teoria clássica, há diferenças fundamentais:

- estados quânticos **não podem ser copiados** (teorema do no-cloning)  
- não é possível medir os estados sem perturbá-los  
- a compressão ocorre em termos de **subespaços**, não apenas sequências de símbolos  

Essas diferenças tornam a compressão quântica conceitualmente mais sutil.

## Importância

A compressão quântica de informação é um resultado central da teoria da informação quântica.

Ela:

- fornece uma interpretação operacional da **entropia de von Neumann**  
- estabelece limites fundamentais para **armazenamento de informação quântica**  
- conecta teoria da informação com **estrutura do espaço de Hilbert**  
- serve de base para resultados mais avançados em **comunicação quântica**  

Assim, o teorema de Schumacher mostra que a entropia quântica não é apenas uma quantidade abstrata, mas representa diretamente o **custo físico de armazenar informação quântica**.