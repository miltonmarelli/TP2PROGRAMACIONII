from Archivo import Archivo
from Carrera import Carrera 
import random
import string

class Curso:
    prox_codigo = 1
    def __init__(self, nombreCurso, contrasenia_matriculacion, Carrera, archivo=None):
        self.__nombreCurso = nombreCurso
        self.__contrasenia_matriculacion = contrasenia_matriculacion
        self.__carrera = Carrera 
        self.__codigo = Curso.prox_codigo 
        Curso.prox_codigo += 1
        self.__archivo= []

    @property
    def nombreCurso(self):
        return self.__nombreCurso

    @property
    def contrasenia_matriculacion(self):
        return self.__contrasenia_matriculacion
    
    @contrasenia_matriculacion.setter
    def contrasenia_matriculacion(self, nueva_contrasenia):
        self.__contrasenia_matriculacion = nueva_contrasenia
    
    @property
    def carrera(self):
        return self.__carrera
    
    @property
    def codigo(self):
        return self.__codigo
    
    @property
    def archivo(self):
        return self.__archivo
    
    def infoCurso(self):
        return f"Curso: {self.__nombreCurso}"
    
    # reciclo codigo del TP anterior dado por los profes
    @classmethod
    def generar_contrasenia(cls): #si se hace privada (__) no funciona en el llamado de la class Profesor 
        characters = string.ascii_letters + string.digits
        cod = ''.join(random.choice(characters) for i in range(8))
        return cod
    
    
    def NuevoArchivo(self, archivo):
        self.__archivo.append(archivo)
