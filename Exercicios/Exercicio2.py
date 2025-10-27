### Exercício 2: Resto da Divisão por 5

try:
    # Verifica se a  entrada do usuário para um inteiro
    numero = int(input("Digite um número: "))
    print("O resto da divisão de", numero, "por 5 é:", numero % 5)


except ValueError:
    # Se ocorrer um erro de conversão, informa o usuário
    print("Entrada inválida! Por favor, digite apenas números")