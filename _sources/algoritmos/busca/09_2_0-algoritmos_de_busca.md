# Algoritmos de Busca

```{note}
Material extraído do TCC [*Computação Quântica: Uma abordagem para estudantes de graduação em Ciências Exatas*](../../tcc-giovani.pdf), de Giovani Goraiebe Pollachini.
```

Neste capítulo serão abordados os algoritmos de Busca, algoritmos que possuem o objetivo de encontrar um item específico em uma lista, ordenada ou não.

## Oráculos quânticos

O conceito de oráculo quântico foi retratado nos algoritmos introdutórios. Entratanto, para o entendimento dos algoritmos de busca, recomendamos ler novamente sobre os oráculos quânticos.

Os oráculos são funções booleanas $f \colon \{ 0,1 \}^n \to \{ 0,1 \}$ consideradas como ``caixas pretas''. Dado um vetor de bits $x$, o oráculo clássico fornece $f(x)$. Alguns problemas computacionais são escritos em termos de oráculos, como o problema de Deutsch-Jozsa, o problema de Simon e o problema de busca de Grover. Para abordar esses problemas, é necessário definir uma versão quântica desse oráculo, o que será abordado nesta seção. 
 
Há duas maneiras de se escrever um análogo quântico ao oráculo clássico: o oráculo XOR e o oráculo de fase.

### Oráculo XOR

O oráculo XOR é uma operação unitária que realiza a função booleana $f$ por meio de um bit extra, que sinaliza as entradas em que $f$ vale 1. 

![oraculo_xor](../../images/algoritmos/base/oraculo_xor.png)

### Construção do Oráculo de Fase usando o Oráculo XOR

Pode-se obter o oráculo de fase a partir do oráculo XOR com o uso do qubit alvo como um qubit auxiliar. Ao usarmos $\ket{-}$ na entrada alvo do oráculo XOR, obtemos, para qualquer estado $\ket{x}$ da base computacional:

$$
\ket{x}\ket{-} = \ket{x}\tfrac{\ket{0}-\ket{1}}{\sqrt{2}} \xrightarrow{O_{\text{XOR}}} 
  \begin{cases}
   \ket{x}\frac{\ket{0}-\ket{1}}{\sqrt{2}} = \ket{x}\ket{-}    &\text{se $f(x)=0$}  \\
   \ket{x}\frac{\ket{1}-\ket{0}}{\sqrt{2}} = \ket{x}(-\ket{-}) &\text{se $f(x)=1$} \ ,
  \end{cases}
$$

  o que pode ser resumido por $\ket{x}\big((-1)^{f(x)}\ket{-} \big)$. Além disso, o fator multiplicativo $(-1)^{f(x)}$ pode ser movido para qualquer entrada tensorial por multilinearidade do produto tensorial:

$$
\ket{x}\otimes(-1)^{f(x)}\ket{-} =  (-1)^{f(x)} \ket{x}\otimes\ket{-}
$$

A figura a seguir ilustra a construção do oráculo de fase.

![oraculo_fase.png](../../images/algoritmos/base/oraculo_fase.png)

## Conteúdo

Nesse capítulo serão abordados os seguintes algoritmos:

- [Algoritmo de Grover](09_2_1-grover.ipynb)
