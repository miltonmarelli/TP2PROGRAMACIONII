from Usuario import Usuario

class Estudiante(Usuario):
    def __init__(self, nombre, apellido, email, contrasenia, legajo, anio_inscripcion_carrera):
        super().__init__(nombre, apellido, email, contrasenia)
        self.__legajo = legajo
        self.__anio_inscripcion_carrera = anio_inscripcion_carrera

    @property
    def legajo(self):
        return self.__legajo
    @property
    def anio_inscripcion_carrera(self):
        return self.__anio_inscripcion_carrera
    
    def infoEstudiante(self):
        return f"Estudiante: {self.nombre} {self.apellido}"

    def matricular_en_curso(self, curso):
        pass
    
    def validar_credenciales(self, email, contrasenia):
        return self.email == email and self.contrasenia == contrasenia