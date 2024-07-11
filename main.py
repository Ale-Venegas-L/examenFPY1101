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
        stats()
    elif opc==4:
        report()
    elif opc==5:
        print("Saliendo del programa...")
        print("Alejandro Venegas - 22041459-0")
        break    
    else:
        print("Debe ingresar una de nuestras opciones, intente de nuevo")
        time.sleep(1)