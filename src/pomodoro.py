import sys
import time

def define_parametros():
    repeticiones = input("Número de repeticiones:")
    workout = input("Tiempo de workout (s):")
    descanso = input("Tiempo de descanso (s):")
    return [repeticiones, workout, descanso]

def cuenta_atras(s, etiqueta):
    """ Imprime el tiempo hacia atrás s segundos """
    for i in range(s, -1, -1):
        sys.stdout.write('\r' + etiqueta +': %i s' % i)
        sys.stdout.flush()
        time.sleep(1)    

def main():
    #pprint(loglines)
    parametros = define_parametros()
    parametros = list(
        map(
            int,
            parametros))
    for r in range(parametros[0]):
        cuenta_atras(parametros[1], 'Workout ' + str(r + 1) + ' de ' + str(parametros[0]))
        if r < parametros[0]:
            cuenta_atras(parametros[2], 'Descanso ' + str(r + 1) + ' de ' + str(parametros[0]))
    print("\rSerie terminada!")
    
if __name__ == "__main__":
    main()