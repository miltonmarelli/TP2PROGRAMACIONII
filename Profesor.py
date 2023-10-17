from Usuario import Usuario

class Profesor(Usuario):
    def __init__(self, nombre, apellido, email, contrasenia, titulo, anio_egreso):
        super().__init__(nombre, apellido, email, contrasenia)
        self.__titulo = titulo
        self.__anio_egreso = anio_egreso
        
    @property
    def titulo(self):
        return self.__titulo
    @property
    def anio_egreso(self):
        return self.__anio_egreso
    


    def infoProfesor(self):
        return f"Profesor: {self.nombre} {self.apellido}"

    def dictar_curso(self, curso):
        pass
    
    def validar_credenciales(self, email, contrasenia):
        return self.email == email and self.contrasenia == contrasenia