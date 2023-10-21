from Estudiante import Estudiante
from Profesor import Profesor
from Curso import Curso
from functions import ingresar_como_alumno 

estudiantes = []
profesores = []
carreras =[]

estudiante1 = Estudiante('Milton', 'marelli', 'milton@ejemplo.com', 'password', 1, 2023)
estudiantes.append(estudiante1)
estudiante2 = Estudiante('Joel', 'pepe', 'joel@ejemplo.com', 'password', 2, 2023)
estudiantes.append(estudiante2)
estudiante3 = Estudiante('Ciro', 'pepi', 'ciro@ejemplo.com', 'password', 3, 2023)
estudiantes.append(estudiante3)
    
profesor1 = Profesor('Mercedes', 'Valoni', 'mercedes@ejemplo.com', 'password', 'Programacion', 2010)
profesores.append(profesor1)
profesor2 = Profesor('Tomas', 'Ponce', 'tomas@ejemplo.com', 'password', 'Programacion', 2008)
profesores.append(profesor2)

curso1 = Curso('InglesI','matricula123')
carreras.append(curso1)
curso2 = Curso('InglesII','matricula123')
carreras.append(curso2)
curso3 = Curso('Laboratorio I','matricula123')
carreras.append(curso3)
curso4 = Curso('Laboratorio II', 'matricula123')
carreras.append(curso4)
curso5 = Curso('Programación I','matricula123')
carreras.append(curso5)
curso6 = Curso('Programación II', 'matricula123')
carreras.append(curso6)

while True:
    print("Menú:")
    print("1. Ingresar como alumno")
    print("2. Ingresar como profesor")
    print("3. Ver cursos")
    print("4. Salir")
    opcion = input("Seleccione una opcion: ")
    if opcion == "1":
        estudiante = ingresar_como_alumno(estudiantes)
        if estudiante is not None:
            while True:
                    print("Submenu Alumno:")
                    print("1. Matricularse a un curso")
                    print("2. Ver curso")
                    print("3. Volver al menú principal")
                    sub_opcion = input("\tSeleccione una opción: \n")
                    if sub_opcion == "1":
                        print("Lista de cursos disponibles:\n")
                        for i, curso in enumerate(carreras, start=1): #enumera los cursos de la lista carrera ,empiesa en 1 
                            print(f"{i}. {curso.nombreCurso}")
                        opcion_curso = input("\t Seleccione el Numero del curso: \n")
                        if opcion_curso.isdigit(): #se verifica que se ingreso un numero 
                            opcion_curso = int(opcion_curso) #se convierte en entero
                            if 1 <= opcion_curso <= len(carreras):
                                curso_elegido = carreras[opcion_curso - 1] #se resta 1 porque la lista empiesa con el indice 0 
                                estudiante.matricular_en_curso(curso_elegido) 
                            else:
                                print("Numero no valido ")
                        else:
                            print("Ingrese un numero valido") 
                    elif sub_opcion == "2":
                        if len(estudiante.mis_cursos) > 0:
                            print("\t Cursos matriculados:")
                            for curso in estudiante.mis_cursos:
                                print(f"\t Nombre: - {curso.nombreCurso} -")
                        else:
                            print("\t No se ha anotado en ningun curso aun!")
                    elif sub_opcion == "3":
                        break                   
        elif opcion == "2":
            from functions import ingresar_como_profesor
            ingresar_como_profesor(profesores)
        elif opcion == "3":
            curso_ordenado = sorted(carreras, key=lambda curso: curso.nombreCurso)
            for curso in curso_ordenado:
                print(f"Materia: {curso.nombreCurso} \n Carrera: Tecnicatura Universitaria en Programacion")
        elif opcion == "4":
            print("Saliendo del sistema")
            break
    else:
        print("Ingrese una opcion valida")

        
        