# 4) Dado o valor de faturamento mensal de uma distribuidora,
#detalhado por estado:

# SP – R$67.836,43
# RJ – R$36.678,66
# MG – R$29.229,88
# ES – R$27.165,48
# Outros – R$19.849,53

# Escreva um programa na linguagem que desejar onde calcule o 
# percentual de representação que cada estado teve dentro do
# valor total mensal da distribuidora.


SP = 67836.43
RJ = 36678.66
MG = 29229.88
ES = 27165.48
Outros = 19849.53
arr = {'SP': SP,'RJ': RJ,'MG': MG,'ES': ES,'Outros': Outros}
total=0

for i in arr.values():
  total += i
# MODO DE INPUT (imprime o que o percentual do estado de sua 
# escolha)

# print('Insira o estado cujo faturamento mensal é desejado.')
# estado = input()


# if estado not in arr.keys():
#   estado = 'Outros'
# x = arr[estado]*100/total
# print("{:.2f}%".format(x))

# MODO RELATÓRIO (imprime todos os percentuais disponíveis)

print('Percentuais disponíveis:')
print()
for i, y in arr.items():
  print('{0}: {1}'.format(i, y))
  print('----------')
  print('Percentual: {:.2f}%'.format(y*100/total))
  print()
