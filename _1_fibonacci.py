# 1) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor 
# sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 
# 21, 34...), escreva um programa na linguagem que desejar onde, informado um 
# número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando 
# se o número informado pertence ou não a sequência.

# IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua 
# preferência ou pode ser previamente definido no código;

# calcula a sequencia de fibonacci e retorna se x pertence à sequencia
def belongs_fib(x):
    if x == 0 or x == 1:
        return True
    
    last_last = 0
    last = 1
    
    while last < x:
        aux = last
        last = last + last_last
        last_last = aux
        
        if last == x:
            return True
    
    # não encontrou x na sequencia
    return False

x = input("insira um número para verificar se esta na sequencia de fibonacci")

if belongs_fib(int(x)):
    print("o número informado pertence a sequencia")
else:
    print("o número informado não pertence a sequencia")
