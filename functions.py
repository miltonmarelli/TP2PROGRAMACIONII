from Profesor import Profesor

def ingresar_como_alumno(estudiantes:list):
    email = input(" \t Ingrese su email: \n")
    estudiante = None
    for alumno in estudiantes:
        if alumno.email == email:
            estudiante = alumno
            break
    if estudiante is not None:
        contrasenia = input(" \t Ingrese su contraseña: \n")
        if estudiante.validar_credenciales(email, contrasenia) is True:
            print(f"\tBienvenido {estudiante.nombre} {estudiante.apellido}! \n") 
            return estudiante          
        else:
            print("Contraseña incorrecta\n")
    else:
        print("\tAlumno no encontrado, darse de alta en alumnado\n")
                    
admin = "admin123" #codigo para registrar alta de profesores                   
def ingresar_como_profesor(profesores:list):
    email = input("\t Ingrese su email: \n")
    profesor = None
    for profe in profesores:
        if profe.email == email:
            profesor = profe
            break
    if profesor is not None:
        contrasenia = input("\tIngrese su contraseña: \n")
        if profesor.validar_credenciales(email, contrasenia) is True:
            print(f"\tBienvenido Profesor {profesor.nombre} {profesor.apellido}!\n")
            return profesor
        else:
            print("Contraseña incorrecta\n")           
    else:
        print("Profesor no encontrado")
        registro = input("\t Desea darse de alta? (S/N): ")
        if registro.lower() == 's':
            admin_ingresado = input("\tIngrese el código admin para darse de alta como profesor: ")
            if admin_ingresado == admin:
                nombre = input("\tIngrese su nombre: ")
                apellido = input("\tIngrese su apellido: ")
                email = input("\tIngrese su nuevo email: ")
                contrasenia = input("\tIngrese su nueva contraseña: ")
                titulo = input("\tIngrese el titulo que posee: ")
                anio_egreso = input("\t Ingrese su año de egreso: ")

                profesor = Profesor(nombre, apellido, email, contrasenia, titulo, anio_egreso)
                profesores.append(profesor)
                print("\tProfesor dado de alta exitosamente!")
                print(f"\tBienvenido Profesor {profesor.nombre } { profesor.apellido }!")
            else:
                print("\t Codigo admin incorrecto")
        else:
            print("\tNo se ha registrado como profesor.")
        
    
 
     