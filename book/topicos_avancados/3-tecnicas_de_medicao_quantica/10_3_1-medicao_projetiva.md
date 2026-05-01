# Medição Projetiva

A **medição projetiva** constitui uma das estruturas fundamentais da mecânica quântica e representa o formalismo padrão para a extração de informação de sistemas quânticos. Em computação quântica, ela modela o processo pelo qual estados quânticos — potencialmente em superposição e entrelaçamento — produzem resultados clássicos observáveis.

Diferentemente da evolução unitária, a medição projetiva introduz uma dinâmica intrinsecamente probabilística e não reversível, sendo responsável pela transição entre o domínio quântico e o clássico.

## Estrutura Matemática

Uma medição projetiva é descrita por um conjunto de operadores ${P_i}$ definidos sobre um espaço de Hilbert $\mathcal{H}$, satisfazendo:

* **Hermiticidade:**
  $
  P_i = P_i^\dagger
  $

* **Idempotência:**
  $
  P_i^2 = P_i
  $

* **Ortogonalidade:**
  $
  P_i P_j = 0 \quad (i \neq j)
  $

* **Completude:**
  $
  \sum_i P_i = I
  $

Essas condições implicam que:

* Cada $P_i$ é um **projetor ortogonal** sobre um subespaço de $\mathcal{H}$
* O conjunto ${P_i}$ define uma **decomposição direta** do espaço:
  $
  \mathcal{H} = \bigoplus_i \mathcal{H}_i
  $

Ou seja, a medição corresponde a uma **partição do espaço de estados em subespaços mutuamente ortogonais**, cada um associado a um resultado possível.

## Interpretação Operacional

Fisicamente, cada projetor $P_i$ representa um possível resultado da medição. O sistema não “escolhe” um vetor específico, mas sim um **subespaço**.

Isso é crucial em casos degenerados:

* Se o autovalor é degenerado, o estado colapsa para um subespaço de dimensão maior que 1
* A informação dentro desse subespaço pode permanecer parcialmente preservada

## Regra de Born Generalizada

A probabilidade de observar o resultado $i$ é dada por:

### Estado puro

$$
p(i) = \bra{\psi} P_i \ket{\psi}
$$

### Estado misto

$$
p(i) = \mathrm{Tr}(P_i \rho)
$$

Essa formulação tem implicações importantes:

* A probabilidade depende apenas da **projeção do estado no subespaço**
* Fases globais não têm efeito
* Coerências entre subespaços diferentes não contribuem diretamente para probabilidades

## Estrutura Estatística da Medição

A medição projetiva define uma variável aleatória clássica $X$ com distribuição:

$$
\mathbb{P}(X = i) = \mathrm{Tr}(P_i \rho)
$$

Além disso, é possível definir o valor esperado de um observável associado:

$$
\mathbb{E}[A] = \sum_i a_i , \mathrm{Tr}(P_i \rho)
$$

Esse resultado conecta diretamente o formalismo da medição com a estatística clássica.

## Dinâmica da Medição

A medição projetiva induz uma transformação condicional no estado.

### Estado puro

$$
\ket{\psi} \rightarrow \frac{P_i \ket{\psi}}{\sqrt{\bra{\psi} P_i \ket{\psi}}}
$$

### Estado misto

$$
\rho \rightarrow \frac{P_i \rho P_i}{\mathrm{Tr}(P_i \rho)}
$$

### Propriedades importantes

* A transformação é **completamente positiva**
* Preserva o traço
* Não é unitária
* Não admite inversa (em geral)

## Medição como Canal Quântico

A medição projetiva pode ser vista como um **mapa quântico (canal)**:

### Caso não seletivo:

$$
\mathcal{E}(\rho) = \sum_i P_i \rho P_i
$$

Esse mapa possui propriedades estruturais importantes:

* É um canal CPTP (completely positive trace-preserving)
* Remove coerências entre subespaços
* Atua como um mecanismo formal de **decoerência**

## Decoerência Induzida por Medição

Após uma medição não seletiva, termos fora da diagonal na base dos projetores desaparecem:

Se:
$$
\rho = \sum_{i,j} c_{ij} \ket{i}\bra{j}
$$

então:
$$
\mathcal{E}(\rho) = \sum_i c_{ii} \ket{i}\bra{i}
$$

Isso significa:

* Perda de interferência quântica
* Conversão de superposição em mistura clássica
* Redução da informação quântica acessível

## Relação com Observáveis

Toda medição projetiva está associada a um operador hermitiano $A$:

$$
A = \sum_i a_i P_i
$$

Essa decomposição é única (até degenerescência) e define:

* $a_i$: valores possíveis medidos
* $P_i$: subespaços associados

### Degenerescência

Se múltiplos autovetores compartilham o mesmo autovalor:

* O projetor é de dimensão maior
* A medição não distingue estados dentro desse subespaço

## Compatibilidade de Medições

Duas medições são compatíveis se:

$$
[P_i, Q_j] = 0 \quad \forall i,j
$$

Equivalentemente:

$$
[A, B] = 0
$$

Consequências:

* Existe base comum de autovetores
* Medições simultâneas são possíveis
* A ordem das medições não altera o resultado

Caso contrário:

* Surge perturbação do estado
* A ordem das medições altera probabilidades

## Dependência de Base

A medição projetiva é intrinsecamente dependente da base escolhida.

Formalmente:

$$
P_i^{(U)} = U \ket{i}\bra{i} U^\dagger
$$

Isso implica que:

* Medir em uma base arbitrária equivale a aplicar uma unitária seguida de medição padrão
* Toda medição projetiva pode ser reduzida à base computacional

Esse princípio é central em algoritmos quânticos.

## Estrutura em Sistemas Compostos

Para sistemas compostos:

$$
\mathcal{H} = \mathcal{H}_A \otimes \mathcal{H}_B
$$

A medição pode atuar localmente:

$$
P_i = P_i^{(A)} \otimes I^{(B)}
$$

Consequências:

* A medição em $A$ pode afetar $B$ se houver entrelaçamento
* Pode induzir colapso não local

## Exemplo com Qubit

Estado inicial:

$$
\ket{\psi} = \frac{\ket{0} + \ket{1}}{\sqrt{2}}
$$

Projetores:

$$
P_0 = \ket{0}\bra{0}, \quad P_1 = \ket{1}\bra{1}
$$

Probabilidades:

$$
p(0) = p(1) = \frac{1}{2}
$$

Após aplicar Hadamard:

$$
H\ket{\psi} = \ket{0}
$$

Resultado:

* Probabilidade determinística
* Interferência construtiva

## Papel em Computação Quântica

A medição projetiva é essencial para:

### Extração de resultado

Todo algoritmo quântico termina com medição

### Controle de informação

Escolha da base define o que é observável

### Interferência

Resultados dependem da interferência antes da medição

### Sub-rotinas quânticas

Utilizada em:

* preparação de estados
* verificação
* filtragem de resultados

## Interpretação Física

A medição projetiva levanta questões fundamentais:

* O colapso não é descrito pela equação de Schrödinger
* Introduz descontinuidade na evolução do estado
* Depende implicitamente de um aparato clássico

Apesar disso:

* É extremamente bem validada experimentalmente
* Funciona como modelo operacional preciso

## Estrutura Informacional

Do ponto de vista da teoria da informação:

* A medição reduz a entropia quântica condicionalmente
* Pode aumentar entropia média (caso não seletivo)
* Converte informação quântica em clássica

## Conclusão

A medição projetiva é uma estrutura matemática rigorosa que:

* Define como resultados clássicos emergem de estados quânticos
* Introduz irreversibilidade e aleatoriedade
* Depende criticamente da escolha de base
* Atua como mecanismo formal de decoerência

Ela não é apenas um detalhe do formalismo, é o ponto onde toda computação quântica se conecta com o mundo observável.