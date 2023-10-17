from Estudiante import Estudiante
from Profesor import Profesor
from Curso import Curso
from app import *


def ingresar_como_alumno(Estudiantes:list):
                email = input("Ingrese su email: ")
                estudiante = None
                for alumno in Estudiantes:
                    if alumno.email == email:
                        estudiante = alumno
                        break
                if estudiante is not None:
                    contrasenia = input("Ingrese su contraseña: ")
                    if estudiante.validar_credenciales(email, contrasenia):
                        print(f"Bienvenido, {estudiante.nombre} {estudiante.apellido}!")                
                    else:
                        print("Contraseña incorrecta")
                else:
                    print("Alumno no encontrado, darse de alta en alumnado")
                    
                    
def ingresar_como_profesor(profesores:list):
    email = input("Ingrese su email: ")
    profesor = None
    for prof in profesores:
        if prof.email == email:
            profesor = prof
            break
    if profesor is not None:
        contrasenia = input("Ingrese su contraseña: ")
        if profesor.validar_credenciales(email, contrasenia):
            print(f"Bienvenido, Profesor {profesor.nombre} {profesor.apellido}!")
        else:
            print("Contraseña incorrecta")
    else:
        print("Profesor no encontrado, darse de alta en alumnado")