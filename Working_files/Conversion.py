import os
import string

def check_file(file):
    with open(file) as file: #with (name, "w") as new_file:
        check = []
        for line in file:
            message = line.split()
            message = "".join(message) + ".wav"
            if message in check:
                i = message.find(".")
                x = message[i-1]
                if x.isnumeric():
                    x = int(x)
                    x += 1
                    message = message[:i] + str(x) + message[i:]
                else:
                    message = message[:i] + "1" + message[i:]
            check.append(message)
            print(message)#new_file.write(message)
#check_file("Work.txt")




def write_template(name, templates, combinations):
    with open(name, "w") as options:
        for template in templates:
            for combination in combinations:
                options.write(f"{combination}{template}\n")


template1 = ["Casa",
"Guardería",
"Escuela",
"Estación de tren",
"Biblioteca",
"Casa de la abuela"
]

template2 = [
"Trabajo",
"Lab ciento veintiseis",
"Aeropuerto de la ciudad de Mexico",
"Parque",
"Castillo de Chapultepec"
]

template3 = ["Aeropuerto"]

combinations1 = ["Llevame a la ", "Dame la dirección de la ", "Por favor llevame a la ",  "Obten direcciones para la ", "Por favor dame la dirección de la ", "Vamos hacia la ", "Yo quiero ir la ", "Me gustaría ir para la ", "Obten la dirección la ",  "Por favor llevame para la ", "Necesito que me lleves a la ", "Quiero la dirección de la ", "Llevame hacia el " ]
combinations2 = ["Llevame al ", "Dame la dirección del ", "Por favor llevame al ", "Obten direcciones para el ", "Por favor dame la dirección del ", "Vamos hacia el ", "Yo quiero ir al ", "Me gustaría ir para el ", "Obten la dirección del ", "Por favor llevame para el ", "Necesito que me lleves al ", "Quiero la dirección del ", "Llevame hacia el " ]
extra = ["Cancela la ruta", "Cancela el viaje", "Cancela la navegación", "Cancela el viaje", "Cancelar ruta"]
if __name__ == '__main__':
    check_file("File1.txt")
