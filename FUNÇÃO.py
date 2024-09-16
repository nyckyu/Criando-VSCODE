x = int
y = int

def soma (x,y):
    return x + y

def subtrai (x,y):
    return x - y

def divide (x,y):
    return x/y

def multiplica (x,y):
    return x*y

operação = input("digite se você deseja somar, subtrair, dividir ou multiplicar: ")

operação.lower

sm = "somar" in operação
sb = "subtrair" in operação
dv = "dividir" in operação
mult = "multiplicar" in operação

    
if sm == True:
    x = int(input("digite um valor: "))
    y = int(input ("digite o valor que quer somar com o valor anterior: "))
    resultado_soma = soma(x,y)
    print(resultado_soma)

elif sb == True:
    x = int(input("digite um valor:"))
    y = int(input("digite o valor que quer subtrarir com o valor anterior"))
    resultado_subtrai = subtrai(x,y)
    print(resultado_subtrai)

elif dv == True:
    x = int(input("digite um valor:"))
    y = int(input("digite o valor que quer dividir com o valor anterior"))
    resultado_divide = divide(x,y)
    print(resultado_divide)

else:
    x = int(input("digite um valor:"))
    y = int(input("digite o valor que quer multiplicar com o valor anterior"))
    resultado_multiplica = multiplica(x,y)
    print(resultado_multiplica)

