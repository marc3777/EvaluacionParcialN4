stock_zapatillas = 20
reserva_zapatilla = -1
vip = -1

while True:
    print("\nTOTEM AUTOATENCIÓN RESERVA STRIKE")
    print("1.- Reservar zapatillas")
    print("2.- Buscar zapatillas reservadas.")
    print("3.- Ver stock de reservas.")
    print("4.- Salir.")
    
    while True:
        try:
            opcion =int(input("Selccione una opción(1-4): "))
            if (opcion<1 or opcion >4):
               print("Debe elegir una opción entre 1 y 4")
            else: break
        except:
            print("Debe ingresar una opción válida!!")
    if opcion == 1:
        stock_zapatillas = stock_zapatillas - reserva_zapatilla
        print("-- Reservar Zapatillas --")
        nombre_comprador = input("Nombre del comprador: ")
        frase_secreta = input("Digite la palabra secreta para comfirmar la reserva: ")
        print (f"Reserva realizada excitosamente para {nombre_comprador}")
    elif opcion == 2:
        print("-- Buscar Zapatillas Reservadas --")
        try:
            print(input("Nombre del comprador a buscar: "))
            print(f"Reserva encontrada: {nombre_comprador} -1 par(es) (estándar)")
            
            
            
    elif opcion == 3:
        print("-- Ver Stock de Reservas --")
        print(f"Pares Resesvados: {reserva_zapatilla}")      
        print(f"Pares disponibles: {stock_zapatillas}")
        
    elif opcion == 4:
        print ("Programa terminado...")    
        break
