
class church:
    base = 0

    def __init__(self, n) -> None:
        if n == 0:
            self.value = self.base
        else:
            self.value = self.sucesor(n-1)

    def sucesor(self,n): 
        if n == self.base:
            return self.base + 1
        else:
            return self.sucesor(n-1) + self.sucesor(0)

    def __add__(self, other):
        suma = church( other.value + self.value)
        return suma

    def __mul__(self, other):
        mult = church( other.value * self.value)
        return mult
     
def main():
    print("Indique 2 numeros enteros mayores o iguales a 0")

    numero_1 = church(int(input("numero 1: ")))
    numero_2 = church(int(input("numero 2: ")))

    print(numero_1.value)
    print(numero_2.value)
    print((numero_1+numero_2).value)
    print((numero_1*numero_2).value)

if __name__ == '__main__':
    main()

