#Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor
#sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8,
#13, 21, 34...), escreva um programa na linguagem que desejar onde, informa
#do um número, ele calcule a sequência de Fibonacci e retorne uma mensagem 
#avisando se o número informado pertence ou não a sequência.
def f(x): 
  if x<=1: return x
  return f(x-1) + f(x-2)

z = int(input()) 

for i in range(z+6):
  if(f(i)==z): 
    print('{0} pertence à sequência de Fibonacci.'.format(z))
    break
  if(f(i)>z): 
    print('{0} não pertence à sequência de Fibonacci.'.format(z))
    break
