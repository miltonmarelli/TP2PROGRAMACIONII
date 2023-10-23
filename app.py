from Estudiante import Estudiante
from Profesor import Profesor
from Curso import Curso
from Archivo import Archivo
from Carrera import Carrera
from functions import ingresar_como_alumno
from functions import ingresar_como_profesor 

estudiantes = []
profesores = []
cursos=[]
carreras =[]
archivos=[]

estudiante1 = Estudiante('Milton', 'marelli', 'milton@ejemplo.com', 'password', 1, 2023, 'Tecnico en Programacion')
estudiantes.append(estudiante1)
estudiante2 = Estudiante('Lionel', 'Messi', 'messi@ejemplo.com', 'password', 2, 2023, 'Tecnico en Programacion')
estudiantes.append(estudiante2)
estudiante3 = Estudiante('Cristiano', 'Ronaldo', 'cr7@ejemplo.com', 'password', 3, 2023,'Tecnico en Programacion')
estudiantes.append(estudiante3)
    
profesor1 = Profesor('Mercedes', 'Valoni', 'mercedes@ejemplo.com', 'password', 'Programacion', 2010)
profesores.append(profesor1)
profesor2 = Profesor('Tomas', 'Ponce', 'tomas@ejemplo.com', 'password', 'Programacion', 2008)
profesores.append(profesor2)

carrera1= Carrera( 'Tecnico en Programacion' , 2)
carreras.append(carrera1)

curso1 = Curso('InglesI','matricula123','Tecnico_en_Programacion')
cursos.append(curso1) #se instancia curso para hacer prueba en matriculacion (facil contraseña)


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
                    print("2. Desmatricularse a un curso")
                    print("3. Ver curso")
                    print("4. Volver al menu principal")
                    sub_opcion = input("\tSeleccione una opcion: \n")
                    if sub_opcion == "1":
                        print("Lista de cursos disponibles:\n")
                        for i, curso in enumerate(cursos, start=1): #enumera los cursos de la lista cursos ,empiesa en 1 
                            print(f"{i}. {curso.nombreCurso}")
                        opcion_curso = input("\t Seleccione el Numero del curso: \n")
                        if opcion_curso.isdigit(): #se verifica que se ingreso un numero 
                            opcion_curso = int(opcion_curso) #se convierte en entero
                            if 1 <= opcion_curso <= len(cursos):
                                curso_elegido = cursos[opcion_curso - 1] #se resta 1 porque la lista empiesa con el indice 0 
                                estudiante.matricular_en_curso(curso_elegido) 
                            else:
                                print("-Numero no valido ")
                        else:
                            print("-Ingrese un numero valido")
                    elif sub_opcion == "2":
                        if len(estudiante.mis_cursos) > 0:
                            estudiante.desmatricular_curso(estudiante.mis_cursos)
                        else:
                            print("No estás matriculado en ningún curso.") 
                    elif sub_opcion == "3":
                        if len(estudiante.mis_cursos) > 0:
                            print("\t - Tus Cursos:")
                            for curso in estudiante.mis_cursos:
                                print(f"\t Nombre: - {curso.nombreCurso} -")
                        else:
                            print("\t -No se ha anotado en ningun curso aun!")
                    elif sub_opcion == "4":
                        break   
                    else:
                        print("Ingrese una opcion valida")                
    elif opcion == "2":
        profesor= ingresar_como_profesor(profesores)
        if profesor is not None:
            while True:
                print("Submenu Profesor:")
                print("1. Dictar curso")
                print("2. Ver cursos")
                print("3. Volver al menu principal")
                sub_opcion = input("\t -Seleccione una opcion: \n")
                if sub_opcion == "1":
                    nombre_curso = input("\tIngrese el nombre del curso: \n ")
                    nuevo_curso = profesor.dictar_curso(nombre_curso, cursos)
                    print(f"\t Curso dado de alta exitosamente! ")
                    print(f"\t NOMBRE : {nuevo_curso.nombreCurso}")
                    print(f"\t CODIGO: {nuevo_curso.codigo}")
                    print(f"\t CONTRASEÑA : ` {nuevo_curso.contrasenia_matriculacion} `\n")
                elif sub_opcion == "2":
                    if len(profesor.mis_cursos) > 0:
                        print("\t - Tus Cursos:")
                        for i, curso in enumerate(profesor.mis_cursos, start=1):
                            print(f"{i}. {curso.nombreCurso}")
                        opcion_curso = input("Seleccione el número del curso: ")
                        if opcion_curso.isdigit():
                            opcion_curso = int(opcion_curso)
                            if 1 <= opcion_curso <= len(profesor.mis_cursos):
                                curso_elegido = profesor.mis_cursos[opcion_curso - 1]
                                print(f"\tCurso: {curso_elegido.nombreCurso}")
                                print(f"\tCODIGO: {curso_elegido.codigo}")
                                print(f"\tCONTRASEÑA: {curso_elegido.contrasenia_matriculacion}")
                                print(f"\tCANTIDAD DE ARCHIVOS: {len(curso_elegido.archivo)}\n")
                                agregar_archivo = input(" Desea agregar un archivo adjunto? (s/n): ")
                                if agregar_archivo.lower() == 's':
                                    nombre_archivo = input("\tIngrese el nombre del archivo: ")
                                    formato_archivo = input("\tIngrese el formato del archivo: ")
                                    archivo = Archivo(nombre_archivo, formato_archivo)
                                    curso_elegido.NuevoArchivo(archivo)
                                    print("\tArchivo agregado con exito !")
                                else:
                                    print("No se han agregado Archivos ")
                                    break
                            else:
                                print("- Numero no valido")
                        else:
                            print("- Ingrese un numero valido ")
                    else:
                        print("No tiene cursos registrados para gestionar archivos ")                    
    elif opcion == "3":
        orden_curso = sorted(cursos, key=lambda curso: curso.nombreCurso)
        for curso in orden_curso:
            print(f"Materia: {curso.nombreCurso} \t Carrera: {curso.carrera}")
    elif opcion == "4":
        print("Saliendo del sistema")
        break
    else:
        print("Ingrese una opcion valida")

        
        