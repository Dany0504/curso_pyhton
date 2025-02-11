




def carga_archivos_texto(archivo:str)-> list:
    ''' 
    Carga un archivo de un texto y develve una lista con las oraciones del archivo
    '''
    with open(archivo, 'r') as file:
        oraciones = file.readlines()
    return oraciones

if __name__ == '__main__':
    lista = carga_archivos_texto('./plantillas/plantilla-0.txt')
    for elemento in lista:
        print(elemento)
