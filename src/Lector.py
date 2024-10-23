import pandas as pd
from bsd import *
from Usuario import *
from utils import * 
from Bibliotecario import * 
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
    def prestar_libro(self):#Le permite al lector prestar un libro del catalogo
        titulo = input('Ingresa el titulo del libro: ').capitalize()
        libro_existe = buscar_dato_existente(titulo,'Titulo',catalogo)
        if libro_existe == True:
            print('Libro encontrado exitosamente')
            for i in catalogo:
                if titulo == i['Titulo']:
                    for j in lectores:
                        if j['Nombre'] == self.nombre_usuario:
                            j['Prestamos'].append(titulo)
                            mermar_libro(catalogo,titulo)
            