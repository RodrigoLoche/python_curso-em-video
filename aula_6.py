# Condições # if, elif,  else,


#----------------------------------------------#

# tempo = int(input("Quantos anos tem seu carro? "))
# if tempo <=3:
#     print("Carro novo")
# else:
#     print("Carro velho")
# print("FIM")

# # Outra opção

# tempo = int(input("Quantos anos tem seu carro? "))
# print("Carro novo" if tempo <=3 else "Carro velho")
# print("Fim!")


#----------------------------------------------#


# nome = input("Qual é o seu nome? ")
# if nome == "Rodrigo":
#     print("Que nome lindo você tem!")
# print(f"Bom dia {nome}!") #Estrutura condicional simples.

# nome = input("Qual é o seu nome? ")
# if nome == "Rodrigo":
#     print("Que nome lindo você tem!")
# else: # Estrutura condicional composta.
#     print("Que nome comum você tem!") 
# print(f"Bom dia {nome}!")


#----------------------------------------------#

# n1 = float(input("Digite a primeira nota: "))
# n2 = float(input("Digite a segunda nota: "))
# m = (n1 + n2) / 2

# print(f"A sua média foi {m:.2f}")

# if m >= 6.0:
#     print("Sua média foi boa! PARABÉNS")
# else:
#     print("Sua média foi ruim! ESTUDE MAIS!")

#----------------------------------------------#

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
m = (n1 + n2) / 2

print(f"A sua média foi {m:.2f}")
print("PARABÉNS" if m >=6 else "ESTUDE MAIS!")


# Cores no terminal 
#"ANSI Python"

# Para usar algumas cores pode digitar o comando : \033[m
# \033[style;text;backgroundm exemplo: print("\033[0;33;44mHello World\033[m")



# print("\033[0;33;44mHello World\033[m") # se não fechar no final, o background vai preencher toda a linha.
# print("\033[0;33;44mHello World")

# print("\033[0;33;44mHello World\033[m") Cada valor dentro significa uma cor.
# Exemplo:
# Style: 0=none 
#        1=Bold
#        4=Underline
#        7=Negative
# 
# Text: 30=Branco
#       31=Vermelho
#       32=Verde
#       33=Amarelo
#       34=Azul
#       35=Roxo
#       36=azul claro
#       37=cinza
#
# Background: 40=Branco
#             41=Vermelho
#             42=Verde
#             43=Amarelo
#             44=Azul
#             45=Roxo
#             46=Azul Claro
#             47=Cinza


print("\033[0;30;41mTESTE\033[m")

print("\033[4;33;44mTESTE\033[m")

print("\033[1;35;43mTESTE\033[m")

print("\033[30;42mTESTE\033[m") # Se for manter o style padrão, não precisa digitar o 0.

print("\033[mTESTE\033[m") # Cor padrão.

print("\033[7;40mTESTE\033[m") # Fundo Branco com letra preta


nome = "Jubileu"

cores = {"limpa":"\033[m", # Fazer uma lista com cores pode facilitar.
         "azul": "\033[34m",
         "amarelolimpa": "\033[33m",
         "pretoebranco": "\033[0;30;40m"}

print(f"prazer em te conhecer {cores['azul']}{nome}{cores['pretoebranco']}!!!\033[m")
