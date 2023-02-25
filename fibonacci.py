# 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores
# anteriores(exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde,
# informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número
# informado pertence ou não a sequência.

def fibonacci(n):                                                           #Funcão para calcular o fibonacci
    a=0
    b=1
    while b < n:                                                           #Calculando o fibonacci
        a=b
        b=a + b
    if b == n:                                                              #Verificando se o numero está na sequencia
        return True
    else:
        return False

num=int(input('Informe um número inteiro positivo: '))                      #Recebendo o valor

if num <= 0:                                                                #Descartando caso seja zero ou negativo
    print('Informe um número positivo')
else:                                                                       #Printando a resposta
    if fibonacci(num):
        print(f"O número {num} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {num} não pertence à sequência de Fibonacci.")
