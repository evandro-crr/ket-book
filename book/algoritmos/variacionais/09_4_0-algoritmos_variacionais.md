# Algoritmos Variacionais Quânticos (VQAs)

Os Algoritmos Variacionais Quânticos (VQAs) representam uma das abordagens mais promissoras para explorar o potencial dos computadores quânticos da era NISQ (Noisy Intermediate-Scale Quantum), dispositivos com dezenas a centenas de qubits, ainda sujeitos a ruído e erros. 

Esses algoritmos combinam processamento quântico e clássico de forma híbrida, utilizando o computador quântico para preparar e medir estados quânticos, e o computador clássico para ajustar parâmetros e minimizar uma função de custo. 

Essa arquitetura híbrida permite contornar as limitações atuais do hardware quântico, tornando os VQAs uma das principais ferramentas para aplicações práticas de curto prazo, como otimização, simulação de sistemas físicos e aprendizado de máquina quântico.

```{note}
Material extraído do Artigo [*Quantum Finance: um tutorial de computação quântica aplicada ao mercado financeiro*](./artigo_hamiltoniano.pdf).
```

## Como eles Funcionam

A ideia central dos VQAs é a seguinte:

1. **Preparação do Estado Parametrizado:**
   Um circuito quântico $U(\boldsymbol{\theta})$ é preparado, dependendo de um conjunto de parâmetros clássicos $\boldsymbol{\theta} = (\theta_1, \theta_2, ..., \theta_n)$.
   Esses parâmetros controlam rotações e operações que definem o estado quântico $\ket{\psi(\boldsymbol{\theta})} = U(\boldsymbol{\theta})\ket{0}$.

2. **Medição de um Observável:**
   Mede-se o valor esperado de um **Observável, que pode ser Hamiltoniano** $H$, que representa o problema físico ou matemático a ser resolvido.
   Essa medida fornece a **função de custo**:
   
   $$
   C(\boldsymbol{\theta}) = \bra{\psi(\boldsymbol{\theta})} H \ket{\psi(\boldsymbol{\theta})}
   $$

3. **Otimização Clássica:**
   Um **otimizador clássico** (como gradient descent, Nelder–Mead ou Adam) ajusta os parâmetros $\boldsymbol{\theta}$ para minimizar o valor de $C(\boldsymbol{\theta})$.

4. **Iteração:**
   O processo se repete até atingir a convergência, ou seja, até encontrar um conjunto de parâmetros que minimize a energia esperada.

Esse ciclo híbrido, **preparação → medição → otimização → atualização**, é o núcleo de qualquer VQA.

### O que é o Observável

Em mecânica quântica, um **observável** é qualquer grandeza física que pode ser medida em um sistema quântico - como energia, magnetização, posição, momento ou qualquer quantidade derivada delas.

Matematicamente, um observável é representado por um **operador Hermitiano** (ou seja, um operador igual ao seu próprio adjunto). Essa propriedade garante que os valores obtidos ao medir o observável sejam **reais**, como esperado em uma medida física.

Nos Algoritmos Variacionais Quânticos (VQAs), o observável desempenha um papel fundamental: ele define **a função de custo** que se deseja minimizar.

#### Observável como Função de Custo

Ao aplicar o circuito parametrizado $U(\boldsymbol{\theta})$ sobre o estado inicial, obtém-se um estado variacional $\ket{\psi(\boldsymbol{\theta})}$.

O valor esperado do observável $O$ nesse estado é dado por:

$$
\langle O \rangle_{\boldsymbol{\theta}} =
\bra{\psi(\boldsymbol{\theta})} O \ket{\psi(\boldsymbol{\theta})}
$$

Esse valor esperado é exatamente o que o VQA usa como **função objetivo** a ser minimizada (ou maximizada), dependendo do problema.

Se $O$ for o Hamiltoniano $H$ do sistema, então:

* Minimizar $\langle H \rangle$ significa buscar o **estado fundamental**.
* Maximizar $\langle O \rangle$ pode ser útil em certos problemas de machine learning quântico.

### O que é o Hamiltoniano

O **Hamiltoniano** é um operador fundamental na mecânica quântica, representando a **energia total** (cinética + potencial) de um sistema.
Nos VQAs, ele é usado para **codificar o problema que se deseja resolver**.

Por exemplo:

- Em problemas de **simulação de sistemas físicos**, o Hamiltoniano descreve o comportamento de elétrons, spins, ou partículas em um campo.

- Em problemas de **otimização combinatória**, o Hamiltoniano é construído de modo que seu **estado fundamental (menor energia)** corresponda à **melhor solução do problema clássico**.

Matematicamente, ele pode ser escrito como uma soma de produtos de operadores de Pauli:

$$
H = \sum_i h_i P_i
$$

onde cada $P_i$ é uma combinação de operadores $I, X, Y, Z$ aplicados aos qubits, e $h_i$ são coeficientes reais.

Em termos práticos: o Hamiltoniano é o “coração” do problema. Ele define **o que o algoritmo quer minimizar** — seja energia, erro ou custo. 

## Conteúdo

Nesse capítulo serão abordados os seguintes algoritmos:

- [Algoritmo Quântico de Otimização Aproximada (QAOA)](09_4_1-QAOA.ipynb)
- [Algoritmo Baseado em Feedback para Otimização Quântica Linear (FALQON)](09_4_2-FALQON.ipynb)
