import bsd as bsd
from Usuario import *
class Bibliotecatario(Usuario):
    def registrar(self):#Sube los datos del Biblioteacario a la bsd 
        bsd.bibliotecarios.append({'Nombre':self.nombre_usuario,'Contraseña':self.contreseña})
    #Gestionar prestamos
    def realizar_prestamo(self):#Se crea un prestamo y se le asigna a un lector
        print('\n\tPrestar libro\n')
        titulo_libro = input('Ingresa el titulo del libro: ')
        nombre_lector = input('Ingresa el nombre del prestador: ')
        for i in bsd.lectores:
            if i['Nombre'] == nombre_lector:
                i['Prestamos'] = [titulo_libro]
Bibliotecatario().realizar_prestamo()
print(bsd.lectores)