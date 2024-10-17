import bsd as bsd
from Usuario import *
class Bibliotecatario(Usuario):
    def registrar(self):#Sube los datos del Biblioteacario a la bsd 
        bsd.bibliotecarios.append({'Nombre':self.nombre_usuario,'Contraseña':self.contreseña})
    def gestionar_prestamo(self):#Le permite gestionar los libros prestados
        pass
    def gestionar_devolucion(self):#Le permite gestionar los libros devueltos
        pass