# Canais Quânticos

Na prática, sistemas quânticos raramente permanecem perfeitamente isolados. Toda implementação física de computação quântica envolve interação com o ambiente, imperfeições experimentais, ruído eletrônico, perdas de energia e processos de decoerência. Como consequência, a evolução real de um sistema quântico dificilmente pode ser descrita apenas por operadores unitários ideais.

A teoria de **canais quânticos** surge exatamente como o formalismo matemático capaz de descrever a evolução mais geral possível de estados quânticos físicos. Enquanto operadores unitários representam dinâmicas reversíveis e isoladas, canais quânticos incorporam efeitos irreversíveis associados à perda de informação, dissipação de energia e interação com graus de liberdade externos.

Essa estrutura tornou-se central na teoria da informação quântica moderna, pois praticamente toda implementação física real — desde comunicação quântica até hardware NISQ — depende da compreensão de como estados quânticos evoluem sob ruído.

## Estrutura Matemática e Condições Físicas

Um canal quântico é uma aplicação linear

$$
\Phi : \rho \rightarrow \Phi(\rho)
$$

que transforma uma matriz densidade válida em outra matriz densidade válida.

Para que essa transformação represente um processo físico possível, duas propriedades fundamentais devem ser satisfeitas.

A primeira é a **preservação do traço**:

$$
\mathrm{Tr}(\Phi(\rho)) = 1
$$

Essa condição garante conservação da probabilidade total, assegurando que o estado final continua fisicamente normalizado.

A segunda — e mais profunda — é a propriedade de **completa positividade**. Não basta que o canal preserve positividade apenas no sistema isolado; ele também deve permanecer positivo quando estendido a sistemas auxiliares arbitrários:

$$
\Phi \otimes I_n
$$

Isso é essencial porque sistemas quânticos podem estar entrelaçados com outros sistemas externos. Um mapa que fosse apenas positivo poderia produzir estados não físicos ao atuar sobre parte de um sistema entrelaçado.

Transformações que satisfazem simultaneamente preservação do traço e completa positividade são chamadas de **mapas CPTP** (*Completely Positive Trace Preserving*). Esses mapas constituem a estrutura matemática fundamental dos processos físicos quânticos abertos.

## Representação de Kraus e Estrutura Operacional

Uma das representações mais importantes de canais quânticos é a **representação de Kraus**, na qual o canal assume a forma

$$
\Phi(\rho) = \sum_k K_k \rho K_k^\dagger
$$

onde os operadores $K_k$ são chamados de operadores de Kraus.

Para garantir preservação do traço, esses operadores devem satisfazer

$$
\sum_k K_k^\dagger K_k = I
$$

Essa formulação possui interpretação física extremamente rica. Cada operador de Kraus pode ser associado a uma possível “trajetória efetiva” do sistema durante sua interação com o ambiente.

Além disso, a representação de Kraus evidencia que canais quânticos generalizam naturalmente tanto evoluções unitárias quanto medições quânticas. Em particular:

* Um único operador unitário corresponde a evolução isolada;
* Múltiplos operadores introduzem irreversibilidade e perda de informação;
* Medições surgem como casos especiais condicionais de canais.

A decomposição de Kraus não é única: diferentes conjuntos de operadores podem representar o mesmo canal físico. Isso reflete a existência de múltiplas descrições equivalentes para uma mesma interação sistema-ambiente.

## Interpretação Física e Sistemas Abertos

A interpretação mais profunda dos canais quânticos surge ao considerar sistemas abertos.

Considere um sistema quântico inicialmente em estado $\rho$ e um ambiente em estado $\ket{e_0}$. O sistema conjunto evolui de forma unitária:

$$
U(\rho \otimes \ket{e_0}\bra{e_0})U^\dagger
$$

Como normalmente não temos acesso completo ao ambiente, realizamos o traço parcial sobre seus graus de liberdade:

$$
\Phi(\rho) =
\mathrm{Tr}_E
\left(
U(\rho \otimes \ket{e_0}\bra{e_0})U^\dagger
\right)
$$

Esse resultado é extremamente importante: **todo canal quântico pode ser interpretado como uma evolução unitária global seguida do descarte parcial do ambiente**.

Assim, a irreversibilidade observada localmente não contradiz a reversibilidade da mecânica quântica fundamental. A perda de informação surge porque parte dela “escapa” para o ambiente.

Essa interpretação conecta canais quânticos diretamente aos fenômenos de decoerência e termodinâmica quântica.

## Ruído, Decoerência e Perda de Informação

Os canais quânticos fornecem uma linguagem natural para modelar ruído.

O exemplo mais simples é o canal unitário:

$$
\Phi(\rho) = U\rho U^\dagger
$$

que representa evolução ideal sem perda de informação.

Entretanto, sistemas físicos reais sofrem processos muito mais complexos.

O **canal despolarizante** modela situações em que o estado perde progressivamente sua estrutura quântica e converge para um estado maximamente misto:

$$
\Phi(\rho) =
(1-p)\rho + p\frac{I}{2}
$$

Esse processo destrói informação quântica de maneira isotrópica, reduzindo coerências e pureza do estado.

Outro exemplo fundamental é o **canal de damping de amplitude**, utilizado para modelar relaxação energética:

$$
K_0 =
\begin{pmatrix}
1 & 0 \\
0 & \sqrt{1-\gamma}
\end{pmatrix},
\qquad
K_1 =
\begin{pmatrix}
0 & \sqrt{\gamma} \\
0 & 0
\end{pmatrix}
$$

Esse canal descreve fenômenos físicos como emissão espontânea e decaimento de estados excitados.

Enquanto o canal despolarizante remove informação sem direção preferencial, o damping de amplitude introduz dissipação energética real, aproximando o sistema de estados de menor energia.

Esses exemplos mostram que diferentes tipos de ruído possuem estruturas matemáticas e consequências físicas distintas.

## Relação com Medição Quântica

Medições quânticas podem ser interpretadas como canais condicionais.

Quando um resultado específico é selecionado, a evolução corresponde a uma transformação não unitária associada a determinado operador de Kraus. Quando o resultado da medição é ignorado, o processo total assume exatamente a forma de um canal CPTP.

Assim, medições e ruído podem ser tratados dentro de um mesmo formalismo matemático unificado.

Isso revela uma ideia profunda da teoria quântica: tanto a decoerência ambiental quanto a medição correspondem, essencialmente, a processos de perda parcial de informação sobre o sistema.

## Entropia, Informação e Irreversibilidade

Os canais quânticos estão intimamente ligados à teoria da informação.

Em geral, canais ruidosos aumentam a entropia do sistema e reduzem coerências quânticas. Esse comportamento formaliza matematicamente a degradação da informação quântica.

Além disso, canais quânticos definem limites fundamentais para transmissão de informação. Questões como:

* quanta informação clássica pode ser transmitida;
* quanta informação quântica pode sobreviver ao ruído;
* qual a capacidade máxima de um canal;

são todas formuladas em termos de propriedades entrópicas dos canais.

Nesse contexto surgem resultados fundamentais como:

* capacidade clássica de canais quânticos;
* capacidade quântica;
* teorema de Holevo;
* coerência quântica e informação mútua.

## Papel em Computação Quântica

Na computação quântica moderna, canais quânticos desempenham papel central.

Hardware quântico real opera inevitavelmente em presença de ruído. Assim, praticamente toda análise de dispositivos NISQ envolve modelagem via canais quânticos.

Eles são utilizados para:

* caracterização experimental de qubits;
* modelagem de decoerência;
* simulação de ruído;
* desenvolvimento de códigos de correção de erros;
* mitigação de erros;
* benchmark de portas quânticas.

Além disso, técnicas como tomografia de processos quânticos têm justamente o objetivo de reconstruir experimentalmente o canal associado a determinado dispositivo físico.

## Considerações Finais

Os canais quânticos constituem a linguagem matemática fundamental da dinâmica quântica realista. Eles generalizam a evolução unitária ideal ao incorporar interação com o ambiente, perda de informação, medições e decoerência.

Mais do que simples ferramentas matemáticas, canais quânticos formalizam a maneira como informação quântica evolui em sistemas físicos abertos. Eles revelam que irreversibilidade, ruído e dissipação não são exceções da teoria quântica, mas consequências naturais da interação entre sistemas e ambiente.

Por esse motivo, a teoria de canais quânticos tornou-se uma das áreas centrais da computação e da informação quântica contemporânea, sendo indispensável para compreender os limites físicos e informacionais das tecnologias quânticas reais.
