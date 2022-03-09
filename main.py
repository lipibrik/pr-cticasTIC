class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    def saludo(self):
        print("Me llamo %s" % (self.nombre)
        
class Perro(Animal):
    def __init__(self, nombre, raza):
        super().__init__(nombre)
        self.raza = raza
        print("Perro creado. Guau!")
    def ladrar(self):
        print("Guau guau")
    def queRazaSoy(self):
        print("Mi raza es %s" % (self.raza))
    def saludo(self):
        print("Guau guau, soy %s" % (self.nombre))
        
class Cerdo(Animal):
    def __init__(self, nombre, DO):
        super().__init__(nombre)
        self.DO = DO
        print("Cerdo creado. Oink oink")
    def gruñir(self):
        print("Oink oink")
class Granja:
    def __init__(self, perro, cerdo):
        self.perro = perro
        self.cerdo = cerdo
    def saludo(self):
        self.perro.saludo()
        self.cerdo.saludo()

perroGolfo = Perro("Golfo", "Perro de agua")
perroGolfo.saludo()
perroGolfo.ladrar()
perroGolfo.queRazaSoy()
cerdoBabe = Cerdo("Babe", "Jabugo")
cerdoBabe.saludo()
cerdoBabe.gruñir()


