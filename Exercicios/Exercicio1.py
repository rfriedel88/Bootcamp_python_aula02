# Exercício 1: Soma de Dois Números Inteiros


## Resposta com Validação de Entrada

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
  
      