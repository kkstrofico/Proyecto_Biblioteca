import bsd as bsd
from Usuario import *
class Lector(Usuario):
    def regisrar(self):#Sube los datos del Lector a la bsd
        bsd.lectores.append({'Nombre':self.nombre_usuario,'Contraseña':self.contreseña})
    def consultar_catalogo(self):#Permite consultar el catalogo de libros
        pass