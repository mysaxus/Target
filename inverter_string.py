# 5) Escreva um programa que inverta os caracteres de um string.

# IMPORTANTE:
# a) Essa string pode ser informada através de qualquer entrada 
# de sua preferência ou pode ser previamente definida no código;
# b) Evite usar funções prontas, como, por exemplo, reverse;

stringas = list(input())

for i in range(int(len(stringas)/2)):
  aux = stringas[len(stringas)-1-i]
  stringas[len(stringas)-1-i] = stringas[i]
  stringas[i] = aux
stringas = ''.join(stringas)
print(stringas)
