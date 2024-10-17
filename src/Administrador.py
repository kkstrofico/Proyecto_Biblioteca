import bsd
from Usuario import *
from Lector import *
from Bibliotecario import *
class Administrador(Usuario):
    def registrar(self):#Sube los datos del Administrador a la bsd
        bsd.administradores.append({'Nombre':self.nombre_usuario,'Contraseña':self.contreseña})
    #Gestionar Usuarios
    def crear_usuarios(self):#Le permite al admistrador registrar bibliotecarios y lectores
        print(f'ELIGE UNA OPCION\n')
        opcion = input('A. Registrar Bibliotecario\nB. Registrar Lector\nDIGITA AQUI: ').upper()
        if opcion == 'A':
            print('\nIngresa los datos de Blibliotecario ')
            nombre = input('NOMBRE: ')
            contraseña = input('CONTRASEÑA: ')
            bibliotecario = Bibliotecatario(nombre,contraseña)
            bibliotecario.registrar()
        elif opcion == 'B':
            print('\nIngresa los datos del lector')
            nombre = input('NOMBRE: ')
            contraseña = input('CONTRASEÑA: ') 
            lector = Lector(nombre,contraseña)
            lector.regisrar()
    def eliminar_usuario():
        pass