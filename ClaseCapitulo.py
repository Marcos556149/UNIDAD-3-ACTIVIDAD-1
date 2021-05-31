class Capitulo:
    __titulo= ''
    __cantidadPaginas= ''
    def __init__(self,titu='',cantPag=''):
        self.__titulo= titu
        self.__cantidadPaginas= cantPag
    def __str__(self):
        return 'TITULO: {}, CANTIDAD DE PAGINAS: {}'.format(self.__titulo,self.__cantidadPaginas)
    def getTituloo(self):
        return self.__titulo
    def getPaginas(self):
        return self.__cantidadPaginas
