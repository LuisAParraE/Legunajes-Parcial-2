class heap:

    def __init__(self, value,leafA,leafB) -> None:
        self.value = value
        self.leafA = leafA
        self.leafB = leafB


def esMinHeapBalanceado(heap):
    
    hojas = leafHeight(heap, 0)

    if(max(hojas) - min(hojas) > 1):
        print("Arbol No Balanceado")
    else:
        print("Arbol Balanceado")

def leafHeight(heap,n):

    leafheight = []
    if(heap.leafA == None and heap.leafB == None):
    
        return (leafheight + [n])
    
    if(heap.leafA != None):
        leafheight = leafheight + leafHeight(heap.leafA,n+1)

    if(heap.leafB != None):
        leafheight = leafheight + leafHeight(heap.leafB,n+1)

    return leafheight


def test():

    prueba = heap(2,
                heap(4,
                    heap(9,None,None),
                    heap(7,None,None)),
                heap(8,
                    heap(10,None,None),
                    heap(9,
                        heap(12,
                            heap(15, None, None), 
                            None),
                        None)))

    prueba1 = heap(2,
                heap(4,
                    heap(9,None,None),
                    heap(7,None,None)),
                heap(8,
                    heap(10,None,None),
                    heap(9,None,None))
                    )

    #esMinHeapBalanceado(prueba1)


test()