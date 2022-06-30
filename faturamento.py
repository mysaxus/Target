# Dado um vetor que guarda o valor de faturamento diário de uma
# distribuidora, faça um programa, na linguagem que desejar, que
# calcule e retorne:
# • O menor valor de faturamento ocorrido em um dia do mês;
# • O maior valor de faturamento ocorrido em um dia do mês;
# • Número de dias no mês em que o valor de faturamento diário
# foi superior à média mensal.

import json

dados = """{
  "faturamento": [ 
    {"dia": 1, "semana": "segunda-feira", "valor": 32426},
    {"dia": 2, "semana": "terça-feira", "valor": 17534},
    {"dia": 3, "semana": "quarta-feira", "valor": 28293},
    {"dia": 4, "semana": "quinta-feira", "valor": 26353},
    {"dia": 5, "semana": "sexta-feira", "valor": 19836},
    {"dia": 6, "semana": "sábado", "valor": 0},
    {"dia": 7, "semana": "domingo", "valor": 0},
    {"dia": 8, "semana": "segunda-feira", "valor": 19051},
    {"dia": 9, "semana": "terça-feira", "valor": 33604},
    {"dia": 10, "semana": "quarta-feira", "valor": 21964},
    {"dia": 11, "semana": "quinta-feira", "valor": 16820},
    {"dia": 12, "semana": "sexta-feira", "valor": 24030},
    {"dia": 13, "semana": "sábado", "valor": 0},
    {"dia": 14, "semana": "domingo", "valor": 0},
    {"dia": 15, "semana": "segunda-feira", "valor": 22441},
    {"dia": 16, "semana": "terça-feira", "valor": 19314},
    {"dia": 17, "semana": "quarta-feira", "valor": 26498},
    {"dia": 18, "semana": "quinta-feira", "valor": 17070},
    {"dia": 19, "semana": "sexta-feira", "valor": 21847},
    {"dia": 20, "semana": "sábado", "valor": 0},
    {"dia": 21, "semana": "domingo", "valor": 0},
    {"dia": 22, "semana": "segunda-feira", "valor": 25851},
    {"dia": 23, "semana": "terça-feira", "valor": 18224},
    {"dia": 24, "semana": "quarta-feira", "valor": 29452},
    {"dia": 25, "semana": "quinta-feira", "valor": 20627},
    {"dia": 26, "semana": "sexta-feira", "valor": 25498},
    {"dia": 27, "semana": "sábado", "valor": 0},
    {"dia": 28, "semana": "domingo", "valor": 0},
    {"dia": 29, "semana": "segunda-feira", "valor": 30020},
    {"dia": 30, "semana": "terça-feira", "valor": 34032}
  ]
}"""

dic = json.loads(dados)
y = []

total = 0
count = 0 #valores superiores a media
z = 0 #valores válidos (!=0)
for i in range(len(dic['faturamento'])):
  x = dic['faturamento'][i]['valor']
  if x==0: continue
  z+=1
  total += x
  y.append(x)
  
media = total/z
y.sort()

for i in range (z):
  if int(y[i])>media : count += 1


print("Menor valor de faturamento do mês: ", y[len(y)-z])
print("Maior valor de faturamento do mês: ", y[len(y) - 1])
print("Número de dias com faturamento diário superior à média mensal: ", count)
