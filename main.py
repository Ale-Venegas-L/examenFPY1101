from functions import *
while True:
    os.system("cls")
    print("REPORTES")
    print("1. Asignar Sueldos.")
    print("2. Clasificar Sueldos.")
    print("3. Ver Estadisticas.")
    print("4. Reporte de Sueldos.")
    print("5. Salir del programa.")
    opc = verify_opc() 
    if opc==1:
        asignar()
    elif opc==2:
        clasify()
    elif opc==3:
        pass
    elif opc==4:
        pass
    elif opc==5:
        pass
    else:
        print("Debe ingresar una de nuestras opciones, intente de nuevo")
        time.sleep(1)