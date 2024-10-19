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
    def retirar_prestamo(self):#Se encarga de quitar un libro de los prestamos de un lector
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
        titulo = input('TITULO: ').capitalize()
        autor = input('AUTOR: ')
        isbm = input('ISBM: ')
        editorial = input('EDITORIAL: ')
        categoria = input('CATEGORIA: ')
        año_de_publicacion = input('AÑO DE PUBLICACION: ')
        categoria = input('CATEGORIA: ')
        cantidad = input('CANTIDAD: ')
        libro = {'Titulo':titulo,
                 'Autor': autor,
                 'Isbm': isbm,
                 'Editorial':editorial,
                 'Categoria':categoria,
                 'Año Publicacion':año_de_publicacion,
                 'Cantidad':cantidad
                 } 
        catalogo.append(libro)
    def editar_libro(self):#Permite modificar los datos de un libro en el catalogo
        print('\n\tIngresa los datos del libro para encontrar el libro que deseas modificar\n')
        titulo = input('TITULO: ').capitalize()
        buscar_libro = buscar_dato_existente(titulo,'Titulo',catalogo)
        if buscar_libro == True:#Editar libro
            print('Libro Encontrado Exitosamente.')
            dato_modificar = input('Que deseas modificar del libro:\n\nTITULO\nAUTOR\nISBM\nEDITORIAL\nCATEGORIA\nAÑO PUBLICACION\nCANTIDAD\nDIGITA AQUI: ').capitalize()
            nuevo_dato = input(f'Ingresa el\la nuev@ {dato_modificar}:  ')
            modificar_dato(catalogo,titulo,dato_modificar,nuevo_dato)#Modifica un dato de una lista
        elif buscar_libro == False:
            print('No se encontro el libro')
            volver_menu(Bibliotecatario(self.nombre_usuario,self.contreseña).editar_libro())
        else:
            print('A ocurrido un error al buscar el libro')
            volver_menu(Bibliotecatario(self.nombre_usuario,self.contreseña).editar_libro())
    def eliminar_libro(self):#Permite eliminar un libro del catalogo
        print('\n\tIngresa los datos del libro para encontrar el libro que deseas eliminar\n')
        titulo = input('TITULO: ').capitalize()
        buscar_libro = buscar_dato_existente(titulo,'Titulo',catalogo)
        if buscar_libro == True:#Eliminar libro
            print('Libro encontrado exitosamente')
            opcion_eliminar = input('\nEstas seguro de eliminar el libro si/no: ').capitalize()
            if opcion_eliminar == 'Si':
                for i in catalogo:
                    if i['Titulo'] == titulo:
                        catalogo.remove(i)
            elif opcion_eliminar == 'No':
                print('Se volvera al menu')
                volver_menu(Bibliotecatario(self.nombre_usuario,self.contreseña).eliminar_libro())
        elif buscar_libro == False:
            print('No se encontro el libro')
            volver_menu(Bibliotecatario(self.nombre_usuario,self.contreseña).editar_libro())
Bibliotecatario().eliminar_libro()
print(catalogo)