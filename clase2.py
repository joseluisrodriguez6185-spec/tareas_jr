# type:ignore

carreras = ("Ingeniería de Software", "Contabilidad", "Derecho")

personas = [
    ("Juan", "Pérez", 38, 0),
    ("Carlos", "Santana", 29, 1),
    ("Raúl", "Sosa", 19, 2)
]

estudiantes = []

for _ in range(2):
    # Solicita los datos aquí
    nombre = input("ingrese el nombre: ")
    apellido = input("ingrese el apellido: ")
    edad = int(input("ingrese la edad: "))
    carrera = int(input("ingrese la carrera (0,1 o 2): "))
    
    persona = (nombre, apellido, edad, carrera)
    personas.append(persona)

print("")

for nombre, apellido, edad, carrera in personas:
    nombre_carrera = carreras[carrera]
    
    estudiante = {
        "nombre": nombre,
        "apellido": apellido,
        "edad": edad,
        "carrera": nombre_carrera
    }
    
    estudiantes.append(estudiante)

for estudiante in estudiantes:
    print(
        f"{estudiante['nombre']} {estudiante['apellido']} tiene "
        f"{estudiante['edad']} años y estudia {estudiante['carrera']}"
    )