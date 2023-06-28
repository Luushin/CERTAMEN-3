import os
os.system("cls")


nompersona = input("Ingrese su nombre:")
apellpersona = input("Ingrese apellido: ")

menu = '''
1. Registrar un producto
2. Buscar un producto
3. Listar un producto
4. Salir del sistema
'''

codnum = []
nombre = []
precio = []
categoria = []
cantstock = []

while True:
    try:
        opc = int(input(menu))
        if opc == 4:
            print(f"Ha deseado salir, gracias por elegirnos {nompersona} {apellpersona}, hasta pronto")
            print("VERSION 1.0 ILUFIN SYSTEM")
            break

        elif opc == 1:
            while True:
                try:
                    codigo = int(input("Código de séis dígitos a ingresar: "))
                    if codigo >= 100000 and codigo < 1000000: 
                        codnum.append(codigo)
                        print(codnum)
                        break
                    else:
                        print("Por favor, intente nuevamente.")
                except:
                    print("Excepción de código, intente nuevamente.")
            while True:
                try:
                    nom = input("Ingrese nombre del producto:")
                    if len(nom) >= 2 and len(nom) <= 50:
                        nombre.append(nom) 
                        print(nombre)
                        break
                    else:
                        print("Por favor, intente nuevamente.")
                except:
                    print("Excepción en el nombre, por favor, intente nuevamente.")
            while True: 
                try:
                    prec = int(input("Precio a inggresar: "))
                    if prec > 0:
                        precio.append(prec)
                        print(precio)
                        break
                    else:
                        print ("Por favor, intente nuevamente.")
                except:
                    print("Ocurrió una excepción de precio, por favor, intente nuevamente")
            while True:
                try:
                    categ = input("¿Encomienda por sobre o paquete?:")
                    if categ == "paquete" or categ == "sobre":
                        categoria.append(categ)
                        print(categoria)
                        break
                    else:
                        print("La categoría es invalida, por favor, ingresar categoría válida.")
                except:
                    print("Ocurrió una excepción en la categoría, intente nuevamente.")
            while True:
                try:
                    stock = int(input("Stock del producto a ingresar:"))
                    if stock > 0:
                        cantstock.append(stock)
                        print(cantstock)
                        break
                    else:
                        print("Por favor, intente nuevamente.")
                except:
                    print("Ocurrió una excepción, por favor, intente nuevamente.")
        elif opc == 2:
            busca = int(input("Código de 6 dígitos a buscar: "))
            print(f"Ha seleccionado buscar {busca} \n")
            print("|   CÓDIGO NUMÉRICO  |   NOMBRE   |   CATEGORÍA PRODUCTO   |   PRECIO PRODUCTO  |  STOCK PRODUCTO  |")
            print("--+------------------+------------+------------------------+--------------------+------------------+")
            for i in range(len(codnum)):
                if busca == codnum[i] and busca >= 100000 and busca < 1000000:
                    print(f"|  {codnum[i]:9d}        |    {nombre[i]:10s}  |    {categoria[i]:8s}    |   {precio[i]:7d}     |     {cantstock[i]:5d}| ")
                    print("--+------------------+------------+------------------------+--------------------+------------------+")
        elif opc == 3:
            print("|   CÓDIGO NUMÉRICO  |   NOMBRE   |   CATEGORÍA PRODUCTO   |   PRECIO PRODUCTO  |  STOCK PRODUCTO  |")
            print("--+------------------+------------+------------------------+--------------------+------------------+")
            contsto = 0
            for i in range(len(codnum)):
                if cantstock[i] < 5:
                    sto = "Stock en cantidad baja"
                    contsto += 1
                else:
                    sto = "Stock en límite "
                print(f"|  {codnum[i]:9d}        |    {nombre[i]:10s}  |    {categoria[i]:8s}    |   {precio[i]:7d}     |     {cantstock[i]:5d}|  {sto} ")
                print("--+------------------+------------+------------------------+--------------------+------------------+")
                print(f"Stock bajos: {contsto}")
    except:
        print("Ocurrió una excepción, intente nuevamente.")