print("")
print("Alfaro_Ibarra_Sheccid_3w_1171.")
#Preguntar al usuario
nm=input("Coloque su nombre: ")
ed=input("Coloque su edad: ")
dr=input("Coloque su direccion: ")
tf=input("Coloque su numero telefonico: ")
#Crear diccionario con los datos proporcionados
datos={
    "Nombre" : nm,
    "Edad" : ed,
    "Direccion" : dr,
    "Telefono" : tf
}
#Mostrar los datos proporcionados
print(nm, " tiene ", ed, "años, vive en ", dr, " y su telefono es:", tf)
