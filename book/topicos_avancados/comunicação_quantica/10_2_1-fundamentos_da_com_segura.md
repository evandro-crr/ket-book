# Fundamentos da Comunicação Segura

A comunicação segura trata do problema de transmitir informação entre duas partes de forma que terceiros não autorizados não consigam acessar ou modificar o conteúdo da mensagem. Esse é um tema central em áreas como computação, redes e teoria da informação.

De modo geral, a segurança de um sistema de comunicação envolve três aspectos principais: **confidencialidade**, **integridade** e **autenticidade**. A confidencialidade garante que apenas os destinatários tenham acesso à mensagem, a integridade assegura que ela não foi alterada, e a autenticidade permite verificar quem está se comunicando.

Na prática, esses objetivos são tradicionalmente alcançados por meio da criptografia clássica. No entanto, essa abordagem possui limitações importantes, especialmente quando analisada do ponto de vista da teoria da informação e da mecânica quântica.

## Segurança na comunicação clássica

Na comunicação clássica, a segurança geralmente depende de algoritmos criptográficos que utilizam chaves. A ideia é tornar a mensagem incompreensível para qualquer pessoa que não possua a chave correta.

Esses métodos são baseados em problemas matemáticos considerados difíceis de resolver. Assim, a segurança depende do fato de que um possível adversário não possui recursos suficientes para quebrar o sistema em tempo viável.

Esse tipo de segurança é chamado de **segurança computacional**, pois depende diretamente do poder computacional disponível.

Apesar de funcionar bem na prática, essa abordagem não é absoluta. Com o avanço da tecnologia — seja por novos algoritmos ou novos modelos de computação — esses sistemas podem se tornar vulneráveis.

![falqon](../../images/topicos/comunicacao/Alice.jpg)

## Segurança baseada em teoria da informação

Uma alternativa é analisar a segurança a partir da teoria da informação. Nesse caso, o objetivo não é apenas dificultar o acesso à mensagem, mas garantir que um interceptador **não consiga extrair informação relevante**, independentemente de seu poder computacional.

Esse tipo de abordagem é conhecido como **segurança incondicional**.

Um exemplo clássico é o **one-time pad**, em que a mensagem é combinada com uma chave aleatória do mesmo tamanho. Quando usado corretamente, esse método garante que a mensagem interceptada não revela nenhuma informação sobre o conteúdo original.

Apesar disso, ele apresenta dificuldades práticas, principalmente na distribuição segura das chaves.

::: {admonition} Exemplo
:class: tip

Considere uma mensagem binária:

$$
m = 1011
$$

e uma chave aleatória do mesmo tamanho:

$$
k = 1100
$$

A mensagem criptografada é obtida aplicando a operação XOR bit a bit:

$$
c = m \oplus k
$$

Calculando:

$$
c = 1011 \oplus 1100 = 0111
$$

Para recuperar a mensagem original, o receptor aplica novamente XOR com a mesma chave:

$$
m = c \oplus k = 0111 \oplus 1100 = 1011
$$

Observe que, sem conhecer a chave, o valor de $c$ pode corresponder a **qualquer mensagem possível** com a mesma probabilidade. Isso significa que o interceptador não obtém nenhuma informação sobre $m$ a partir de $c$.

Esse exemplo ilustra por que o one-time pad fornece segurança perfeita sob condições ideais, embora sua aplicação prática seja limitada pela necessidade de compartilhar chaves aleatórias do mesmo tamanho da mensagem.

:::

## Limitações da abordagem clássica

Mesmo com técnicas avançadas, a comunicação clássica possui algumas limitações importantes.

Uma delas é que a informação pode ser copiada perfeitamente. Isso significa que um interceptador pode capturar e duplicar a mensagem sem necessariamente ser detectado.

Além disso, a distribuição de chaves seguras continua sendo um problema central. Em muitos casos, é necessário assumir a existência de um canal previamente seguro, o que nem sempre é viável.

Esses pontos mostram que a segurança, no modelo clássico, não está diretamente ligada às leis físicas do sistema.

## Segurança em sistemas quânticos

A comunicação quântica propõe uma abordagem diferente, na qual a segurança está associada às próprias propriedades físicas da informação.

Sistemas quânticos possuem características que não aparecem no mundo clássico, como:

* a impossibilidade de copiar estados quânticos arbitrários (*No-cloning theorem*)
* a perturbação causada por medições
* limites fundamentais na extração de informação

Essas propriedades implicam que qualquer tentativa de interceptação tende a deixar rastros, pois altera o estado do sistema.

Com isso, a segurança deixa de depender apenas de hipóteses matemáticas e passa a ser analisada com base na física do sistema.

## Motivação para comunicação quântica

Diante dessas diferenças, a comunicação quântica surge como uma forma de expandir os modelos tradicionais de comunicação.

Ela permite estudar:

* como transmitir informação usando estados quânticos
* quais são os limites dessa transmissão
* como explorar propriedades físicas para garantir segurança

Nos próximos tópicos, esses conceitos serão utilizados para analisar protocolos específicos e entender como a informação pode ser transmitida e protegida em sistemas quânticos.