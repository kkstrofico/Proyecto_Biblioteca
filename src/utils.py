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
def buscar_usuario_existente(dato,dato_buscar,lista):#Funcion para comprobar si un usuario existe
    for i in lista:
        if i[dato_buscar] == dato:
            return True
        else:
            return False

