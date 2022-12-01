from random import choices

usuarios = {
        "super_root": {
            "nombre": "Root",
            "apellido": "Root",
            "password": "0000"
    },
        "carlos": {
            "nombre": "Carlos",
            "apellido": "Fernandez",
            "password": "654321"
    },
        "jose": {
            "nombre": "Jose",
            "apellido": "Ramirez",
            "password": "123456"
    }
 }

pregunta, dato = choices(list(usuarios["super_root"].items()), k=1)[0]
print(f"tu pregunta es: {pregunta} y el valor es: {dato}")
respuesta = input("Cual es la respuesta?: ")

if respuesta == dato:
    print('Pasa')
elif respuesta != dato:
    print('falla')

