# Métodos Numéricos — Problema das Duas Vigas

> Projeto desenvolvido para a disciplina de **Métodos Numéricos**.

Este projeto tem como objetivo determinar numericamente a largura `x` de um galpão no problema das duas vigas, utilizando e comparando três métodos de resolução de equações não lineares:

- 🔹 Método da Bisseção
- 🔹 Método de Newton-Raphson
- 🔹 Método da Secante

O objetivo é observar a convergência dos métodos, comparar o número de iterações e verificar o desempenho de cada método para este problema.

---

## 1. Objetivo do projeto

Determinar numericamente a largura `x` do galpão no problema das duas vigas, comparando três métodos de resolução de equações não lineares:

- **Bisseção**
- **Newton-Raphson**
- **Secante**

O objetivo é observar a convergência dos métodos, comparar o número de iterações e verificar qual método apresenta o melhor desempenho para este problema.

---

## 2. Enunciado

Duas vigas de madeira, com comprimentos de **20 m e 30 m**, estão adaptadas entre paredes alternativas de um galpão. As vigas se cruzam a uma altura de **8 m** em relação ao chão.

As alturas alcançadas pelas vigas nas paredes são:

$$
a = \sqrt{30^2-x^2}
$$

$$
b = \sqrt{20^2-x^2}
$$

A condição do problema é:

$$
\frac{1}{8} = \frac{1}{a} + \frac{1}{b}
$$

Substituindo `a` e `b`:

$$
\frac{1}{8} = \frac{1}{\sqrt{900-x^2}} + \frac{1}{\sqrt{400-x^2}}
$$

O problema consiste em encontrar numericamente `x`.

---

## 3. 📐 Formulação da função

Para aplicar os métodos numéricos, colocamos toda a expressão em um único lado:

$$
f(x) = \frac{1}{8} - \frac{1}{\sqrt{900-x^2}} - \frac{1}{\sqrt{400-x^2}}
$$

Assim, procuramos uma raiz tal que:

$$
\boxed{f(x)=0}
$$

### Derivada para Newton-Raphson

O método de Newton-Raphson precisa da derivada de `f(x)`:

$$
f'(x) = -\frac{x}{(900-x^2)^{3/2}} - \frac{x}{(400-x^2)^{3/2}}
$$

---

## 4. Restrições físicas

Como `x` aparece dentro de raízes quadradas, é necessário respeitar:

$$
900-x^2 > 0
$$

e

$$
400-x^2 > 0
$$

A restrição mais forte vem da viga de **20 m**:

$$
0 \leq x < 20
$$

Portanto, a solução deve estar nesse intervalo.

Para a Bisseção foi utilizado o intervalo inicial:

$$
[0,19{,}9]
$$

Nesse intervalo:

$$
f(0)>0
$$

$$
f(19{,}9)<0
$$

Logo, existe uma raiz entre os dois pontos.

---

# 5. Métodos utilizados

## 5.1 Método da Bisseção

A Bisseção começa com um intervalo `[a,b]` onde existe mudança de sinal.

Calcula-se o ponto médio:

$$
x_m = \frac{a+b}{2}
$$

Depois verifica-se em qual metade do intervalo permanece a mudança de sinal.

### ✅ Vantagens

- Muito simples.
- É robusto.
- Mantém a raiz dentro do intervalo.

### ❌ Desvantagem

- Normalmente precisa de muitas iterações.

---

## 5.2 Método de Newton-Raphson

O método utiliza a derivada da função:

$$
x_{k+1} = x_k - \frac{f(x_k)}{f'(x_k)}
$$

Foi utilizado como chute inicial:

$$
x_0=15
$$

### ✅ Vantagens

- A convergência é muito rápida quando o chute inicial é adequado.
- Para este problema, chegou à solução em poucas iterações.

### ❌ Desvantagens

- Precisa da derivada.
- Um chute ruim pode fazer o método divergir ou sair do domínio físico.

---

## 5.3 Método da Secante

A Secante é semelhante ao método de Newton-Raphson, mas não precisa que a derivada seja calculada explicitamente.

A fórmula utilizada é:

$$
x_{k+1} = x_k - f(x_k) \frac{x_k-x_{k-1}} {f(x_k)-f(x_{k-1})}
$$

Foram utilizados:

$$
x_0=10
$$

$$
x_1=19
$$

### ✅ Vantagens

- Não precisa da derivada.
- É mais rápida que a Bisseção neste exemplo.

### ❌ Desvantagem

- Não possui a mesma garantia de confinamento da Bisseção.

---

# 6. Resultado dos três métodos

Foi utilizada a tolerância:

$$
\varepsilon=10^{-10}
$$

| Método | Chute / Intervalo inicial | Iterações | Resultado de `x` (m) | Erro residual |
|---|---|---:|---:|---:|
| Bisseção | `[0, 19,9]` | 28 | 16,2121258993 | 2,862e-11 |
| Newton-Raphson | `x₀ = 15` | 4 | 16,2121258971 | 4,309e-12 |
| Secante | `x₀ = 10, x₁ = 19` | 9 | 16,2121258969 | 2,501e-12 |

### Comparação

O Newton-Raphson foi o mais rápido neste problema, precisando de apenas **4 iterações** para cumprir a tolerância.

A Bisseção utilizou **28 iterações**, mas apresenta a vantagem de ser mais robusta por manter a raiz dentro do intervalo escolhido.

A Secante apresentou um resultado intermediário, com **9 iterações**, sem necessidade de calcular a derivada.

---

# 7. Iterações — Bisseção

O método da Bisseção convergiu em **28 iterações**.

| k | a | b | xₖ | f(xₖ) | \|f(xₖ)\| |
|---:|---:|---:|---:|---:|---:|
| 1 | 0,0000000000 | 19,9000000000 | 9,9500000000 | 3,203e-02 | 3,203e-02 |
| 2 | 9,9500000000 | 19,9000000000 | 14,9250000000 | 1,146e-02 | 1,146e-02 |
| 3 | 14,9250000000 | 19,9000000000 | 17,4125000000 | -1,757e-02 | 1,757e-02 |
| 4 | 14,9250000000 | 17,4125000000 | 16,1687500000 | 4,774e-04 | 4,774e-04 |
| 5 | 16,1687500000 | 17,4125000000 | 16,7906250000 | -7,252e-03 | 7,252e-03 |
| 6 | 16,1687500000 | 16,7906250000 | 16,4796875000 | -3,135e-03 | 3,135e-03 |
| 7 | 16,1687500000 | 16,4796875000 | 16,3242187500 | -1,272e-03 | 1,272e-03 |
| 8 | 16,1687500000 | 16,3242187500 | 16,2464843750 | -3,840e-04 | 3,840e-04 |
| 9 | 16,1687500000 | 16,2464843750 | 16,2076171875 | 5,000e-05 | 5,000e-05 |
| 10 | 16,2076171875 | 16,2464843750 | 16,2270507812 | -1,661e-04 | 1,661e-04 |
| 11 | 16,2076171875 | 16,2270507812 | 16,2173339844 | -5,787e-05 | 5,787e-05 |
| 12 | 16,2076171875 | 16,2173339844 | 16,2124755859 | -3,882e-06 | 3,882e-06 |
| 13 | 16,2076171875 | 16,2124755859 | 16,2100463867 | 2,307e-05 | 2,307e-05 |
| 14 | 16,2100463867 | 16,2124755859 | 16,2112609863 | 9,599e-06 | 9,599e-06 |
| 15 | 16,2112609863 | 16,2124755859 | 16,2118682861 | 2,859e-06 | 2,859e-06 |
| 16 | 16,2118682861 | 16,2124755859 | 16,2121719360 | -5,110e-07 | 5,110e-07 |
| 17 | 16,2118682861 | 16,2121719360 | 16,2120201111 | 1,174e-06 | 1,174e-06 |
| 18 | 16,2120201111 | 16,2121719360 | 16,2120960236 | 3,316e-07 | 3,316e-07 |
| 19 | 16,2120960236 | 16,2121719360 | 16,2121339798 | -8,972e-08 | 8,972e-08 |
| 20 | 16,2120960236 | 16,2121339798 | 16,2121150017 | 1,209e-07 | 1,209e-07 |
| 21 | 16,2121150017 | 16,2121339798 | 16,2121244907 | 1,561e-08 | 1,561e-08 |
| 22 | 16,2121244907 | 16,2121339798 | 16,2121292353 | -3,706e-08 | 3,706e-08 |
| 23 | 16,2121244907 | 16,2121292353 | 16,2121268630 | -1,073e-08 | 1,073e-08 |
| 24 | 16,2121244907 | 16,2121268630 | 16,2121256769 | 2,440e-09 | 2,440e-09 |
| 25 | 16,2121256769 | 16,2121268630 | 16,2121262699 | -4,143e-09 | 4,143e-09 |
| 26 | 16,2121256769 | 16,2121262699 | 16,2121259734 | -8,515e-10 | 8,515e-10 |
| 27 | 16,2121256769 | 16,2121259734 | 16,2121258251 | 7,942e-10 | 7,942e-10 |
| 28 | 16,2121258251 | 16,2121259734 | 16,2121258993 | -2,862e-11 | 2,862e-11 |

---

# 8. Iterações — Newton-Raphson

| k | xₖ | f(xₖ) | f'(xₖ) | xₖ₊₁ | \|f(xₖ₊₁)\| |
|---:|---:|---:|---:|---:|---:|
| 1 | 15,0000000000 | 1,092e-02 | -7,335e-03 | 16,4884113449 | 3,243e-03 |
| 2 | 16,4884113449 | -3,243e-03 | -1,242e-02 | 16,2272188956 | 1,680e-04 |
| 3 | 16,2272188956 | -1,680e-04 | -1,117e-02 | 16,2121704568 | 4,946e-07 |
| 4 | 16,2121704568 | -4,946e-07 | -1,110e-02 | 16,2121258971 | 4,309e-12 |

---

# 9. Iterações — Secante

| k | xₖ₋₁ | xₖ | xₖ₊₁ | f(xₖ₊₁) | \|f(xₖ₊₁)\| |
|---:|---:|---:|---:|---:|---:|
| 1 | 10,0000000000 | 19,0000000000 | 12,6081602309 | 2,385e-02 | 2,385e-02 |
| 2 | 19,0000000000 | 12,6081602309 | 14,1021577770 | 1,672e-02 | 1,672e-02 |
| 3 | 12,6081602309 | 14,1021577770 | 17,6051836122 | -2,154e-02 | 2,154e-02 |
| 4 | 14,1021577770 | 17,6051836122 | 15,6330050033 | 5,780e-03 | 5,780e-03 |
| 5 | 17,6051836122 | 15,6330050033 | 16,0502278494 | 1,742e-03 | 1,742e-03 |
| 6 | 15,6330050033 | 16,0502278494 | 16,2302109560 | -2,015e-04 | 2,015e-04 |
| 7 | 16,0502278494 | 16,2302109560 | 16,2115550586 | 6,335e-06 | 6,335e-06 |
| 8 | 16,2302109560 | 16,2115550586 | 16,2121238778 | 2,241e-08 | 2,241e-08 |
| 9 | 16,2115550586 | 16,2121238778 | 16,2121258969 | -2,501e-12 | 2,501e-12 |

---

# 10. Verificação da solução

Usando a solução obtida pelo método de Newton-Raphson:

$$
x \approx 16,2121258971\text{ m}
$$

Calculamos as alturas:

$$
a = \sqrt{900-x^2} \approx25,2421665848\text{ m}
$$

$$
b = \sqrt{400-x^2} \approx11,7118305101\text{ m}
$$

Substituindo na equação original:

$$
\frac{1}{a}+\frac{1}{b} \approx0,125000000004
$$

Enquanto:

$$
\frac{1}{8}=0,125000000000
$$

O erro é:

$$
\left| \frac{1}{8} - \frac{1}{a} - \frac{1}{b} \right| \approx4,309\times10^{-12}
$$

A diferença é praticamente zero dentro da tolerância definida.

### Resultado final

$$
\boxed{x\approx16,212126\text{ m}}
$$

A largura do galpão é aproximadamente **16,21 metros**.

---

# 11. Código utilizado no Jupyter Notebook

O caderno deste projeto contém as células abaixo, realizadas em sequência.

## Importação das bibliotecas

```python
import math
import pandas as pd
import matplotlib.pyplot as plt
```

A principal biblioteca matemática utilizada é `math`, para raízes e operações matemáticas.

A biblioteca `pandas` é utilizada para organizar as tabelas de iterações e `matplotlib` para visualizar a função e a raiz.

---

## Função

```python
def f(x):
    return (
        1/8
        - 1/math.sqrt(30**2 - x**2)
        - 1/math.sqrt(20**2 - x**2)
    )
```

---

## Derivada

```python
def df(x):
    return (
        -x/(30**2 - x**2)**1.5
        -x/(20**2 - x**2)**1.5
    )
```

---

## Método da Bisseção

```python
def bissecao(a, b, tol=1e-10, max_iter=100):
    fa = f(a)
    historico = []

    for k in range(1, max_iter + 1):
        x = (a + b) / 2
        fx = f(x)

        historico.append([k, a, b, x, fx, abs(fx)])

        if abs(fx) < tol or (b - a) / 2 < tol:
            return x, historico

        if fa * fx < 0:
            b = x
        else:
            a = x
            fa = fx

    return x, historico
```

---

## Método de Newton-Raphson

```python
def newton(x0, tol=1e-10, max_iter=100):
    historico = []
    x = x0

    for k in range(1, max_iter + 1):
        fx = f(x)
        dfx = df(x)

        x_novo = x - fx / dfx

        historico.append([
            k,
            x,
            fx,
            dfx,
            x_novo,
            abs(f(x_novo))
        ])

        x = x_novo

        if abs(f(x)) < tol:
            return x, historico

    return x, historico
```

---

## Método da Secante

```python
def secante(x0, x1, tol=1e-10, max_iter=100):
    historico = []

    f0 = f(x0)
    f1 = f(x1)

    for k in range(1, max_iter + 1):
        x2 = x1 - f1 * (x1 - x0) / (f1 - f0)
        f2 = f(x2)

        historico.append([
            k,
            x0,
            x1,
            x2,
            f2,
            abs(f2)
        ])

        if abs(f2) < tol:
            return x2, historico

        x0, x1 = x1, x2
        f0, f1 = f1, f2

    return x2, historico
```

---

## Execução

```python
x_bis, hist_bis = bissecao(0, 19.9)
x_newton, hist_newton = newton(15)
x_sec, hist_sec = secante(10, 19)
```

```python
print("Bisseção:", x_bis)
print("Newton-Raphson:", x_newton)
print("Secante:", x_sec)
```

---

## Tabelas

```python
df_bis = pd.DataFrame(
    hist_bis,
    columns=["Iteração", "a", "b", "x", "f(x)", "|f(x)|"]
)
```

```python
df_newton = pd.DataFrame(
    hist_newton,
    columns=[
        "Iteração",
        "x_k",
        "f(x_k)",
        "f'(x_k)",
        "x_k+1",
        "|f(x_k+1)|"
    ]
)
```

```python
df_sec = pd.DataFrame(
    hist_sec,
    columns=[
        "Iteração",
        "x_k-1",
        "x_k",
        "x_k+1",
        "f(x_k+1)",
        "|f(x_k+1)|"
    ]
)
```

```python
exibir(df_bis)
exibir(df_newton)
exibir(df_sec)
```

---

## Verificação

```python
a = math.sqrt(30**2 - x_newton**2)
b = math.sqrt(20**2 - x_newton**2)

lado_esquerdo = 1/8
lado_direito = 1/a + 1/b
```

```python
print("x =", x_newton)
print("a =", a)
print("b =", b)
print("1/8 =", lado_esquerdo)
print("1/a + 1/b =", lado_direito)
print("Erro =", abs(lado_esquerdo - lado_direito))
```

---

# 12. Bibliotecas utilizadas

| Biblioteca | Utilidade |
|---|---|
| `math` | Raiz quadrada e operações matemáticas |
| `pandas` | Tabelas e organização das iterações |
| `matplotlib` | Gráficos da função e visualização da raiz |
| Jupyter Notebook | Execução documentada do código |

Todas são bibliotecas comuns do ecossistema Python.

Caso necessário, podem ser instaladas com:

```bash
pip install pandas matplotlib jupyter
```

---

# 13. Pré-requisitos

- Python 3
- Jupyter Notebook
- Google Colab ou Jupyter local
- Pandas
- Matplotlib
- Git
- GitHub

---

# 14. Verificação computacional

Além da comparação entre os métodos, a solução foi verificada novamente na equação original.

Uma solução foi:

$$
x\approx16,212126\text{ m}
$$

O erro residual foi:

$$
4,309\times10^{-12}
$$

Isso confirma que a solução numérica foi obtida dentro da tolerância de:

$$
10^{-10}
$$

---

# 15. Conclusão

Os três métodos foram capazes de encontrar praticamente o mesmo valor para a largura do galpão:

$$
\boxed{x\approx16,212126\text{ m}}
$$

Os resultados mostraram que:

- **Bisseção:** mais robusta, porém mais lenta.
- **Newton-Raphson:** mais rápido neste problema, utilizando a derivada.
- **Secante:** boa alternativa quando não se deseja calcular a derivada.

O Newton-Raphson foi utilizado como método principal, pois convergiu em apenas **4 iterações**, contra **28 da Bisseção** e **9 da Secante**.

É importante destacar que essa escolha é específica para as condições utilizadas no projeto:

- Chute inicial: `x₀ = 15`
- Tolerância: `10⁻¹⁰`
- Função utilizada no problema

A Bisseção continua sendo uma opção interessante quando a prioridade é a robustez.

---

# 16. Equipe de alunos

- Anderson Rodrigues
- Arthur Henrique
- José Everton
- Kelly Acioli
- Ronald Chaves

---

# 17. Professor

**Paulo Rocha**

### Disciplina

**Métodos Numéricos**

---

# 18. Referências

RUGGIERO, Márcia A. Gomes; LOPES, Vera Lúcia da Rocha. *Cálculo numérico: aspectos teóricos e computacionais*. 2. ed. São Paulo: Pearson Makron Books, 1996.

Métodos numéricos e computacionais na prática de engenharias e ciências / Reyolando M. L. R. F. Brasil, José Manoel Balthazar, Wesley Góis. – São Paulo: Blucher, 2015. 

Material didático da disciplina de Métodos Numéricos disponibilizado pelo professor.
