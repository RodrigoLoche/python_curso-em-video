# # Estrutura de repetição

# # Laço com valores definidos.

# for c in range(1, 6): # contagem de 1 a 5. Zero é contado.
#     print("Oi") 
# print("FIM")


# for c in range(6, -1, -1): # contagem de 6 até 0 de 1 em 1. Se colocar, x, x, -2 ou -3 ou -4 etc... Pula de quantia em quantia.
#     print(c)
# print("FIM")

# for c in range(0, 7, 2): # Contagem comum, pulando de dois em dois.
#     print(c)
# print("FIM")


# # Exemplo usando input.

# n = int(input("Digite um número: "))
# for c in range(0, n+1):
#     print(c)
# print("FIM")


# # Exemplo

# i = int(input("Início: "))
# f = int(input("Fim: "))
# p = int(input("Passo: "))
# for c in range(i, f+p): #Começa no incio, vai até o fim e com o passo desejado.
#     print(c)
# print("FIM")


# # Exemplo
# for c in range(0, 10): # de 0 até 10, Permite o usuário digitar 10 vezes.
#     n = int(input("Digite um valor: "))
# print("FIM")

# exemplo de soma usando estrutura de repetição.
s = 0
for c in range(0,4):
    n = int(input("Digite um valor: "))
    s += n
print(f"A soma de todos os valores foi {s}")
