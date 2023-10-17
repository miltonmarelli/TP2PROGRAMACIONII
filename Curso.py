from Estudiante import Estudiante
from Profesor import Profesor

class Curso(Estudiante, Profesor):
    def __init__(self, nombreCurso, contrasenia_matriculacion):
        super().__init__('', '', '', '', 0, 0)
        self.__nombreCurso = nombreCurso
        self.__contrasenia_matriculacion = contrasenia_matriculacion

    @property
    def nombreCurso(self):
        return self.__nombreCurso
    @property
    def contrasenia_matriculacion(self):
        return self.__contrasenia_matriculacion
    
    def infoCurso(self):
        return f"Curso: {self.__nombre}"

    def generar_contrasenia(self):
        pass