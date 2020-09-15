import os
import string


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

Scenario4_t = ["ruta", "navegación", "viaje", "destino"]
Scenario4_c = ["Cancela ","Detén ", "Por favor deten ", "Por favor cancela ", "Termina ", "Por favor termina "]

Scenario5_t = ["1235512", "1234", "45633", "54321",]
Scenario5_c = ["Llama al ", "Marca al ", "Por favor marca al ", "Haz una llamada al ", "Por favor llama al ", "Realiza una llamada al "]

Scenario6_t = ["Lucía Naira", "Sofía Idaira", "María Dácil", "Jon Rodriguez",]
Scenario6_c = ["Llama a ", "Marca a ", "Por favor marca a ", "Haz una llamada a ", "Por favor llama a ", "Realiza una llamada a "]

Scenario7_t = ["0", "1", "8", "7"]
Scenario7_c = ["Marca el ", "Marca ", "Por favor marca ", "Presiona el ", "Aprieta el "]
if __name__ == '__main__':
    #write_template("File1.txt", template1, combinations1)
    #write_template("File2.txt", template2, combinations2)
    #write_template("Aeropuerto.txt", template3, combinations2)
    #write_template("Scenario4.txt", Scenario4_t, Scenario4_c)
    #write_template("Scenario5.txt", Scenario5_t, Scenario5_c)
    #write_template("Scenario6.txt", Scenario6_t, Scenario6_c)
    write_template("Scenario7.txt", Scenario7_t, Scenario7_c)
