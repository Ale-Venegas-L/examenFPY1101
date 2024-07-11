import random, os, time
aleatorio = random.randint(300000,2500000)
trabajadores = [["Juan Pérez"],["María García"],["Carlos López"],["Ana Martínez"],
                ["Pedro Rodríguez"],["Laura Hernández"],["Miguel Sánchez"],
                ["Isabel Gómez"],["Francisco Díaz"],["Elena Fernández"]]
def verify_opc():
    try:
        while True:
            op = int(input("Ingrese opción: "))
            return op
    except:
        print("Debe ingresar un número, intente de nuevo")
        time.sleep(1)

def asignar():
    for i in trabajadores:
        aleatorio = random.randint(300000,2500000)
        i.append(aleatorio)
        print("Sueldos asignados! ╰(*°▽°*)╯")



asignar()