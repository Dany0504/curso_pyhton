import random
'''
tablero.py: dibuje el tablero del juego de el gato
'''
def dibuja_tablero(simbolos:dict):
    '''
    Dibuja el tablero de juego del gato
    '''
    print(f'''
    {simbolos['1']} | {simbolos['2']} | {simbolos['3']}
    ---------
    {simbolos['4']} | {simbolos['5']} | {simbolos['6']}
    ---------
    {simbolos['7']} | {simbolos['8']} | {simbolos['9']}
''')

lista_combinaciones = [
        ['1','2','3'],
        ['4','5','6'],
        ['7','8','9'],
        ['1','4','7'],
        ['2','5','8'],
        ['3','6','9'],
    ]

def ia(simbolos:dict):
    ''' Juega la Mquina '''
    ocupado = True
    while ocupado == True:
        x = random.choice(list(simbolos.keys()))
        if simbolos[x] not in ['X','O']:
            simbolos[x] = 'O'
            ocupado = False

def checa_winner(simbolos:dict, combinaciones:list):
    '''Checa si hay un ganador'''
    for c in combinaciones:
        if simbolos[c[0]]:
            return None

def usuario(simbolos:dict):
    '''Juega el usuario'''
    ocupado = True
    while ocupado is True:
        x = input('Ingresa el número de la casilla: ')
        if x in numeros:
            if simbolos [x] not in ['X','0']:
                simbolos [x] = 'X' 
                ocupado = False 
            else:
                print('Casilla ocupada')
        else:
            print('numero equivocado')

def juego(simbolos:dict):
    movimientos = 0
    en_juego = True
    while en_juego:
        usuario(simbolos)
        dibuja_tablero(simbolos)
        movimientos += 1
        gana = checa_winner(simbolos, lista_combinaciones)
        if gana is not None:
            en_juego = False
            continue
        if movimientos >= 9:
            en_juego = False
            continue
        ia(simbolos)
        dibuja_tablero(simbolos)
        movimientos += 1
        gana = checa_winner(simbolos, lista_combinaciones)
        if gana is not None:
            en_juego = False
            continue
        if movimientos >= 9:
            en_juego = False
            continue
    return gana

def main():
    ''' 
    Funcion Principal
    '''
    numeros = [str(i) for i in range(1, 10)]
    dsimbolos = {x:x for x in numeros}
    g = juego(dsimbolos)
    if g is not None:
        print(f'El ganador')
    else:
        print('empate')

if __name__ == '__main__':
    numeros = [str(i) for i in range(1, 10)]
    dsimbolos = {x:x for x in numeros}
    g = juego(dsimbolos)
    if g is not None:
        print(f'El ganador')
    else:
        print('empate')
    ##dibuja_tablero(dsimbolos)
    ##ia(dsimbolos)
    #x = random.choice(numeros)5
    #numeros.remove(x)
    #dsimbolos[x] = 'X'
    #dibuja_tablero(dsimbolos)
    #usuario(dsimbolos)
    #dibuja_tablero(dsimbolos)
    #o = random.choice(numeros)
    #numeros.remove(o)
    #simbolos[o] = 'O'
    #dibuja_tablero(dsimbolos)
    #print(numeros)


