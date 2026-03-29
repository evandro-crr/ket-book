# Introdução à Comunicação e Internet Quântica

A comunicação quântica estuda como transmitir informação utilizando sistemas quânticos, explorando propriedades como superposição e emaranhamento. Diferente da comunicação clássica, onde a informação é codificada em bits, aqui utilizamos os **qubits** já estudados, que permitem representar estados de forma mais geral.

Enquanto na comunicação clássica a informação pode ser copiada, amplificada e transmitida sem restrições fundamentais, na comunicação quântica essas operações são limitadas pelas próprias leis da física. Como consequência, surgem tanto novas possibilidades quanto novos desafios.

Com base nos conceitos de teoria da informação quântica, como canais quânticos, entropia e limites de informação, é possível desenvolver protocolos que utilizam esses recursos para transmitir informação e estabelecer correlações entre sistemas distantes.

Esse modelo não substitui a comunicação clássica, mas a **estende**, introduzindo novas formas de representar, transmitir e interpretar informação.

## O que é Comunicação Quântica

A comunicação quântica envolve o envio de estados quânticos através de um canal físico, seguido de medições que permitem extrair informação clássica.

De forma geral, o processo pode ser descrito em três etapas:

* preparação de um estado quântico
* transmissão por um canal quântico
* medição no receptor

Do ponto de vista formal, esse processo pode ser descrito como a evolução de um estado quântico ( \rho ) através de um canal quântico ( \mathcal{E} ):

$$
\rho \rightarrow \mathcal{E}(\rho)
$$

seguido de uma medição que produz resultados clássicos. Essa descrição conecta diretamente a comunicação quântica com a teoria de canais quânticos estudada anteriormente.

Mais especificamente, o canal ( \mathcal{E} ) modela todos os efeitos físicos envolvidos na transmissão, incluindo ruído, perdas e interação com o ambiente. Dessa forma, a comunicação quântica pode ser analisada como um problema de transformação e degradação de estados.

Além disso, canais clássicos auxiliares frequentemente são necessários para complementar a comunicação, como ocorre em protocolos de teletransporte quântico, nos quais a transmissão do estado depende da troca de bits clássicos.

Um aspecto central é que a informação quântica não pode ser tratada como informação clássica. Em particular:

* estados quânticos não podem ser copiados arbitrariamente (*No-cloning theorem*)
* a medição pode alterar o estado
* há limites fundamentais para a quantidade de informação que pode ser extraída

Essas características implicam que a informação quântica não pode ser acessada diretamente, mas apenas por meio de medições, o que introduz uma distinção fundamental entre **informação armazenada** e **informação acessível**.

## O que é uma Internet Quântica

A internet quântica é uma rede que permite a distribuição de estados quânticos entre diferentes nós, de forma análoga às redes clássicas, mas com objetivos e funcionamento distintos.

Enquanto a internet clássica transmite dados (bits), a internet quântica busca transmitir **estados quânticos** ou estabelecer **emaranhamento** entre sistemas distribuídos.

Na prática, muitas tarefas não envolvem o envio direto de estados quânticos, mas sim a **distribuição de emaranhamento** entre nós. Esse recurso pode então ser utilizado para realizar protocolos como teletransporte quântico e distribuição de chaves criptográficas.

Essa mudança de paradigma é importante: em vez de transmitir informação diretamente, a rede passa a distribuir **recursos quânticos**, que podem ser utilizados posteriormente para realizar tarefas de comunicação.

Essa rede é composta por:

* **nós quânticos**, capazes de armazenar e processar qubits
* **canais quânticos**, responsáveis pela transmissão de estados
* **canais clássicos**, usados para coordenação e controle

A presença simultânea de canais quânticos e clássicos evidencia que redes quânticas são, na prática, sistemas híbridos.

## Diferenças em relação à internet clássica

Embora compartilhem algumas semelhanças estruturais, redes quânticas apresentam diferenças importantes em relação às redes clássicas.

Na comunicação clássica:

* a informação pode ser copiada e retransmitida livremente
* sinais podem ser amplificados sem alterar seu conteúdo
* a segurança depende de algoritmos

Já na comunicação quântica:

* estados não podem ser copiados arbitrariamente
* a transmissão é sensível a ruído e perdas
* a segurança pode ser analisada com base em princípios físicos

Essas diferenças implicam que redes quânticas não podem utilizar estratégias clássicas como amplificação e retransmissão de sinais. Em particular, a impossibilidade de clonagem impede a criação de “repetidores clássicos”, exigindo o desenvolvimento de técnicas específicas para preservar e distribuir informação.

Além disso, em muitos casos, a comunicação quântica não consiste no envio direto de informação, mas sim na criação de correlações entre sistemas distribuídos. Isso altera a forma como a informação é utilizada e interpretada em redes.

## Motivação e objetivos

O estudo da comunicação e da internet quântica busca compreender como essas propriedades podem ser utilizadas em sistemas reais.

Entre os principais objetivos estão:

* desenvolver protocolos de comunicação seguros
* entender os limites fundamentais de transmissão de informação
* construir redes capazes de distribuir estados quânticos de forma confiável

Além disso, a comunicação quântica permite investigar questões mais profundas da teoria da informação, como os limites entre informação clássica e quântica e o papel das correlações na transmissão de informação.

Nos próximos tópicos, esses conceitos serão formalizados por meio da arquitetura de redes quânticas e utilizados na análise de protocolos de comunicação.