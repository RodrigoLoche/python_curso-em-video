# Operadores aritméticos

# + Adição           ** Potência
# - Subtração        // Divisão inteira
# * Multiplicação    %  Resto da divisão
# / Divisão         #

# pode utilizar o comando (pow) para elevar um número.


print(5 + 2)
print(5 - 2)
print(5 * 2)
print(5 / 2)
print(5 ** 2)
print(pow(5,2))
print(5 // 2)
print(5 % 2)
print(pow(5,3))

# Calcular raiz quadrada = x ** (1/2)
# Calcular raiz cúbica = x ** (1/3)

# Odem de Precedência que o python resolve.

# primeiro = ()
# segundo = **
# Terceiro = *, /, //, %
# Quarto = +, -

print(5 + 3 * 2)
print(3 * 5 + 4 ** 2)
print(3 * (5 + 4) ** 2)

print(25 ** (1/2))


# Multiplicar str
print("!" * 5)

# centralizar algo ^ 
# centralizar algo e colocar algo antes =^
name = input("Name: ")
print(f"{name:^20}")
print(f"{name:=^20}")


# Para não quebrar a linha de um print para o outro.
# Adiciona o (,end="") depois das " antes de fechar o parênteses.

name = input("Name: ")
print(f"{name:^20}", end=" ")
print(f"{name:=^20}")

# Para quebrar a linha use \n
print("Olhe! UM MELÃO\n AZUL!")
