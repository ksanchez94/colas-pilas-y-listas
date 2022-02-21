class Cola:
    def __init__(self, tamano):
        self.cola = []
        self.tope = 0
        self.size = tamano

    def push(self,tamaño):
        if self.size > self.tope:
            for x in range (tamaño):
                dato = input('Ingrese un dato a la cola: ')
                self.cola.append(dato)
                self.tope += 1
        else:
            print('Cola Llena\n')

    def pop(self):
        if len(self.cola) != 0:
            self.cola.pop(0)
            self.tope -= 1
            print(f'Mostrando cola nueva: {self.cola}\n')
        else:
            print('Cola vacia\n')

    def longitud(self):
        print(f'La longitud de la Cola es: {len(self.cola)}\n')

    def show(self):
        if len(self.cola) != 0:
            print(self.cola)
        else:
            print('Cola vacia\n')

    def buscar(self):
        if len(self.cola) != 0:
            pos = input('Ingrese el elemento para retornar una posicion: ')
            if pos in self.cola:
                print(f'Posicion: {self.cola.index(pos)}')
            else:
                print(f'Imprimiendo Elmento de la posicion -1: {self.cola[-1]}\n')
        else:
            print('Cola vacia\n')