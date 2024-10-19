#PEGUE UM NUMERO INTEIRO E FAÇA A TABUADA DELE

valor = int(input("digite o valor"))

for t in range(11):
    resultado = valor * t
    print(valor, "x", t, "=", resultado)