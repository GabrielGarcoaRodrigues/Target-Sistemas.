string = str(input('Informe a string: '))
inverted_string = ""

for i in range(len(string)-1, -1, -1):          #Utilizando o range para determinar o tamanho, passando o len(string)-1, -1, -1 para indicar onde vai começar o i, onde vai terminar e qual o passo
    inverted_string += string[i]                #Salvando na nova string ao contrário

print(inverted_string)
