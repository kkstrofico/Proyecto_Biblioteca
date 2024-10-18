from bsd import *
from Usuario import *
from utils import *
class Bibliotecatario(Usuario):
    def registrar(self):#Sube los datos del Biblioteacario a la bsd 
        bibliotecarios.append({'Nombre':self.nombre_usuario,'Contraseña':self.contreseña})
    #Gestionar prestamos
    def realizar_prestamo(self):#Se crea un prestamo y se le asigna a un lector
        print('\n\tPrestar libro\n')
        titulo_libro = input('Ingresa el titulo del libro: ')
        nombre_lector = input('Ingresa el nombre del prestador: ')
        for i in lectores:
            if i['Nombre'] == nombre_lector:
                i['Prestamos'] = [titulo_libro]
    #Devoluciones
    def retirar_prestamo(self):#Se encarga de quitar el libro de los prestamos de un lector
        print('\n\tDevolucion\n')
        nombre_lector = input('Ingresa el nombre del prestador: ')
        while buscar_dato_existente(nombre_lector,'Nombre',lectores) == False:
            print('\n\tUsuario no encontrado')
            nombre_lector = input('Ingresa el nombre del prestador: ')
        titulo_libro = input('Ingresa el titulo del libro: ')
        contador = 0
        for i in lectores:
            if i['Nombre'] == nombre_lector:
                if titulo_libro in i['Prestamos']:
                    contador += 1
                    i['Prestamos'].remove(titulo_libro)
        if contador == 0:
            print('\n\tNo se encontro el libro\nAsegurate de ingresarlo correctamente')
            Bibliotecatario(self.nombre_usuario,self.nombre_usuario).retirar_prestamo()
    #Gestionar catalogo de libros
    def añadir_libro(self):#Permite agregar un libro al catalogo de libros
        print('\n\tAgregar libro al catalogo de libros\n')
        titulo = input('TITULO: ')
        autor = input('AUTOR: ')
        isbm = input('ISBM: ')
        editorial = input('EDITORIAL: ')
        categoria = input('CATEGORIA: ')
        año_de_publicacion = input('AÑO DE PUBLICACION: ')
        categoria = input('CATEGORIA: ')
        cantidad = input('CANTIDAD: ')
        libro = {'Titulo':titulo,
                 'Autor': autor,
                 'ISBM': isbm,
                 'Editorial':editorial,
                 'Categoria':categoria,
                 'Año Publicacion':año_de_publicacion,
                 'Cantidad':cantidad
                 } 
        catalogo.append(libro)