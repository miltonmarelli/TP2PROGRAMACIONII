def ingresar_como_alumno(estudiantes:list):
    email = input(" \t Ingrese su email: \n")
    estudiante = None
    for alumno in estudiantes:
        if alumno.email == email:
            estudiante = alumno
            break
    if estudiante is not None:
        contrasenia = input(" \t Ingrese su contraseña: \n")
        if estudiante.validar_credenciales(email, contrasenia):
            print(f"\tBienvenido, {estudiante.nombre} {estudiante.apellido}! \n") 
            return estudiante          
        else:
            print("Contraseña incorrecta\n")
    else:
        print("\tAlumno no encontrado, darse de alta en alumnado\n")
                    
                    
def ingresar_como_profesor(profesores:list):
    email = input("\t Ingrese su email: \n")
    profesor = None
    for profe in profesores:
        if profe.email == email:
            profesor = profe
            break
    if profesor is not None:
        contrasenia = input("\tIngrese su contraseña: \n")
        if profesor.validar_credenciales(email, contrasenia):
            print(f"\tBienvenido, Profesor {profesor.nombre} {profesor.apellido}!\n")
            return profesor
        else:
            print("Contraseña incorrecta\n")
           
    else:
        print("\t Profesor no encontrado, darse de alta en alumnado\n")
    
 
     