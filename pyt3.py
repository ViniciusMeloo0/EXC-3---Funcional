
#Funçao para o Fibonacci
def fibon(n):

    if n <= 1:
        return 1
    else:
        return fibon(n-1)+fibon(n-2)

#Funçao para o fatorial 
def fatorial(n):

    if n == 1:
        return n
    else:
        return n*fatorial(n-1)

#Leitura do arquivo
file = open('input.dat','r')   
dados = file.readlines()       

#Printa-se os dados para visualizaçao do arquivo txt
print(dados)

#Print da nova lista
lista = [numero.strip().split() for numero in dados]

with open('output.dat','w') as output:
    cont = 1
    for item in lista:
        x, y= item
        a = fibon(int(x))
        b = fatorial(int(y))
        output.write(f"Linha {cont} ///Fibonacci de {x} = {a} |Fatorial de {y} = {b}\n")
        cont+=1

