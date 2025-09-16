# Álgebra Linear para Computação Quântica

```{note}
Material extraído do TCC [*Computação Quântica: Uma abordagem para estudantes de graduação em Ciências Exatas*](./tcc-giovani.pdf), de Giovani Goraiebe Pollachini.
```

NESTE capítulo, um resumo de Álgebra Linear voltado para Computação Quântica é apresentado. A teoria é apresentada usando-se a *notação de Dirac*, ou, *notação de braket*, uma notação utilizada largamente em Mecânica Quântica e que será necessária para o restante do trabalho. Essa notação é conveniente para se fazer contas e faz com que as diversas operações possíveis se encaixem naturalmente.

Na Álgebra Linear abstrata, pode-se considerar espaços vetoriais sobre diversos corpos (ou escalares), que são estruturas algébricas com propriedades semelhantes aos números reais e complexos. Os espaços vetoriais podem ter dimensão finita ou infinita.

Na Computação Quântica o interesse é voltado a espaços vetoriais de **dimensão finita** sobre o corpo dos números complexos. Isso permite a identificação do espaço com as $n$-uplas de números complexos, o que simplifica grandemente a teoria. Os resultados resumidos neste capítulo estão situados nesse contexto.

A principal referência para esse capítulo é {cite}`nielsen_quantum_2010`. Outra referência muito útil é {cite}`lima_algebra_2021`, que possui um capítulo voltado a espaços vetoriais complexos. Livros texto clássicos de Álgebra Linear, como {cite}`steinbruch_algebra_2009` também são úteis. Embora tenham ênfase em espaços vetoriais reais, a maioria das definições, resultados e demonstrações se transporta integralmente para os espaços vetoriais complexos.

Será considerado um pré-requisito a este texto um curso de Álgebra Linear ao nível de graduação abordando-se os seguintes itens: espaços vetoriais, base e dimensão, transformações lineares, autovalores e autovetores. Por ter um caráter de resumo, os resultados apresentados, via de regra, não são acompanhados de suas demonstrações, as quais podem ser encontradas nos livros mencionados no parágrafo anterior.

