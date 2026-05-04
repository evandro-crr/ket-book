# Tomografia Quântica

A **tomografia quântica** é o procedimento pelo qual se reconstrói completamente o estado de um sistema quântico a partir de dados experimentais. Diferentemente da medição projetiva isolada, que fornece apenas um resultado associado a uma base específica, a tomografia envolve a realização de um conjunto estruturado de medições sobre múltiplas cópias idênticas do sistema, permitindo inferir a descrição completa do estado — tipicamente na forma de uma matriz densidade.

Esse processo é fundamental em computação quântica e em experimentos de informação quântica, pois estados quânticos não são diretamente observáveis. Em vez disso, apenas distribuições de resultados podem ser acessadas, e a tomografia fornece o mecanismo inverso: reconstruir o estado a partir dessas estatísticas.

## Estrutura Matemática e Reconstrução do Estado

Formalmente, o objetivo da tomografia quântica é determinar um operador densidade $\rho$ que descreva completamente o sistema. Para isso, realiza-se um conjunto de medições associadas a operadores ${M_i}$, cujas probabilidades são dadas por:

$$
p(i) = \mathrm{Tr}(M_i \rho)
$$

A ideia central é escolher um conjunto de medições **informacionalmente completo**, ou seja, suficiente para determinar unicamente $\rho$. Em um sistema de dimensão $d$, a matriz densidade possui $d^2 - 1$ parâmetros independentes (considerando hermiticidade, traço unitário e positividade), de modo que é necessário obter informação suficiente para fixar todos esses graus de liberdade.

Na prática, isso é feito expandindo $\rho$ em uma base de operadores. Para um qubit, por exemplo, utiliza-se frequentemente a decomposição em termos das matrizes de Pauli:

$$
\rho = \frac{1}{2}\left(I + \vec{r} \cdot \vec{\sigma}\right)
$$

onde $\vec{r}$ é o vetor de Bloch. Nesse caso, a tomografia reduz-se à estimação das componentes de $\vec{r}$ por meio de medições em diferentes bases.

O problema da tomografia pode então ser formulado como um problema inverso: dado um conjunto de probabilidades experimentais ${p(i)}$, encontrar o operador $\rho$ que melhor explica os dados.

## Métodos de Estimação e Consistência Física

Na prática, os dados experimentais estão sujeitos a ruído estatístico e imperfeições, o que torna a reconstrução direta potencialmente inconsistente (por exemplo, produzindo operadores que não são positivos). Por isso, métodos de estimação mais sofisticados são utilizados.

Um dos mais comuns é a **máxima verossimilhança**, no qual se busca o estado $\rho$ que maximiza a probabilidade de gerar os dados observados, sujeito às restrições físicas (positividade e traço unitário). Esse método garante que o estado reconstruído seja fisicamente válido.

Alternativamente, abordagens bayesianas permitem incorporar conhecimento prévio e produzir distribuições de probabilidade sobre estados possíveis, em vez de uma única estimativa pontual.

Esses métodos evidenciam que a tomografia não é apenas uma reconstrução algébrica, mas um problema estatístico profundo, no qual a inferência desempenha papel central.

## Escalabilidade e Estrutura da Informação

Um dos principais desafios da tomografia quântica é sua **complexidade exponencial**. O número de parâmetros cresce como $d^2$, o que, para sistemas compostos de $n$ qubits ($d = 2^n$), implica um crescimento exponencial no número de medições necessárias.

Isso torna a tomografia completa inviável para sistemas de grande escala. Como consequência, diversas abordagens alternativas foram desenvolvidas, explorando estrutura adicional do estado:

* Estados de baixa entropia ou baixa rank
* Técnicas de compressão (compressed sensing)
* Tomografia adaptativa
* Métodos baseados em sombras clássicas (classical shadows)

Essas técnicas reduzem drasticamente o número de medições necessárias ao explorar propriedades típicas dos estados relevantes em aplicações práticas.

## Relação com Medição e Observáveis

A tomografia quântica depende essencialmente da escolha das medições realizadas. Como cada medição acessa apenas uma projeção parcial do estado, é necessário combinar resultados de diferentes bases para obter uma reconstrução completa.

Esse fato reflete uma característica fundamental da mecânica quântica: não existe uma única medição que revele todas as propriedades de um sistema. Em vez disso, diferentes observáveis — frequentemente não comutantes — devem ser acessados separadamente.

Assim, a tomografia pode ser interpretada como uma forma sistemática de contornar essa limitação, agregando informações provenientes de múltiplas perspectivas experimentais.

## Dinâmica, Canais e Tomografia de Processos

O conceito de tomografia pode ser estendido além de estados, incluindo a caracterização de **canais quânticos** e operações. Nesse contexto, fala-se em **tomografia de processo quântico**, cujo objetivo é reconstruir completamente uma transformação $\mathcal{E}$.

Isso é feito aplicando o canal a um conjunto de estados de entrada conhecidos e realizando tomografia nos estados de saída. O resultado é uma descrição completa da dinâmica do sistema, frequentemente expressa em termos de operadores de Kraus ou de uma matriz de Choi.

Essa generalização é essencial para validação de portas lógicas em computação quântica e para caracterização de ruído em dispositivos reais.

## Papel em Computação Quântica e Experimentos

Na prática, a tomografia quântica é uma ferramenta indispensável para:

* Verificar a preparação correta de estados quânticos
* Caracterizar erros experimentais
* Validar portas e circuitos quânticos
* Testar protocolos de informação quântica

Ela atua como um instrumento de diagnóstico, permitindo comparar o estado ideal com o estado efetivamente produzido em laboratório.

No entanto, devido ao seu custo, seu uso em larga escala é limitado, sendo frequentemente substituído por técnicas mais eficientes em sistemas maiores.

## Considerações Finais

A tomografia quântica fornece o elo entre teoria e experimento ao permitir reconstruir estados quânticos a partir de dados observáveis. Trata-se de um problema de inferência estatística profundamente enraizado na estrutura da mecânica quântica, refletindo tanto suas limitações quanto sua riqueza.

Embora conceitualmente direta, sua implementação prática enfrenta desafios significativos de escalabilidade, motivando o desenvolvimento de métodos mais eficientes e adaptativos.

Ainda assim, como ferramenta de caracterização e validação, a tomografia permanece essencial, especialmente em regimes onde o controle e a compreensão detalhada do sistema são necessários.
