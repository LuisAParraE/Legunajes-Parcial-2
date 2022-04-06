X = 0
Y = 8
Z = 3
alpha = ((X + Y ) % 5) + 3
beta = ((Y + Z) % 5) + 3

def fibonacci(n):

    if(n >= 0 and (n < alpha * beta)):
        return n
    elif (n >= alpha * beta):
        
        return (fibonacci(n-beta) +fibonacci(n-(beta*2)) +fibonacci(n-(beta*3)) +fibonacci(n-(beta*4)) +fibonacci(n-(beta*5)) +fibonacci(n-(beta*6))) 

def main():
    
    entrada = int(input("Introduzca el numero a calcular: "))
    resultado = fibonacci(entrada)
    print(f"El resultado es: {resultado}")

main()