productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
             '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
             'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
             'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
             'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
             '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
             '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
             'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
}
#append y lower validar si es mayuscula y minuscula
stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
         'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
         'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0],
}

def stock_marca(marca):
    for i in productos:
        if productos[i][0].lower()== marca.lower():
            print(f"El stock es: {productos[i][0]}")
def búsqueda_precio(p_min, p_max):
    lista = []
    for i in stock:
        if stock [i][0]>= p_min and stock [i][0]<=p_max:
            lista.append(f"{productos[i][0]} -- {i}")
    if len(lista) > 0:
        for i in sorted (lista):
            print(i)
    else :
        print ("No hay notebooks en ese rango de precios.")
def actualizar_precio(modelo,p):
    if modelo in stock:
        stock[modelo][0] = int(p)
        return True
    else :
        return False
def main():
    while True:
        print("\n*** MENU PRINCIPAL ***")
        print("1. Stock marca.")
        print("2. Búsqueda por precio.")
        print("3. Actualizar precio.")
        print("4. Salir.")
        
        while True:
            try:
                opcion = int(input("Ingrese opcion: "))
                if (opcion<1 or opcion >4):
                    print("Debe elegir una opion entre el 1 y el 4.")
                else : break
            except:
                print("Debe seleccionar una opción válida!!")
        if opcion == 1:
            marca_ingresada = input("Ingrese marca a consultar: ")
            stock_marca(marca_ingresada)
        elif opcion == 2:
            try:
                minIngresado = int(input("Ingrese precio mínimo: "))
                try:
                    maxIngresado = int(input("Ingrese precio máximo: "))
                    búsqueda_precio(minIngresado, maxIngresado)
                except ValueError: 
                    print("Debe ingresar valores enteros!!")
            except ValueError:
                print("Debe ingresar valores enteros!!")
        elif opcion == 3:
            while True:
                modeloIngresado = input("Ingrese el modelo a actualizar: ")
                precioIngresado = input("Ingrese precio nuevo: ")
                if actualizar_precio(modeloIngresado, precioIngresado)== True:
                    print("Precio actualizado!!")
                else:
                    print("El modelo no existe!!")
                    actualizar = input("Desea actualizar otro precio(s/n): ")
                if actualizar=='n':
                    break
        elif opcion == 4:
            print("Programa finalizado.")
            break
main()
        
        
                    
                
    