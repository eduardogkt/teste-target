# 2) Escreva um programa que verifique, em uma string, a existência da letra ‘a’, 
# seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela 
# ocorre.

# IMPORTANTE: Essa string pode ser informada através de qualquer entrada de sua 
# preferência ou pode ser previamente definida no código;

def count_a(string):
    count = 0
    length = len(string)
    i = 0
    
    while i < length:
        if string[i] == 'a' or string[i] == 'A':
            count += 1
        i += 1
    
    return count

string = "hgdfgkfg djf "

count = count_a(string)
print(count)