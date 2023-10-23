from datetime import date

class Archivo:
    def __init__(self, nombre, formato):
        self.__nombre = nombre
        self.__fecha = date.today()
        self.__formato = formato

    @property
    def nombre(self):
        return self.__nombre

    @property
    def fecha(self):
        return self.__fecha

    @property
    def formato(self):
        return self.__formato

    def infoArchivo(self):
        return f"Nombre: {self.__nombre}, Fecha: {self.__fecha}, Formato: {self.__formato}"






