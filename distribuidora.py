# 3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
# • O menor valor de faturamento ocorrido em um dia do mês;
# • O maior valor de faturamento ocorrido em um dia do mês;
# • Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

import sys                                                                  #Importando o sys para utilizar o valor maximo

lista =[
	{
		"dia": 1,
		"valor": 22174.1664
	},
	{
		"dia": 2,
		"valor": 24537.6698
	},
	{
		"dia": 3,
		"valor": 26139.6134
	},
	{
		"dia": 4,
		"valor": 0.0
	},
	{
		"dia": 5,
		"valor": 0.0
	},
	{
		"dia": 6,
		"valor": 26742.6612
	},
	{
		"dia": 7,
		"valor": 0.0
	},
	{
		"dia": 8,
		"valor": 42889.2258
	},
	{
		"dia": 9,
		"valor": 46251.174
	},
	{
		"dia": 10,
		"valor": 11191.4722
	},
	{
		"dia": 11,
		"valor": 0.0
	},
	{
		"dia": 12,
		"valor": 0.0
	},
	{
		"dia": 13,
		"valor": 3847.4823
	},
	{
		"dia": 14,
		"valor": 373.7838
	},
	{
		"dia": 15,
		"valor": 2659.7563
	},
	{
		"dia": 16,
		"valor": 48924.2448
	},
	{
		"dia": 17,
		"valor": 18419.2614
	},
	{
		"dia": 18,
		"valor": 0.0
	},
	{
		"dia": 19,
		"valor": 0.0
	},
	{
		"dia": 20,
		"valor": 35240.1826
	},
	{
		"dia": 21,
		"valor": 43829.1667
	},
	{
		"dia": 22,
		"valor": 18235.6852
	},
	{
		"dia": 23,
		"valor": 4355.0662
	},
	{
		"dia": 24,
		"valor": 13327.1025
	},
	{
		"dia": 25,
		"valor": 0.0
	},
	{
		"dia": 26,
		"valor": 0.0
	},
	{
		"dia": 27,
		"valor": 25681.8318
	},
	{
		"dia": 28,
		"valor": 1718.1221
	},
	{
		"dia": 29,
		"valor": 13220.495
	},
	{
		"dia": 30,
		"valor": 8414.61
	}
]

maior, media, count, dias_faturados = 0,0,0,0
menor = sys.maxsize


for valor in lista:                                                                         #Percorrendo a lista
    if valor['valor'] > maior:                                                              #Achando o maior valor
        maior = valor['valor']                                                              #Pegando esse valor
    
    elif valor['valor'] < menor and valor['valor'] != 0:                                    #Restringindo a busca para o menor valor e diferente de zero
        menor = valor['valor']                                                              #Pegando esse valor
    
    if valor['valor'] != 0:                                                                 #Achando os dias que teve faturamento
        dias_faturados += 1                                                                 #Incrementando a variavel
        media += valor['valor']                                                             #Somando os valores

     

for valor in lista:
    if valor['valor'] > (media/dias_faturados):                                             #Verificando se o faturamento é maior que a média
        count += 1  

print(f'O menor valor de faturamento ocorrido em um dia do mês: R${menor:.2f}')
print(f'O maior valor de faturamento ocorrido em um dia do mês: R${maior:.2f}')
print(f'Número de dias no mês em que o valor de faturamento diário foi superior à média mensal: {count} dias')
