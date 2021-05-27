print("Hello, World!")
print("Qual o seu nome?")
nome = input()
print("Prazer em conhecer você, " + nome + '!')
print("\nVocê sabia que seu nome contém " + str(len(nome)) + " letras?") #para fazer a concatenação, convertemos o nome para string.
print("\nQual a sua idade?")
idade = input()
print("Você terá " + str(int(idade) + 1) + " anos no ano que vem!") #idade para int e somou + 1. O resultado foi convertido para string.