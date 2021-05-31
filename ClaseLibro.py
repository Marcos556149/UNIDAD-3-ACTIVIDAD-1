from ClaseCapitulo import Capitulo
class Libro:
    __idLibro= ''
    __titulo= ''
    __autor= ''
    __editorial= ''
    __isbn= ''
    __cantidadCapitulos= ''
    __capitulos= []
    def __init__(self,id='',tit='',aut='',edit='',isb='',cantCap=''):
        self.__idLibro= id
        self.__titulo= tit
        self.__autor= aut
        self.__editorial= edit
        self.__isbn= isb
        self.__cantidadCapitulos= cantCap
        self.__capitulos= []
    def __str__(self):
        return 'ID: {}, TITULO: {}, AUTOR: {}, EDITORIAL: {}, ISBN: {}, CANTIDAD DE CAPITULOS: {}'.format(self.__idLibro,self.__titulo,self.__autor,self.__editorial,self.__isbn,self.__cantidadCapitulos)
    def getLongitudCapitulos(self):
        return len(self.__capitulos)
    def MostrarNombreCapitulo(self,indice):
        return self.__capitulos[indice].getTituloo()
    def agregarCapitulo(self,titu,cantPag):
        capituloo= Capitulo(titu,cantPag)
        self.__capitulos.append(capituloo)
    def getID(self):
        return self.__idLibro
    def getTitulo(self):
        return self.__titulo
    def obtenerPaginas(self,indiceee):
        return self.__capitulos[indiceee].getPaginas()
    def getAutor(self):
        return self.__autor
