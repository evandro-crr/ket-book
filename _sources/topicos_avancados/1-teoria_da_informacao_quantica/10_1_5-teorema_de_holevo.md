# Teorema de Holevo

O **teorema de Holevo** é um dos resultados mais importantes da teoria da informação quântica. Ele estabelece um limite fundamental para a quantidade de **informação clássica** que pode ser extraída de um sistema quântico.

Embora estados quânticos possam existir em superposição e parecer carregar uma grande quantidade de informação, o teorema de Holevo mostra que há um limite rigoroso para o quanto dessa informação pode ser acessado por meio de medidas.

Esse resultado é central para compreender **as limitações da comunicação quântica** e o papel da mecânica quântica no processamento de informação.

## O problema do Teorema de Holevo

Considere o seguinte cenário:

- um emissor (Alice) deseja enviar informação clássica
- ela codifica mensagens clássicas $i$ em estados quânticos $\rho_i$
- cada estado é enviado com probabilidade $p_i$

O receptor (Bob) recebe o estado quântico, mas para obter informação ele precisa realizar uma **medida quântica**.

A questão fundamental é:

> quanta informação clássica Bob pode extrair sobre a variável $i$ a partir das medições?

## Enunciado do Teorema

Defina o estado médio da fonte como

$$
\rho = \sum_i p_i \rho_i
$$

O teorema de Holevo afirma que a quantidade de informação acessível é limitada por

$$
I(X:Y) \le \chi
$$

onde

$$
\chi = S(\rho) - \sum_i p_i S(\rho_i)
$$

é chamada de **quantidade de Holevo**.

Aqui:

- $S(\rho)$ é a entropia de von Neumann
- $I(X:Y)$ é a informação mútua entre a variável enviada e o resultado da medida

Esse resultado vale para **qualquer estratégia de medição**.

## Interpretação do Teorema de Holevo

O teorema de Holevo mostra que:

- não é possível extrair arbitrariamente muita informação de um sistema quântico  
- a quantidade acessível é limitada por uma diferença de entropias  

Mesmo que os estados $\rho_i$ sejam complexos ou de alta dimensão, a informação clássica recuperável é restrita.

Um caso importante ocorre quando os estados $\rho_i$ são puros:

$$
S(\rho_i) = 0
$$

Nesse caso,

$$
\chi = S(\rho)
$$

Ou seja, a quantidade de informação acessível é limitada pela entropia do estado médio.

## Exemplo simples

Considere uma fonte que envia:

- $\ket{0}$ com probabilidade $1/2$
- $\ket{1}$ com probabilidade $1/2$

O estado médio é

$$
\rho =
\frac{1}{2}\ket{0}\bra{0} +
\frac{1}{2}\ket{1}\bra{1}
$$

A entropia é

$$
S(\rho) = 1
$$

Como os estados são ortogonais, é possível distingui-los perfeitamente, e Bob pode recuperar **1 bit de informação**.

Agora considere:

- $\ket{0}$ com probabilidade $1/2$
- $\ket{+} = \frac{1}{\sqrt{2}}(\ket{0} + \ket{1})$ com probabilidade $1/2$

Nesse caso, os estados **não são ortogonais**, e não podem ser perfeitamente distinguidos.

O teorema de Holevo garante que a informação extraível é **menor que 1 bit**, mesmo que os estados sejam diferentes.

## Consequências importantes

O teorema de Holevo possui diversas implicações fundamentais.

**Limite de 1 bit por qubit**

Um único qubit não pode transportar mais do que **1 bit de informação clássica** de forma confiável, mesmo que esteja em superposição contínua.

**Não violação da teoria clássica**

Embora estados quânticos pareçam conter infinitas informações (por serem descritos por amplitudes contínuas), essa informação não pode ser totalmente acessada.

**Fundamento da comunicação quântica**

O teorema estabelece limites fundamentais para protocolos de comunicação e para a capacidade de canais quânticos.

## Relação com outros conceitos

O teorema de Holevo está profundamente conectado a outros resultados da teoria da informação quântica.

- ele utiliza a **entropia de von Neumann** como medida central  
- está relacionado à **capacidade de canais quânticos**  
- complementa o **teorema de compressão de Schumacher**  
- aparece em estudos de **codificação e transmissão de informação**  

Além disso, ele é essencial para entender por que a computação quântica não permite acessar diretamente toda a informação contida em um estado quântico.

## Importância

O teorema de Holevo é um dos resultados mais profundos da teoria da informação quântica.

Ele mostra que:

- a mecânica quântica permite novas formas de codificação de informação  
- mas impõe limites fundamentais sobre o que pode ser extraído  
- e estabelece uma ponte entre informação clássica e quântica  

Assim, o teorema de Holevo é essencial para compreender **os limites da informação no mundo quântico** e desempenha um papel central em comunicação quântica, criptografia e computação quântica.