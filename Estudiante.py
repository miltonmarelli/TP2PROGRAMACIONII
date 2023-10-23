from Usuario import Usuario
from Carrera import Carrera 

class Estudiante(Usuario):
    def __init__(self, nombre, apellido, email, contrasenia, legajo, anio_inscripcion_carrera, Carrera):
        super().__init__(nombre, apellido, email, contrasenia)
        self.__legajo = legajo
        self.__anio_inscripcion_carrera = anio_inscripcion_carrera
        self.__mis_cursos = []
        self.__carrera = Carrera

    @property
    def legajo(self):
        return self.__legajo

    @property
    def anio_inscripcion_carrera(self):
        return self.__anio_inscripcion_carrera
    
    @property
    def mis_cursos(self):
        return self.__mis_cursos
    
    @property
    def carrera(self):
        return self.__carrera
    
    def infoUsuario(self):
        return f"Estudiante: {self.nombre} {self.apellido} \n Carrera {self.carrera} \n Cursos {self.mis_cursos}"

    def validar_credenciales(self, email, contrasenia):
        if self.email == email and self.contrasenia == contrasenia:
            return True
        else:
            return False
    
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
    
    def desmatricular_curso(self, mis_cursos):
        if not mis_cursos:
            print("\t No estas matriculado en ningun curso")
            return
        print("Tus cursos matriculados:")
        for i, curso in enumerate(mis_cursos, start=1):
            print(f"{i}. {curso.nombreCurso}")
        opcion_curso = input("\tSelecciona el numero del curso que deseas desmatricular: ")
        if opcion_curso.isdigit():
            opcion_curso = int(opcion_curso)
            if 1 <= opcion_curso <= len(mis_cursos):
                curso_elegido = mis_cursos[opcion_curso - 1]
                confirmacion = input(f" Desea Desmatricular '{curso_elegido.nombreCurso}'? (s/n): ")
                if confirmacion.lower() == 's':
                    contrasenia_alumno = input("Ingrese su contraseña: ")
                    if contrasenia_alumno == self.contrasenia:
                        mis_cursos.remove(curso_elegido)
                        print(f"\t Se ha removido '{curso_elegido.nombreCurso}' de tus cursos")
                    else:
                        print("Contraseña incorrecta")
                else:
                    print("Operacion cancelada")
            else:
                print("Numero no valido")
        else:
            print("Ingrese un numero valido")
    