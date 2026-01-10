#Estrutura de repetição While

## Comparando for e While.
## Estrutura for

# for c in range(1, 10):
#     print(c)
# print("FIM")

# Estrutura while

c = 1
while c < 10:
    print(c)
    # c = c + 1 Pode usar assim também.
    c += 1
print("FIM")

# Quando não sabe-se o limite, não tem como usar o "for", apenas o while.

n = 1
while n != 0: # Só vai parar se digitar o número 0, ou seja, você coloca um comando para parar quando atingir a quantidade desejada..
    n = int(input("Digite um valor: ")) 
print("FIM")



# Opção de escolher quando parar.

r = "S"
while r == "S":
    n = n = int(input("Digite um valor: "))
    r = input("Quer continuar? [S/N] ").upper()
print("FIM")


# Exemplo: Se um programa precisa ler a idade de 10 pessoas, nesse caso utilizar o "for" seria melhor, já está definido a quantidade.
# Mas se não souber quantas pessoas, dai não tem como usar o "for". Nesse caso utiliza o "while".

# Para fazer uma análise:

n = 1
par = impar = 0
while n != 0: 
    n = int(input("Digite um valor: ")) 
    if n != 0: # Faz com que não contabilize o "0"
        if n % 2 == 0:
            #par = par + 1 ## O uso do estilo de baixo é a mesma coisa que esse.
            par += 1
        else:
            impar += 1
print(f"Você digitou {par} números pares e {impar} números ímpares.")
        

