from Usuario import Usuario

class Estudiante(Usuario):
    def __init__(self, nombre, apellido, email, contrasenia, legajo, anio_inscripcion_carrera):
        super().__init__(nombre, apellido, email, contrasenia)
        self.__legajo = legajo
        self.__anio_inscripcion_carrera = anio_inscripcion_carrera
        self.__mis_cursos = []

    @property
    def legajo(self):
        return self.__legajo

    @property
    def anio_inscripcion_carrera(self):
        return self.__anio_inscripcion_carrera
    
    @property
    def mis_cursos(self):
        return self.__mis_cursos
    
    def matricular_en_curso(self, curso):
        if curso not in self.mis_cursos:
            contrasenia_ingresada = input(f"\t Ingrese la contraseña de matriculación del curso -{curso.nombreCurso}-: \n ")
            if contrasenia_ingresada == curso.contrasenia_matriculacion:
                self.mis_cursos.append(curso)
                print(f"\t Te has matriculado en el curso -{curso.nombreCurso}-!")
            else:
                print("contraseña incorrecta")
        else:
            print("\t Ya estas matriculado en este curso! ")
        
    def infoUsuario(self):
        return f"Estudiante: {self.nombre} {self.apellido}"

    def validar_credenciales(self, email, contrasenia):
        return self.email == email and self.contrasenia == contrasenia