import bsd 
from utils import * 
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
    def modificar_usuario(self):#Le permite al administrador modificar los datos de los usuarios 
        opcion = input('A.Modificar Bibliotecario\nB.Modificar Lector\nDigita aqui: ').upper()
        usuario = input('Ingresa el nombre del usuario a modificar: ')
        if opcion == 'A':#Modificar bibliotecarios
            while buscar_usuario_existente(usuario,'Nombre',bsd.bibliotecarios) == False:
                print('Error el usuario no existe')
                usuario = input('NOTA: Ingresa exit para volver al menu\nIngresa el nombre del usuario a modificar: ').upper()
                if usuario == 'EXIT':
                    Administrador().modificar_usuario()
                   
            opcion = input('A.Cambiar Nombre\nB.Cambiar Contraseña\nDigita aqui: ').upper()
            cambiar_datos_usuario(opcion,usuario)
        elif opcion == 'B':#Modificar Lecoteres
            while buscar_usuario_existente(usuario,'Nombre',bsd.bibliotecarios) == False:
                print('Error el usuario no existe')
                usuario = input('NOTA: Ingresa exit para volver al menu\nIngresa el nombre del usuario a modificar: ').upper()
            opcion = input('A.Cambiar Nombre\nB.Cambiar Contraseña\nDigita aqui: ').upper()
            cambiar_datos_usuario(opcion,usuario)
    def eliminar_usuario(self):#Permite eliminar un usuario
        tipo_usuario = input('Selecciona\nA.Eliminar Bibliotecario\nB.Eliminar Lector')
        usuario = input('\nIngresa el nombre del usuario que deseas eliminar: ')
        lista = []
        if tipo_usuario == 'A':
            lista = bsd.bibliotecarios
        elif tipo_usuario == 'B':
            lista = bsd.lectores
        while buscar_usuario_existente(usuario,'Nombre',lista) == False:
                print('Error el usuario no existe')
                usuario = input('NOTA: Ingresa exit para volver al menu\nIngresa el nombre del usuario a eliminar: ').upper()
        elimina_usuario(usuario,lista)
        
        
Administrador().eliminar_usuario()
print(bsd.bibliotecarios)
