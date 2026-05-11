# Entropia de von Neumann

A **entropia de von Neumann** é uma das estruturas centrais da teoria da informação quântica, desempenhando o papel de medida fundamental de informação, incerteza e correlação em sistemas quânticos. Ela surge como uma generalização direta da entropia de Shannon para estados descritos por matrizes densidade, incorporando fenômenos exclusivamente quânticos como superposição, coerência e entrelaçamento.

Enquanto na teoria clássica a entropia quantifica a incerteza associada a uma distribuição de probabilidades, no contexto quântico ela mede a quantidade de informação inacessível sobre um sistema cuja descrição pode envolver combinações coerentes de estados. Dessa forma, a entropia de von Neumann não apenas caracteriza desordem estatística, mas também captura propriedades estruturais profundas da mecânica quântica.

Seu papel é extremamente amplo: aparece na formulação de limites fundamentais de comunicação quântica, na caracterização de entrelaçamento, na análise de canais quânticos, em termodinâmica quântica e até em teorias modernas envolvendo gravidade e informação.

## Estrutura Matemática e Interpretação Informacional

Considere um sistema quântico descrito por uma matriz densidade $\rho$. A entropia de von Neumann é definida por

$$
S(\rho) = -\mathrm{Tr}(\rho \log \rho)
$$

onde $\mathrm{Tr}$ representa o traço da matriz.

Diagonalizando $\rho$, obtemos uma decomposição espectral:

$$
\rho = \sum_i \lambda_i \ket{i}\bra{i}
$$

com $\lambda_i$ correspondendo aos autovalores da matriz densidade. Nesse caso, a entropia assume a forma

$$
S(\rho) = - \sum_i \lambda_i \log \lambda_i
$$

Essa expressão evidencia a forte analogia com a entropia de Shannon, já que os autovalores da matriz densidade formam uma distribuição de probabilidades. No entanto, a interpretação quântica é mais rica: os autovalores representam a estrutura estatística efetiva do estado, enquanto os autovetores codificam sua organização quântica.

Em geral, utiliza-se o logaritmo na base 2, fazendo com que a entropia seja medida em bits quânticos de informação.

Uma característica importante é que a entropia depende apenas do espectro da matriz densidade, sendo invariante sob transformações unitárias:

$$
S(U\rho U^\dagger) = S(\rho)
$$

Isso mostra que a entropia mede propriedades intrínsecas do estado e não da base utilizada para descrevê-lo.

## Estados Puros, Estados Mistos e Informação Quântica

A interpretação mais imediata da entropia de von Neumann é sua capacidade de distinguir estados puros de estados mistos.

Um estado puro possui a forma

$$
\rho = \ket{\psi}\bra{\psi}
$$

e satisfaz

$$
\rho^2 = \rho
$$

Nesse caso, existe apenas um autovalor igual a 1, enquanto todos os demais são nulos. Consequentemente,

$$
S(\rho) = 0
$$

Isso significa que o estado contém informação máxima possível sobre o sistema: não existe incerteza estatística intrínseca.

Por outro lado, estados mistos representam ensembles estatísticos de estados quânticos. Nesses casos, múltiplos autovalores são diferentes de zero, produzindo entropia positiva. Quanto mais uniforme for a distribuição espectral, maior será a entropia.

Para um sistema de dimensão $d$, o valor máximo possível da entropia é

$$
S_{\max} = \log d
$$

atingido pelo estado maximamente misto

$$
\rho = \frac{I}{d}
$$

Esse estado representa ausência completa de informação sobre o sistema.

Assim, a entropia de von Neumann mede o grau de mistura do estado e, simultaneamente, a quantidade de informação clássica faltante sobre sua preparação.

## Estrutura Estatística e Coerência Quântica

Embora a entropia dependa apenas dos autovalores da matriz densidade, ela está profundamente relacionada à coerência quântica.

Considere dois estados com o mesmo espectro. Ambos possuem a mesma entropia, mesmo que um deles apresente coerências fora da diagonal em determinada base. Isso evidencia que a entropia de von Neumann não mede coerência diretamente, mas sim a estrutura probabilística global do estado.

Ainda assim, processos que destroem coerências — como decoerência e medições não seletivas — frequentemente aumentam a entropia do sistema, pois convertem superposições quânticas em misturas clássicas.

Nesse sentido, a entropia conecta informação quântica e irreversibilidade física.

## Sistemas Compostos e Entrelaçamento

A entropia de von Neumann assume um papel ainda mais profundo em sistemas compostos.

Considere um sistema bipartido descrito por

$$
\rho_{AB}
$$

As matrizes reduzidas são definidas por traço parcial:

$$
\rho_A = \mathrm{Tr}*B(\rho*{AB}),
\qquad
\rho_B = \mathrm{Tr}*A(\rho*{AB})
$$

Quando o sistema total está em um estado puro mas os subsistemas possuem entropia positiva, surge um dos fenômenos mais característicos da mecânica quântica: o entrelaçamento.

Considere, por exemplo, o estado de Bell

$$
\ket{\Phi^+} =
\frac{1}{\sqrt{2}}(\ket{00} + \ket{11})
$$

O sistema total satisfaz

$$
S(\rho_{AB}) = 0
$$

pois o estado global é puro. Entretanto, cada subsistema individual possui matriz reduzida

$$
\rho_A = \rho_B = \frac{I}{2}
$$

resultando em

$$
S(\rho_A) = S(\rho_B) = 1
$$

Esse resultado é profundamente não clássico: individualmente, cada qubit parece completamente aleatório, embora o sistema conjunto possua informação perfeitamente definida.

A entropia dos subsistemas torna-se, portanto, uma medida natural de entrelaçamento para estados puros bipartidos.

## Propriedades Fundamentais

A entropia de von Neumann possui propriedades matemáticas fundamentais que estruturam grande parte da teoria da informação quântica.

Ela é sempre não negativa:

$$
S(\rho) \geq 0
$$

e é côncava, refletindo o fato de que misturas estatísticas aumentam incerteza.

Além disso, satisfaz a importante propriedade de subaditividade:

$$
S(\rho_{AB}) \leq S(\rho_A) + S(\rho_B)
$$

e a desigualdade forte de subaditividade, considerada uma das estruturas centrais da teoria da informação quântica.

Outra característica notável é que, diferentemente do caso clássico, a entropia condicional quântica pode assumir valores negativos:

$$
S(A|B) = S(\rho_{AB}) - S(\rho_B)
$$

Esse comportamento está diretamente ligado ao entrelaçamento e não possui análogo clássico.

## Papel em Comunicação e Computação Quântica

A entropia de von Neumann aparece em praticamente toda a teoria da informação quântica moderna.

Ela é central no **teorema de compressão de Schumacher**, que estabelece o limite fundamental para compressão de estados quânticos, desempenhando papel análogo ao teorema de Shannon na teoria clássica.

Também surge no **teorema de Holevo**, que limita a quantidade de informação clássica extraível de sistemas quânticos.

Em canais quânticos, a entropia é utilizada para definir capacidades de transmissão, caracterizar ruído e analisar perda de coerência.

Na computação quântica, ela é amplamente utilizada para:

* caracterização de entrelaçamento;
* análise de decoerência;
* estudo de complexidade quântica;
* validação de estados preparados experimentalmente.

Além disso, em termodinâmica quântica, a entropia conecta informação e energia, aparecendo em formulações modernas da segunda lei da termodinâmica.

## Relação com Decoerência e Medição

A medição quântica frequentemente produz aumento de entropia ao destruir coerências do sistema.

Quando um estado sofre decoerência, os termos fora da diagonal da matriz densidade desaparecem gradualmente, transformando superposições em misturas estatísticas. Esse processo corresponde a uma perda de informação quântica acessível e, em geral, a um crescimento entrópico.

Assim, a entropia de von Neumann fornece uma descrição quantitativa da transição entre comportamento quântico e clássico.

Ela também permite compreender por que processos irreversíveis emergem naturalmente em sistemas quânticos abertos.

## Considerações Finais

A entropia de von Neumann constitui uma das quantidades mais profundas da física moderna. Mais do que uma simples medida de desordem, ela organiza matematicamente conceitos fundamentais como informação, coerência, mistura estatística e entrelaçamento.

Seu formalismo revela que informação quântica possui uma estrutura muito mais rica do que a informação clássica, permitindo fenômenos sem equivalente no mundo clássico, como entropia condicional negativa e correlações não locais.

Por esse motivo, a entropia de von Neumann tornou-se uma ferramenta indispensável não apenas na computação quântica, mas em praticamente toda a teoria quântica contemporânea. 
