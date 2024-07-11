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
                ["Elena Fernández"]]

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
    eightyToTwoMil = []
    overTwoMil = []
    lessEightyHundredC = 0
    eightyToTwoMilC = 0
    overTwoMilC = 0
    if len(trabajadores[0])==2:
        for i in trabajadores:  
            if i[1] < 800000:
                 lessEightyHundred.append(i)
                 lessEightyHundredC = lessEightyHundredC + 1
            elif i[1]>800000 and i[1]<2000000:
                eightyToTwoMil.append(i)
                eightyToTwoMilC = eightyToTwoMilC+1
            else:
                overTwoMil.append(i)
                overTwoMilC = overTwoMilC+1

        print(f"Menos de 800 000: {lessEightyHundredC}")              
        print("Empleado | Salario")              
        for i in lessEightyHundred:
            print(i)
            time.sleep(1)
        time.sleep(1)
        print()
        time.sleep(1)
        print(f"Entre 800 000 y 2 000 000: {eightyToTwoMilC}")
        print("Empleado | Salario")
        for i in eightyToTwoMil:
            print(i)
            time.sleep(1)
        time.sleep(1)
        print()
        time.sleep(1)
        print(f"Más de 2 000 000: {overTwoMilC}")    
        print("Empleado | Salario")
        for i in overTwoMil:
            print(i)
            time.sleep(2)
    else:
        print("No existen sueldos para analizar")


def stats():
    money = []
    number1 = 0
    number2 = 1
    if len(trabajadores[0])==2:
        for i in trabajadores:
                money.append(i[1])
        money.sort()
        for i in money:
            number1 = number1 + i
            number2 = number2 * i 
        promedio = number1/10
        mg = number2*(1/10)
        #me acordaba de como poner potencias acá? no ❤ y ^ no era al parecer
        print(f"El menor salario es: {money[0]}")
        print(f"El mayor salario es: {money[9]}")
        print(f"El promedio de salarios es: {promedio}")
        print(f"La media geométrica de salarios es: {mg}")
        time.sleep(1)
    else:
        print("No existen sueldos para analizar")
    
def report():
    if len(trabajadores[0])==2:
        with open("file.csv", "w") as File:
            FileR = csv.writer(File)
            title = ["Nombre empleado","Sueldo Base","Isapre/Fonasa","Sueldo liquido"]
            FileR.writerow(title)
            for i in trabajadores:
                sueldo = i[1]
                afp = sueldo * 0.12
                salud = sueldo * 0.07
                sueldoL = sueldo - (afp+salud)
                i.append(salud)
                i.append(afp)
                i.append(sueldoL)
                FileR.writerow(i)
        print("(❁´◡`❁) Ha sido creado el reporte de sueldos")
    else:
        print("No existen sueldos, no se puede imprimir")
    time.sleep(1)
