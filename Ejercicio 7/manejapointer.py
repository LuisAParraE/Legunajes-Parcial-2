class pointer:

    def __init__(self, name, direccion, key) -> None:
        self.name = name
        self.direccion = direccion
        self.key = key

class elemento:

    def __init__(self, value, key) -> None:
        self.value = value
        self.key = key


def main():

    apuntadores = []
    elementos = []
    print("SIMULADOR DE APUNTADORES USANDO EL METODO DE LOCKS AND KEYS:")
    while True:

        entrada = input("Indique Instrucción: ")

        if entrada != "":
            
            instruccion = entrada.split()

            if instruccion[0] == "RESERVAR":
                    
                if search_name_list(instruccion[1],apuntadores):

                    pos_elemento = len(elementos)
                    pos_pointer = get_pointer(instruccion[1],apuntadores)

                    elementos.append(elemento(instruccion[2],str(pos_elemento)+instruccion[2]))
                    apuntadores[pos_pointer].direccion = pos_elemento
                    apuntadores[pos_pointer].key = elementos[pos_elemento].key

                    print(f"Se reservo '{apuntadores[pos_pointer].name}' con valor '{instruccion[2]}'")

                else:

                    pos_elemento = len(elementos)
                    pos_pointer = len(apuntadores)

                    elementos.append(elemento(instruccion[2],str(pos_elemento)+instruccion[2]))
                    apuntadores.append(pointer(instruccion[1], pos_elemento, elementos[pos_elemento].key))

                    print(f"Se reservo '{apuntadores[pos_pointer].name}' con valor '{instruccion[2]}'")

            elif instruccion[0] == "ASIGNAR":

                if not search_name_list(instruccion[2],apuntadores):
                    print(f"Error: El Apuntador {instruccion[2]} no esta definido.")
                else:
                    
                    if not search_name_list(instruccion[1],apuntadores):
                        apuntadores.append(pointer(instruccion[1], None, None))

                    pos_pointer = get_pointer(instruccion[1],apuntadores)
                    pos_pointer2 = get_pointer(instruccion[2],apuntadores)

                    apuntadores[ pos_pointer ].direccion = apuntadores[pos_pointer2].direccion
                    apuntadores[ pos_pointer ].key = apuntadores[pos_pointer2].key

                    print(f"Se asigno '{apuntadores[pos_pointer2].name}' a '{apuntadores[ pos_pointer ].name}'")

            elif instruccion[0] == "LIBERAR":

                if not search_name_list(instruccion[1],apuntadores):
                   print(f"Error: El Apuntador {instruccion[1]} no esta definido.")
                else:
                    pos_pointer = get_pointer(instruccion[1],apuntadores)
                    pos_elemento = apuntadores[pos_pointer].direccion
                    elementos[pos_elemento].key = None

                    print(f"Se liberó {apuntadores[pos_pointer].name}")

            elif instruccion[0] == "IMPRIMIR":

                if not search_name_list(instruccion[1],apuntadores):
                    print(f"Error: El Apuntador {instruccion[1]} no esta definido.")
                else:
                    pos_pointer = get_pointer(instruccion[1], apuntadores)
                    pos_elemento = apuntadores[pos_pointer].direccion
                    if(elementos[pos_elemento].key == None) or (elementos[pos_elemento].key != apuntadores[pos_pointer].key):
                        print(f"Error: El Apuntador {apuntadores[pos_pointer].name} no apunta a un valor válido.")
                    else:
                        print(elementos[pos_elemento].value)

            elif instruccion[0] == "SALIR":
                break
            else:
                print("Instrucción No valida")


def search_name_list(name, list):

    for element in list:
        if element.name == name:
            return True

    return False

def get_pointer(name, list_pointers):
    
    i = 0

    while i< len(list_pointers):
        if(name == list_pointers[i].name):
            return i
        i = i +1

    return None


main()