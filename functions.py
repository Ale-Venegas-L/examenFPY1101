import random, os, time, csv
trabajadores = [["Juan Pérez"],
                ["María García"],
                ["Carlos López"],
                ["Ana Martínez"],
                ["Pedro Rodríguez"],
                ["Laura Hernández"],
                ["Miguel Sánchez"],
                ["Isabel Gómez"],
                ["Francisco Díaz"],
                ["Elena Fernández", "chucrut"]]

def verify_opc():
    try:
        while True:
            op = int(input("Ingrese opción: "))
            return op
    except:
        print("Debe ingresar un número, intente de nuevo")
        time.sleep(1)

def asignar():
        if len(trabajadores[0])==2:
            print("Ya existen sueldos, no se pueden reasignar")
            time.sleep(1)
        else:
            for i in trabajadores:
                aleatorio = random.randint(300000,2500000)
                i.append(aleatorio)
            print("Sueldos asignados! ╰(*°▽°*)╯")
            time.sleep(1)


def clasify():
    lessEightyHundred = []
    lessEightyHundredC = 0
    eightyToTwoMil = []
    eightyToTwoMilC= 0
    overTwoMil = []
    overTwoMilC= 0
    if len(trabajadores)<10:
        for i in trabajadores:
            for n in i:
                if i[1]<8000000:
                    lessEightyHundred.append(i)
                    lessEightyHundredC + 1
                elif i[1]>8000000 and n<20000000:
                    eightyToTwoMil.append(i)
                    eightyToTwoMilC + 1
                else:
                    overTwoMil.append(i)
                    overTwoMilC + 1
        print(f"Menos de 800 000: {lessEightyHundredC}")    
        time.sleep(1)            
        print(lessEightyHundredC)
        time.sleep(1)
        print(f"Entre 800 000 y 2 000 000: {eightyToTwoMil}")
        time.sleep(1)
        print(eightyToTwoMilC)
        time.sleep(1)
        print(f"Más de 2 000 000: {overTwoMil}")    
        time.sleep(1)
        print(overTwoMilC)  
    else:
        print("No existen sueldos para analizar")
