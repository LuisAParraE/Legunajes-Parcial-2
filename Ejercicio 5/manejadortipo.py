class tipo:

    def __init__(self, name, size, alineacion) -> None:
        self.name = name
        self.size = size
        self.alineacion = alineacion

class estructura:

    def __init__(self, name, tipos, size) -> None:
        self.name = name
        self.tipos = tipos  #tipos es una lista
        self.size = size

class alias:

    def __init__(self, name, tipo, size) -> None:
        self.name = name
        self.tipo = tipo
        self.size = size

posicion = 0

def main():


    tipos = []
    structs = []
    aliases = []

    while True:

        entrada = input("Indique Instrucción: ")

        if entrada != "":
            
            instruccion = entrada.split()

            if instruccion[0] == "ATOMICO":
                    
                if search_name_list(instruccion[1],tipos):
                   print(f"Error: El Tipo de dato {instruccion[1]} ya esta creado.")
                else:

                    try:
                        size = int(instruccion[2])
                        alineacion = int(instruccion[3])

                        if (type(size) is int) and (type(alineacion) is int):
                            if size >0 and alineacion > 0:
                                tipos.append(tipo(instruccion[1],int(instruccion[2]),int(instruccion[3])))
                            else:
                                print("No se permiten tamano o alineacion negativos o iguales a 0")
                    except:
                        print("Tipo de dato incorrecto suministrado en la entrada")

            elif instruccion[0] == "STRUCT":

                if search_name_list(instruccion[1],structs):
                   print(f"Error: El Struct {instruccion[1]} ya esta creado.")
                else:
                    aux = True
                    for element in instruccion[2:]:
                        aux = search_name_list(element,tipos) or search_name_list(element,aliases) or search_name_list(element,structs)
                        if not aux:
                            break
                    
                    if not aux:
                        print("Error: Alguno de los tipos indicados no esta definido")
                    else: 
                        size = 0 
                        for element in instruccion[2:]:
                            size = size + getsize(element,tipos,structs,aliases)

                        structs.append(estructura(instruccion[1],instruccion[2:],size))
            
            elif instruccion[0] == "ARREGLO":

                if search_name_list(instruccion[1],aliases):
                   print(f"Error: El alias {instruccion[1]} ya esta creado.")
                else:

                    aux = search_name_list(instruccion[2],tipos) or search_name_list(instruccion[2],aliases) or search_name_list(instruccion[2],structs)
                    
                    if not aux:
                        print(f"Error: El tipo {instruccion[2]} indicado no esta definido")
                    else:  
                        
                        try: 
                            size = int(instruccion[3])

                            if (type(size) is int):
                                if size >0 :
                                    aliases.append(alias(instruccion[1],instruccion[2],size))
                                else:
                                    print("No se permiten tamano negativos o iguales a 0")
                        except:
                            print("Tipo de dato incorrecto suministrado en la entrada") 
                            

            elif instruccion[0] == "DESCRIBIR":

                if (not search_name_list(instruccion[1],tipos)) and (not search_name_list(instruccion[1],structs)) and (not search_name_list(instruccion[1],aliases)):
                    print(f"Error: El tipo {instruccion[1]} no esta definidos.")
                else:
                    show_size(instruccion[1],tipos,structs,aliases)
                
                global posicion
                print(posicion)
            elif instruccion[0] == "SALIR":
                break
            else:
                print("Instrucción No valida")


def search_name_list(name, list):

    for element in list:
        if element.name == name:
            return True

    return False

def show_size(name,tipos,structs,aliases):
    
    global posicion
    posicion = 0
    memory = show_size_unpacked(get_tipo(name,tipos,structs,aliases),tipos,structs,aliases)
    print(memory)
    junk = 0
    for element in memory:
        if element == 0:
            junk = junk +1

    size = posicion
    print("<><>< REGISTROS Y ARREGLOS SIN EMPAQUETAR><><>")
    print(f"Tipo dato: {name} ,ocupado: {size} ,desperdiciado: {junk}")

    size = getsize(name,tipos,structs,aliases)
    junk = 0
    print("<><>< REGISTROS Y ARREGLOS EMPAQUETADOS><><>")
    print(f"Tipo dato: {name} ,ocupado: {size} ,desperdiciado: {junk}")



def getsize(name,tipos, structs, aliases):

    for element in tipos:
        if element.name == name:
            return element.size

    for element in structs:
        if element.name == name:
            return element.size

    for element in aliases:
        if element.name == name:
            return (element.size * getsize(element.tipo,tipos, structs, aliases))

def show_size_unpacked(name,tipos,structs,aliases):

    global posicion
    memory = []
    if search_name_list(name.name, tipos):
        
        if(posicion % name.alineacion == 0):
            i = 1
            '''
            print("Se quiere insertar un tipo:" + name.name)
            print(f"Tiene un tamano de : {name.size} y una alineacion de: {name.alineacion}")
            print("No hay offset" )
            print(f"Posicion actual de la memoria:{posicion}")
            '''
            while i <= name.size :
                memory = memory + [1]
                posicion = posicion +1
                i = i+1
        else:
            offset = name.alineacion -(posicion % name.alineacion)
            i = 1
            '''
            print("Se quiere insertar un tipo:" + name.name)
            print(f"Tiene un tamano de : {name.size} y una alineacion de: {name.alineacion}")
            print(f"Hay un offset de: {offset}")
            print(f"Posicion actual de la memoria:{posicion}")
            '''
            while i <= offset :
                memory = memory + [0]
                posicion = posicion +1
                i = i+1

            if(posicion % name.alineacion == 0):
                i = 1
                while i <= name.size :
                    memory = memory + [1]
                    posicion = posicion +1
                    i = i+1

        return memory

    elif(search_name_list(name.name, structs)):

        for element in name.tipos:
            if search_name_list(element, tipos) :
                memory = memory + show_size_unpacked(get_tipo(element,tipos,structs,aliases),tipos,structs,aliases)
            elif search_name_list(element, structs) :
                memory = memory + show_size_unpacked(get_tipo(element,tipos,structs,aliases),tipos,structs,aliases)
            elif search_name_list(element, aliases) :
                memory = memory + show_size_unpacked(get_tipo(element,tipos,structs,aliases),tipos,structs,aliases)

        return memory

    elif(search_name_list(name.name, aliases)):
        
        i = 1
        while i <= name.size:
            if search_name_list(name.tipo, tipos) :
                memory = memory + show_size_unpacked(get_tipo(name.tipo,tipos,structs,aliases),tipos,structs,aliases)
            elif search_name_list(name.tipo, structs) :
                memory = memory + show_size_unpacked(get_tipo(name.tipo,tipos,structs,aliases),tipos,structs,aliases)
            elif search_name_list(name.tipo, aliases) :
                memory = memory + show_size_unpacked(get_tipo(name.tipo,tipos,structs,aliases),tipos,structs,aliases)
            i = i+1

        return memory


def get_tipo(name,tipos,structs,aliases):

    for element in tipos:
        if element.name == name:
            return element

    for element in structs:
        if element.name == name:
            return element

    for element in aliases:
        if element.name == name:
            return element



main()