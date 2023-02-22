# Programa para verificar cual de los dos numeros es entero


# input 
x = int (input("Digite el valor de x: "))
y = int (input("digite el valor de y: "))

# processing
if x > y:
    mayor = x
else: 
    mayor = y
    # output 
print("El mayor entre " + str(x) +  " y "  + str(y) +  " es " +  str(mayor))
if x == y:
    #output
    print(" Los numeros son iguales...")
