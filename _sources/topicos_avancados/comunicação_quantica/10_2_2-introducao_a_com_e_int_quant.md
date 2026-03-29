# Introdução à Comunicação e Internet Quântica

A comunicação quântica estuda como transmitir informação utilizando sistemas quânticos, explorando propriedades como superposição e emaranhamento. Diferente da comunicação clássica, onde a informação é codificada em bits, aqui utilizamos os **qubits** já estudados, que permitem representar estados de forma mais geral.

Com base nos conceitos de teoria da informação quântica, como canais quânticos e limites de informação, é possível desenvolver protocolos que utilizam esses recursos para transmitir informação e estabelecer correlações entre sistemas distantes.

Esse modelo não substitui a comunicação clássica, mas a **estende**, introduzindo novas possibilidades e também novas limitações.

## O que é Comunicação Quântica

A comunicação quântica envolve o envio de estados quânticos através de um canal físico, seguido de medições que permitem extrair informação clássica.

De forma geral, o processo pode ser descrito em três etapas:

* preparação de um estado quântico
* transmissão por um canal quântico
* medição no receptor

Do ponto de vista formal, esse processo pode ser descrito como a evolução de um estado quântico $\rho$ através de um canal quântico $\mathcal{E}$:

$$
\rho \rightarrow \mathcal{E}(\rho)
$$

seguido de uma medição que produz resultados clássicos. Essa descrição conecta diretamente a comunicação quântica com a teoria de canais quânticos estudada anteriormente.

Além disso, canais clássicos auxiliares frequentemente são necessários para complementar a comunicação, como ocorre em protocolos de teletransporte quântico.

Um aspecto central é que a informação quântica não pode ser tratada como informação clássica. Em particular:

* estados quânticos não podem ser copiados arbitrariamente (*No-cloning theorem*)
* a medição pode alterar o estado
* há limites fundamentais para a quantidade de informação que pode ser extraída

Essas características influenciam diretamente como a comunicação é realizada.

## O que é uma Internet Quântica

A internet quântica é uma rede que permite a distribuição de estados quânticos entre diferentes nós, de forma análoga às redes clássicas, mas com objetivos e funcionamento distintos.

Enquanto a internet clássica transmite dados (bits), a internet quântica busca transmitir **estados quânticos** ou estabelecer **emaranhamento** entre sistemas distribuídos.

Na prática, muitas tarefas não envolvem o envio direto de estados quânticos, mas sim a **distribuição de emaranhamento** entre nós. Esse recurso pode então ser utilizado para realizar protocolos como teletransporte quântico e distribuição de chaves criptográficas.

Essa rede é composta por:

* **nós quânticos**, capazes de armazenar e processar qubits
* **canais quânticos**, responsáveis pela transmissão de estados
* **canais clássicos**, usados para coordenação e controle

Em vez de simplesmente enviar mensagens, uma rede quântica permite tarefas como:

* distribuição de chaves criptográficas seguras
* execução de protocolos de comunicação quântica
* compartilhamento de recursos quânticos entre diferentes locais

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

Essas diferenças implicam que redes quânticas não podem utilizar estratégias clássicas como amplificação e retransmissão de sinais, exigindo o desenvolvimento de técnicas específicas para preservar e distribuir informação.

Além disso, em muitos casos, a comunicação quântica não consiste no envio direto de informação, mas sim na criação de correlações entre sistemas distribuídos.

## Motivação e objetivos

O estudo da comunicação e da internet quântica busca compreender como essas propriedades podem ser utilizadas em sistemas reais.

Entre os principais objetivos estão:

* desenvolver protocolos de comunicação seguros
* entender os limites de transmissão de informação
* construir redes capazes de distribuir estados quânticos de forma confiável

Nos próximos tópicos, esses conceitos serão formalizados por meio da arquitetura de redes quânticas e utilizados na análise de protocolos de comunicação.
