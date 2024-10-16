import bsd 
class Usuario:
    def __init__(self,nombre_usuario,contraseña):
        self.nombre_usuario = nombre_usuario
        self.contreseña = contraseña
class Administrador(Usuario):
    def registrar(self):#Sube los datos del Administrador a la bsd
        bsd.administradores.append({'Nombre':self.nombre_usuario,'Contraseña':self.contreseña})
class Bibliotecatario(Usuario):
    def registrar(self):#Sube los datos del Biblioteacario a la bsd 
        bsd.bibliotecarios.append({'Nombre':self.nombre_usuario,'Contraseña':self.contreseña})
class Lector(Usuario):
    def regisrar(self):#Sube los datos del Lector a la bsd
        bsd.lectores.append({'Nombre':self.nombre_usuario,'Contraseña':self.contreseña})