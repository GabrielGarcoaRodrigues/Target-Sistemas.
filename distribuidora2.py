# 4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:

# SP – R$67.836,43
# RJ – R$36.678,66
# MG – R$29.229,88
# ES – R$27.165,48
# Outros – R$19.849,53

faturamento = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

total = sum(faturamento.values())                   #Sum para somar todos os valores do meu dicionário

for estado, valor in faturamento.items():           #Percorrendo os itens
    percentual = (valor / total) * 100              #Dividindo o valor pelo total e multiplicando por 100 para tem o percentual
    print(f'{estado}: {percentual:.2f}%')

