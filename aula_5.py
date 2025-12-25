# Manipulação de cadeias de texto

frase = "Curso em Video Python" # 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20 = Total 21 Começa em 0
print(frase[9]) # Vai retornar a letra v
print(frase[9:13]) # vai imprimir o que tem à partir do 9 até o 12; No  13 para.
print(frase[9:21]) # Vai imprimir do 9 até o 20, após o 21 para.
print(frase[9:21:2]) # Vai começar no 9 e vai até o 21, mas pula 2 e imprime pula 2 e imprime.
print(frase[:5]) # Vai imprimir do inicio até o caracter 4.
print(frase[15:]) # Vai imprimir do 15 até o final.
print(frase[9::3]) #Vai imprimir do 9 até o final pulando de três em três 


# Análisar str

print(len(frase)) # comprimento da frase: 21 nesse caso.
print(frase.count("o")) # Conta quantas vezes tem a letra digitada "o" nesse caso.
print(frase.count("o", 0, 13)) # Conta quantas vezes aparece o "o" de 0 até 12.
print(frase.find("deo")) # Pede pro python procurar algo dentro da str. Retorna a posição da onde começou encontrar.
print(frase.find("Android")) # Quando não encontra o que você pediu, o python retorna -1.

# Transformação

print(frase.replace("Python", "Android")) # Troca a palavra Python por Android na str.
print(frase.upper()) # Transforma a str em maiúscula.
print(frase.lower()) # Transforma a str em minúscula.
print(frase.capitalize()) # Transforma tudo em minúsculo e deixa apenas a primeira letra em Maiúscula.
print(frase.title()) # Transforma a inicial de cada palavra em Maiúscula.
print(frase.strip()) # remove todos os espaços que tiver no incio e no fim da palavra. Usado para evitar que pessoas cadastrem por exemplo "espaços desnecessários."
print(frase.rstrip()) # remove todos os espaços no final "direita".
print(frase.lstrip()) # remove todos os espaços no inicio "esquerda".


# Divisão

print(frase.split()) # "Dividie" cada espaço é retirado e cada palavra incia a contagem novamente.
print("-".join(frase.split())) # Junta cada palavra separada por espaço e pode ser usado no lugar de cada espaço um caracter. Nesse caso "-"





