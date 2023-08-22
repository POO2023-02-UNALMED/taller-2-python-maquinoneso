class Auto:
    cantidadCreados=10
    def __init__(self,modelo,precio,asientos,marca,motor,registro):
        self.modelo = modelo
        self.precio = precio
        self.marca = marca
        self.registro = registro
        self.asientos = asientos
        self.motor = motor

    def cantidadAsientos(self):
        asientos = self.asientos
        cantidadAsientos=0
        for i in asientos:
            if i != None:
                cantidadAsientos+=1
        print(cantidadAsientos)
    
    def verificarIntegridad(self):
        value=self.registro
        for i in self.asientos:
            if i != None and i.registro != self.registro or i!=None and i.registro != self.motor.registro:
                print("Las piezas no son originales")
                value=i.registro
                break
            else:
                None
        if self.registro == value and value == self.motor.registro:
            print("Auto original")
            
class Asiento:
    def __init__(self,color,precio,registro):
        self.color = color
        self.registro = registro
        self.precio = precio
    
    def cambiarColor(self, color):
        if color == 'rojo' or color == 'verde' or color == 'amarillo' or color == 'negro' or color == 'blanco':
            self.color = color       

class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo 
        self.registro = registro

    def cambiarRegistro(self, newRegistro):
        self.registro=newRegistro
    
    def asignarTipo(self, toTipe):
        if toTipe == 'gasolina' or toTipe == 'electrico':
            self.tipo = toTipe

      
