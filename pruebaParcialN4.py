stock_zapatillas = 20
frase_secreta1= 'EstoyEnListaDeReserva'
lista_nombres = {}

def opcion1 ():
                print("-- Reservar Zapatillas --")
                nombre_comprador = input("Nombre del comprador: ")
                if nombre_comprador not in lista_nombres:
                    frase_secreta = input("Digite la palabra secreta para confirmar la reserva: ")
                    if frase_secreta == frase_secreta1:
                        if  len(lista_nombres) >= stock_zapatillas:
                            print("No hay stock para reserva.")
                        else: 
                                lista_nombres[nombre_comprador] = 1
                                print (f"Reserva realizada excitosamente para {nombre_comprador}")
                    else:print("Error: palabra clave incorrecta. Reserva no realizada")
                else: print("Este nombre ya cuenta con reserva.")
                
def opcion2():
                print("-- Buscar Zapatillas Reservadas --")
                nombre_ingresado = (input("Nombre del comprador a buscar: "))
                if nombre_ingresado in lista_nombres:
                    cantidad = lista_nombres[nombre_ingresado]
                    tipo = 'estandar' if cantidad == 1 else "vip"
                    print(f"Reserva encontrada: {nombre_ingresado} - {cantidad} par(es) {tipo}")
                    if cantidad == 1 and (stock_zapatillas - sum (lista_nombres.values()))>= 1:
                        vip = input("¿Desea pagar adicional para VIP y reservar 2 pares? (s/n): ")
                        if vip == 's':
                            lista_nombres [nombre_ingresado]= 2
                            print(f"Reserva actualizada a VIP. Ahora {nombre_ingresado} tiene 2 pares reservados.")
                        else:
                            print("Manteniendo reserva actual.")
                    elif cantidad == 2:
                        print("El cliente ya cuenta con reserva vip.")
                    else:
                        print("No hay stock suficiente para vip.")
                else:
                    print("Nombre ingresasdo no cuenta con reserva.")

def opcion3():
                total_reservas = sum(lista_nombres.values())
                pares_diponibles = stock_zapatillas - total_reservas
                print("-- Ver Stock de Reservas --")
                print(f"Pares Reservados: {total_reservas}")
                print(f"Pares disponibles: {pares_diponibles}")
def main():
    while True:
        print("\nTOTEM AUTOATENCIÓN RESERVA STRIKE")
        print("1.- Reservar zapatillas.")
        print("2.- Buscar zapatillas reservadas.")
        print("3.- Ver stock de reservas.")
        print("4.- Salir.")
        
        while True:
            try:
                opcion =int(input("Selccione una opción(1-4): "))
                if (opcion<1 or opcion >4):
                    print("Debe elegir una opción entre 1 y 4.")
                else: break
            except:
                print("Debe ingresar una opción válida!!")
        if opcion == 1:
            opcion1()
        elif opcion == 2:
            opcion2()
        elif opcion == 3:
            opcion3()
        elif opcion == 4:
            print ("Programa terminado...")    
            break
main()
