class Stack:                
    def __init__(self,tamanio):
        self.pila=[]
        self.tope=0
        self.size=tamanio
    
    def push(self,tamaño):
        if self.tope < self.size:
            for x in range (tamaño):
                dato = input("Ingrese un dato a la pila: ")
                self.pila += [dato]
                self.tope += 1
        else:
            print("La Pila se encuentra Llena")
   
    def pop(self):
        if len(self.pila) != 0:
            self.pila.pop()
            self.tope -= 1
            print(f'Mostrando pila nueva: {self.pila}\n')
        else:
            print('Pila vacia\n')
            
    def longitud(self):
        print(f'La longitud de la pila es: {len(self.pila)}\n')
        
    def show(self):
        if len(self.pila) != 0:
           print(f'Mostrando pila: {self.pila}\n')
        else:
            print('Pila vacia\n')    
    
    def buscar(self):
        if len(self.pila) != 0:
            pos = input('Ingrese el elemento para retornar una posicion: ')
            if pos in self.pila:
                print(f'Posicion: {self.pila.index(pos)}')
            else:
                print(f'Imprimiendo Elemento de la posicion -1: {self.pila[-1]}\n')
        else:
            print('Pila vacia\n')