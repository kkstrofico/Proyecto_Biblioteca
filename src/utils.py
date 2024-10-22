import bsd
def cambiar_datos_usuario(opcion,usuario):#Funcion que permite modificar los datos de un usuario
    if opcion == 'A':
        for i in bsd.bibliotecarios:
            if i['Nombre'] == usuario:
                print(f'Usuario: {i}')
                nuevo_nombre = input('Ingresa el nuevo nombre del usuario: ')
                i['Nombre'] = nuevo_nombre
                print(f"Datos Actualizados: {i}")
                print(bsd.bibliotecarios)
    elif opcion == 'B':
        for i in bsd.bibliotecarios:
            if i['Nombre'] == usuario:
                print(f'Usuario: {i}')
                nueva_contrasena = input('Ingresa la nueva contraseña del usuario: ')
                i['Contraseña'] = nueva_contrasena
                print(f"Datos Actualizados: {i}")
                print(bsd.bibliotecarios)
def elimina_usuario(usuario_borrar,lista):#Funcion que elimina un usuario 
    for i in lista:
        if i['Nombre'] == usuario_borrar:
            lista.remove(i)
def buscar_dato_existente(dato,dato_buscar,lista):#Funcion para comprobar si un usuario existe
    for i in lista:
        if i[dato_buscar] == dato:
            print(i)
            return True
        else:
            return False
def volver_menu(menu):#Funcion que permite regresar al usuario al menu deseado
    menu
def mermar_libro(lista,libro_solicitado):
    for i in lista:
        if i['Titulo'] == libro_solicitado:
            i['Cantidad'] -= 1
def modificar_dato(lista,dato,tipo_dato,nuevo_dato):#Funcion que modifica un dato x de una lista x por otro dato x
    for i in lista:
        if dato == i[tipo_dato]:
            i[tipo_dato] = nuevo_dato