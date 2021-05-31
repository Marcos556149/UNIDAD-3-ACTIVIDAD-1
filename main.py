from ManejaLibros import ManejadorLibros
if __name__=='__main__':
    Libros= ManejadorLibros()
    Libros.leerArchivo()
    while True:
        print("_____MENU DE OPCIONES_____")
        print("[1]...Mostrar titulo de libro, cantidad total de paginas y nombre de sus capitulos")
        print("[2]...Dada una palabra mostrar titulo y autor de los libros que contengan la palabra")
        print("[0]...Salir")
        try:
            op= int(input('Seleccione una opcion: '))
            if op in range(3):
                if op == 1:
                    ident= int(input('Ingrese un identificador de un libro: '))
                    Libros.buscarLibro(ident)
                if op == 2:
                    palabra= input("Ingrese una palabra: ")
                    Libros.buscarPalabra(palabra)
                if op == 0:
                    print("_____MENU FINALIZADO_____")
                    break
            else:
                print("ERROR, solo puede ingresar numeros del 0 al 2")
        except ValueError:
            print("ERROR, ingrese solamente numeros")
