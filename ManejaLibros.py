import csv
from ClaseLibro import Libro
class ManejadorLibros:
    __listaLibros= []
    def __init__(self):
        self.__listaLibros= []
    def leerArchivo(self):
        archivo= open('libros.csv')
        reader= csv.reader(archivo,delimiter=',')
        for fila in reader:
            if len(fila) == 2:               #cantidad de atributos de la clase Capitulo
                titu= fila[0]
                cantPag= int(fila[1])
                libroo.agregarCapitulo(titu,cantPag)
            else:
                id= int(fila[0])
                tit= fila[1]
                aut= fila[2]
                edit= fila[3]
                isb= fila[4]
                cantCap= fila[5]
                libroo= Libro(id,tit,aut,edit,isb,cantCap)
                self.__listaLibros.append(libroo)
        archivo.close()
    def buscarLibro(self,ident):
        indicee= 0
        cont= 0
        bandera= False
        while (indicee < len(self.__listaLibros))and(bandera == False):
            if ident == self.__listaLibros[indicee].getID():
                bandera = True
            indicee += 1
        if bandera:
            indicee -= 1
            print("TITULO: {}".format(self.__listaLibros[indicee].getTitulo()))
            print("CAPITULOS")
            for k in range(self.__listaLibros[indicee].getLongitudCapitulos()):
                print(self.__listaLibros[indicee].MostrarNombreCapitulo(k))
                cont += self.__listaLibros[indicee].obtenerPaginas(k)
            print("CANTIDAD TOTAL DE PAGINAS: ",cont)
        else:
            print("ERROR, el identificador que ingreso no corresponde a ningun libro")
    def buscarPalabra(self,palabra):
        SeEncontroOno= 0
        for p in range(len(self.__listaLibros)):
            if palabra.lower() in self.__listaLibros[p].getTitulo().lower():
                print("TITULO: {}, AUTOR: {}".format(self.__listaLibros[p].getTitulo(),self.__listaLibros[p].getAutor()))
                SeEncontroOno += 1
            else:
                w=0
                bandera3= True
                longitudCapitulos= self.__listaLibros[p].getLongitudCapitulos()
                while (bandera3)and(w < longitudCapitulos):
                    if palabra.lower() in self.__listaLibros[p].MostrarNombreCapitulo(w).lower():
                        print("TITULO: {}, AUTOR: {}".format(self.__listaLibros[p].getTitulo(),self.__listaLibros[p].getAutor()))
                        bandera3= False
                        SeEncontroOno += 1
                    w += 1
        if (SeEncontroOno == 0):
            print("No se encontro ningun libro o capitulo que contenga la palabra dada")
