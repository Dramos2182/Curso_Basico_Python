# Una clase es una plantilla
# Una clase posee un nombre
# Una clase posee atributos y metodos
# Un objeto es una instancia
class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad


# Un constructor es un metodo para crear un objeto
persona1 = Persona('David', 'Ramos', 19)
print(f'Objeto persona 1: {persona1.nombre} {persona1.apellido} {persona1.edad}')

persona2 = Persona('Jonatan', 'Ramos', 14)
print(f'Objeto persona 2: {persona2.nombre} {persona2.apellido} {persona2.edad}')
