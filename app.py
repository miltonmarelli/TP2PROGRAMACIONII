from Usuario import *
from Estudiante import *
from Profesor import *
from Curso import *
from functions import *    
    
estudiantes = []#no funciona , hacerlo ver con profe
profesores = []
carreras =[]

estudiante1 = Estudiante('Milton', 'marelli', 'milton@ejemplo.com', 'password', 1, 2023)
estudiantes.append(estudiante1)
estudiante2 = Estudiante('Joel', 'pepe', 'joel@ejemplo.com', 'password', 2, 2023)
estudiantes.append(estudiante2)
estudiante3 = Estudiante('Ciro', 'pepi', 'ciro@ejemplo.com', 'password', 3, 2023)#no funciona , hacerlo ver con profe
estudiantes.append(estudiante3)
    
profesor1 = Profesor('Mercedes', 'Valoni', 'mercedes@ejemplo.com', 'password', 'Programacion', 2010)
profesores.append(profesor1)
profesor2 = Profesor('Tomas', 'Ponce', 'tomas@ejemplo.com', 'password', 'Programacion', 2008)
profesores.append(profesor2)
curso1 = Curso('Programacion', 'matriculacion123')  #no funciona , hacerlo ver con profe
carreras.append(curso1)

while True:
    print("Menú:")
    print("1. Ingresar como alumno")
    print("2. Ingresar como profesor")
    print("3. Ver cursos")
    print("4. Salir")
    opcion = input("Seleccione una opcion: ")
    if opcion == "1":
        ingresar_como_alumno(estudiantes)  #no funciona , hacerlo ver con profe      
    elif opcion == "2":
        ingresar_como_profesor(profesores) #no funciona , hacerlo ver con profe
    elif opcion == "3":
        pass
    elif opcion == "4":
        print("Saliendo del sistema")
        break
    else:
        print("Ingrese una opcion valida")
        
        
        
        