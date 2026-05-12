# Teorema de Holevo

O **teorema de Holevo** é um dos resultados mais profundos e fundamentais da teoria da informação quântica. Ele estabelece um limite rigoroso para a quantidade de **informação clássica** que pode ser extraída de sistemas quânticos, mostrando que, apesar da enorme riqueza estrutural dos estados quânticos, existe uma restrição física sobre o quanto dessa informação pode ser acessado por meio de medições.

Esse resultado possui enorme importância conceitual porque revela uma tensão central da mecânica quântica: estados quânticos parecem conter muito mais informação do que sistemas clássicos equivalentes — devido à superposição, amplitudes complexas e espaços de Hilbert de alta dimensão — mas a teoria impõe limites severos sobre a informação efetivamente observável.

O teorema de Holevo tornou-se um dos pilares da comunicação quântica moderna, sendo essencial para compreender capacidades de canais quânticos, limites de transmissão de informação e a relação entre informação clássica e quântica.

## Estrutura do Problema Informacional

Considere um cenário de comunicação entre dois agentes, Alice e Bob.

Alice deseja transmitir uma variável clássica $i$ escolhida segundo probabilidades $p_i$. Para isso, ela associa cada mensagem clássica a um estado quântico $\rho_i$ e envia esse estado para Bob.

A fonte é então descrita pelo ensemble:

$$
{p_i,\rho_i}
$$

O estado médio recebido por Bob é

$$
\rho = \sum_i p_i \rho_i
$$

No entanto, Bob não possui acesso direto à variável clássica original. Tudo o que ele recebe é um sistema quântico sobre o qual precisa realizar medições para tentar inferir qual estado foi enviado.

A pergunta fundamental torna-se:

> Qual é a quantidade máxima de informação clássica que Bob pode recuperar a partir das medições?

Essa questão é extremamente profunda porque medições quânticas possuem natureza probabilística e inevitavelmente perturbam os estados. Além disso, estados quânticos não ortogonais não podem ser perfeitamente distinguidos.

O teorema de Holevo fornece exatamente o limite fundamental dessa extração de informação.

## Enunciado do Teorema

A quantidade de informação clássica acessível por qualquer procedimento de medição satisfaz

$$
I(X:Y) \le \chi
$$

onde

$$
\chi =
S(\rho) - \sum_i p_i S(\rho_i)
$$

A quantidade

$$
\chi
$$

é chamada de **quantidade de Holevo**.

Aqui:

* $S(\rho)$ representa a entropia de von Neumann;
* $I(X:Y)$ é a informação mútua entre a variável enviada e o resultado obtido na medição.

Esse limite vale para qualquer estratégia física possível de medição, incluindo medições coletivas sofisticadas sobre múltiplos sistemas.

O resultado estabelece que a quantidade de informação clássica recuperável depende da diferença entre a incerteza global do ensemble e a incerteza média interna dos estados enviados.

## Interpretação Informacional

A interpretação física do teorema é extremamente rica.

O termo

$$
S(\rho)
$$

mede a incerteza total associada ao estado médio recebido. Já o termo

$$
\sum_i p_i S(\rho_i)
$$

representa a incerteza média interna dos estados individuais.

A diferença entre essas quantidades mede efetivamente quanta informação clássica está codificada nas diferenças entre os estados enviados.

Quando os estados $\rho_i$ são puros:

$$
S(\rho_i)=0
$$

e a quantidade de Holevo reduz-se a

$$
\chi = S(\rho)
$$

Nesse caso, toda a limitação informacional é determinada pela estrutura estatística do ensemble médio.

Esse resultado mostra algo profundo: embora estados quânticos possam ser descritos por amplitudes contínuas e aparentemente carregar informação arbitrariamente grande, apenas uma quantidade limitada dessa informação pode ser acessada operacionalmente.

A informação “escondida” nas amplitudes quânticas não pode ser completamente extraída por medições.

## Ortogonalidade e Distinguibilidade

A capacidade de extrair informação depende diretamente da distinguibilidade dos estados enviados.

Considere primeiro o caso em que Alice envia:

$$
\ket{0}
\quad \text{ou} \quad
\ket{1}
$$

com probabilidade igual.

Como esses estados são ortogonais, Bob pode distingui-los perfeitamente através de uma medição apropriada. O estado médio possui entropia

$$
S(\rho)=1
$$

e Bob consegue recuperar exatamente 1 bit de informação clássica.

Agora considere o ensemble:

$$
\ket{0}
\quad \text{e} \quad
\ket{+} =
\frac{1}{\sqrt{2}}(\ket{0}+\ket{1})
$$

Esses estados não são ortogonais. Consequentemente, nenhuma medição consegue distingui-los perfeitamente.

Mesmo que os estados sejam diferentes, a mecânica quântica impõe ambiguidade inevitável. O teorema de Holevo garante então que a informação acessível é estritamente menor que 1 bit.

Essa limitação não é tecnológica, mas fundamentalmente física.

## Limite Informacional dos Qubits

Uma das consequências mais importantes do teorema é o famoso resultado de que:

> Um único qubit não pode transmitir mais do que 1 bit clássico de informação acessível.

Isso é surpreendente porque um qubit puro arbitrário depende de parâmetros contínuos:

$$
\ket{\psi} =
\alpha\ket{0}+\beta\ket{1}
$$

aparentemente contendo infinitas informações reais.

Entretanto, o teorema de Holevo mostra que essas amplitudes não podem ser livremente convertidas em informação clássica observável.

Esse resultado impede paradoxos informacionais e preserva consistência entre teoria quântica e teoria clássica da informação.

## Relação com Medição Quântica

O limite de Holevo emerge diretamente da natureza das medições quânticas.

Medições não revelam o estado completo do sistema, mas apenas projeções probabilísticas associadas a determinados observáveis. Além disso:

* medições perturbam os estados;
* estados não ortogonais não podem ser perfeitamente distinguidos;
* não existe procedimento universal de leitura completa de um estado desconhecido.

Essas restrições tornam impossível acessar toda a informação aparentemente codificada nas amplitudes quânticas.

Assim, o teorema de Holevo formaliza matematicamente os limites observacionais impostos pela mecânica quântica.

## Relação com Entropia e Canais Quânticos

O teorema de Holevo está profundamente conectado à entropia de von Neumann e à teoria de canais quânticos.

A quantidade de Holevo atua como um limite superior para a capacidade clássica de canais quânticos. Em particular, ela aparece em resultados fundamentais envolvendo:

* capacidade clássica de transmissão;
* codificação quântica;
* comunicação assistida por entrelaçamento;
* teoria de compressão quântica.

Além disso, o teorema complementa diretamente o teorema de Schumacher:

* Schumacher determina quanto custa armazenar informação quântica;
* Holevo determina quanta informação clássica pode ser extraída de sistemas quânticos.

Juntos, esses resultados estruturam grande parte da teoria moderna da informação quântica.

## Consequências Conceituais

O teorema de Holevo possui implicações conceituais profundas.

Ele mostra que sistemas quânticos não funcionam como “supermemórias clássicas” capazes de liberar informação arbitrária.

Embora estados quânticos permitam codificações extremamente sofisticadas, a quantidade de informação clássica acessível continua limitada pelas leis da teoria quântica.

Esse resultado ajuda a explicar por que:

* a computação quântica não fornece acesso direto exponencial à informação;
* algoritmos quânticos dependem de interferência e estrutura global, e não simples leitura de amplitudes;
* protocolos quânticos mantêm compatibilidade com causalidade e limites físicos de comunicação.

## Considerações Finais

O teorema de Holevo estabelece um dos limites mais fundamentais da informação no universo quântico. Ele demonstra que, apesar da enorme riqueza matemática dos estados quânticos, apenas uma quantidade limitada de informação clássica pode ser extraída operacionalmente.

Mais profundamente, o resultado revela que a informação quântica possui natureza distinta da informação clássica: ela não corresponde simplesmente a dados ocultos esperando para serem lidos, mas a estruturas físicas cujo acesso é condicionado pelas próprias leis da mecânica quântica.

Por esse motivo, o teorema de Holevo tornou-se uma peça central da teoria da informação quântica, influenciando profundamente comunicação quântica, criptografia, computação quântica e os fundamentos da própria noção física de informação.
