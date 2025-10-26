# Bootcamp_python_aula02

Aula focada em tipos de variáveis e operações básicas em python, além de estratégias de prevenção e contorno de erros.

---
Repositório da Aula : <https://github.com/lvgalvao/data-engineering-roadmap/tree/main/Bootcamp%20-%20Python%20para%20dados/aula02>

---

## Lista de Exercícios

### Exercício 1: Soma de Dois Números Inteiros

[Exercicio1_Basico.py](Exercicios/Exercicio1_Basico.py)


```python
primerio_numero = int(input("Digite o primeiro número inteiro: "))
segundo_numero = int(input("Digite o segundo número inteiro: "))
soma = primerio_numero + segundo_numero
print("A soma dos dois números Digitados é:", soma)
```
[Exercicio1_Validacao.py](Exercicios/Exercicio1_Validacao.py)

``` python
try:
    # Tenta converter a entrada do usuário para um inteiro
    numero1 = int(input("Digite o primeiro número inteiro: "))
    
    # Se o primeiro número foi válido, tenta obter e converter o segundo
    numero2 = int(input("Digite o segundo número inteiro: "))

    # Se ambas as conversões funcionaram, realiza a soma
    soma = numero1 + numero2
    
    # Imprime o resultado final
    print("A soma dos dois números digitados é:", soma)

except ValueError:
    # Se ocorrer um erro de conversão, informa o usuário
    print("Entrada inválida! Por favor, digite apenas números inteiros.")
```