import pandas as pd
from bsd import *
from Usuario import *
class Lector(Usuario):
    def regisrar(self):#Sube los datos del Lector a la bsd
        lectores.append({'Nombre':self.nombre_usuario,'Contraseña':self.contreseña})
    def consultar_catalogo(self):#Permite consultar el catalogo de libros
        df = pd.DataFrame(catalogo)
        print(df)
    def consultar_prestamos(self):#Permite revisar el historial de los libros prestados
        for i in lectores:
            if i['Nombre'] == self.nombre_usuario:
                print(i['Prestamos'])
            