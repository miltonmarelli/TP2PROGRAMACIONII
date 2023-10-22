import random
import string

class Curso:
    def __init__(self, nombreCurso, contrasenia_matriculacion):
        self.__nombreCurso = nombreCurso
        self.__contrasenia_matriculacion = contrasenia_matriculacion

    @property
    def nombreCurso(self):
        return self.__nombreCurso

    @property
    def contrasenia_matriculacion(self):
        return self.__contrasenia_matriculacion
    
    @contrasenia_matriculacion.setter
    def contrasenia_matriculacion(self, nueva_contrasenia):
        self.__contrasenia_matriculacion = nueva_contrasenia
    
    @classmethod
    def generar_contrasenia(cls): 
        # reciclo codigo del TP anterior dado por los profes
        characters = string.ascii_letters + string.digits
        cod = ''.join(random.choice(characters) for i in range(8))
        return cod
    
    
    def infoCurso(self):
        return f"Curso: {self.__nombreCurso}"
