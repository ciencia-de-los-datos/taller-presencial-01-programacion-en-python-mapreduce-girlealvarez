#
# Escriba la función load_input que recive como parámetro un folder y retorna
# una lista de tuplas donde el primer elemento de cada tupla es el nombre del
# archivo y el segundo es una línea del archivo. La función convierte a tuplas
# todas las lineas de cada uno de los archivos. La función es genérica y debe
# leer todos los archivos de folder entregado como parámetro.
#
# Por ejemplo:
#   [
#     ('text0'.txt', 'Analytics is the discovery, inter ...'),
#     ('text0'.txt', 'in data. Especially valuable in ar...').
#     ...
#     ('text2.txt'. 'hypotheses.')
#   ]
#
import glob
import fileinput
import os.path # permite hacer operaciones de archivos

def load_input(input_directory): #lee archivos y devuelve una lista de tuplas con el nombre del archivo y contenido del archivo
    sequence = []
    filenames = glob.glob(input_directory + "/*")  #"/*" muestra todo lo que hay en la carpeta input
    with fileinput.input(files=filenames) as f: #abre archivos de la lista filenames
        for line in f: # f variable con la que se puede iterar todos los archivos
            sequence.append((fileinput.filename(), line)) #por cada iteracion se agrega una tupla a la lista
    return sequence

# Otra forma de leer los archivos
# def load_input(input_directory): # leer archivos en una carpeta

#     dir_path = input_directory + "/*.txt"
#     filenames = glob.glob(dir_path) 

#     sequence = []
#     with fileinput.input(files=filenames) as file:
#         for line in file:
#             tupla = (fileinput.filename(), line)
#             sequence.append(tupla)
#     return(sequence)

# load_input ("input")

#filenames = load_input("input")
#print(filenames)
#print (filenames[1]) #imprime el archivo solo con la primera línea
    
# Escriba una función llamada maper que recibe una lista de tuplas de la
# función anterior y retorna una lista de tuplas (clave, valor). En este caso,
# la clave es cada palabra y el valor es 1, puesto que se está realizando un
# conteo.
#   [
#     ('Analytics', 1), #Lista clave-valor. La clave es la palabra y el valor siempre es 1
#     ('is', 1),
#     ...
#   ]

def mapper(sequence): #mapper convierte el contenido del archivo en una secuencia de palabras con sus ocurrencias
    new_sequence = []
    for _, text in sequence: #El guion bajo _ se utiliza para ignorar la primera parte de la tupla, que es el nombre del archivo, text contiene el contenido del archivo
        words = text.split() #Divide el contenidio del archivo (text) en palabras utilizando split
        for word in words: # Itera sobre todas las palabras en words
            word = word.replace (",","") # Quita comas
            word = word.replace (".","") # Quita puntos
            word = word.lower() # Deja todas las palabras en minúsculas
            new_sequence.append((word,1)) #El 1 es la ocurrencia de la palabra
    return new_sequence

#Otra forma de hacer el mapper
# def mapper (sequence):

#     new_sequence = []
#     for _, text in sequence:
#         for word in text.split():
#             tupla = (word, 1)
#             new_sequence.append(tupla)
#     return new_sequence      


#sequence = load_input("input")
#sequence = mapper(sequence)
#print (sequence)

# Escriba la función shuffle_and_sort que recibe la lista de tuplas entregada
# por el mapper, y retorna una lista con el mismo contenido ordenado por la
# clave.
#   [
#     ('Analytics', 1),
#     ('Analytics', 1),
#     ...
#   ]
def shuffle_and_sort(sequence): #Ordena la secuencia de las palabras en orden alfabético
    sorted_sequence= sorted(sequence, key=lambda x:x[0]) # X:X[0] extrae la primera letra de la palabara. 
    #La secuencia se ordena según la primera letra de la palabra
    #key paráametro que le pasa una función que retorna el elemento por el cual se hace el ordenamiento
    #que es la primera parte de la tupla que es la palabra
    return sorted_sequence

# sequence= load_input("input")
# sequence= mapper(sequence)
# sequence= shuffle_and_sort(sequence)
#print(sequence)

#
# Escriba la función reducer, la cual recibe el resultado de shuffle_and_sort y
# reduce los valores asociados a cada clave sumandolos. Como resultado, por
# ejemplo, la reducción indica cuantas veces aparece la palabra analytics en el
# texto.
#
def reducer(sequence): 

    diccionario={}
    # for key, value in sequence: 
    #     #print(key, "-->", value)
    #     if key not in diccionario.keys(): # devuelve todas las claves del diccionario pero con not in el diccionario debe estar vacio
    #         diccionario[key] = []
    #     diccionario[key].append(value)
    # #print(diccionario)
        
    # new_sequence = []
    # for key, value in diccionario.items():
    #     tupla = (key, sum(value))
    #     new_sequence.append(tupla)
    # return new_sequence

    for key, value in sequence:
        if key not in diccionario.keys():
            diccionario[key] = 0  # En vez de arrancar con una lista, se empieza con cero
        diccionario[key] += value
    
    new_sequence = []
    for key, value in diccionario.items():
        tupla = (key, value)
        new_sequence.append(tupla)
    
    return new_sequence

# sequence = load_input("input")
# sequence= mapper(sequence)
# sequence = shuffle_and_sort(sequence)
# sequence =reducer(sequence)
# print (sequence)


#
# Escriba la función create_ouptput_directory que recibe un nombre de directorio
# y lo crea. Si el directorio existe, la función falla.
#

def create_output_directory(output_directory):
    
    if os.path.exists(output_directory):
        raise FileExistsError (f"The directory,'{output_directory}' alredy exist.") 
    os.makedirs(output_directory)

# sequence = load_input("input")
# sequence= mapper(sequence)
# sequence = shuffle_and_sort(sequence)
# sequence =reducer(sequence)
# create_ouptput_directory("ouput")


#
# Escriba la función save_output, la cual almacena en un archivo de texto llamado
# part-00000 el resultado del reducer. El archivo debe ser guardado en el
# directorio entregado como parámetro, y que se creo en el paso anterior.
# Adicionalmente, el archivo debe contener una tupla por línea, donde el primer
# elemento es la clave y el segundo el valor. Los elementos de la tupla están
# separados por un tabulador.
#
def save_output(output_directory, sequence):
    with open(output_directory + "/part-0000","w") as file:
        for key, value in sequence:
            file.write(f"{key}\t{value}\n")

# sequence = load_input("input")
# sequence= mapper(sequence)
# sequence = shuffle_and_sort(sequence)
# sequence =reducer(sequence)
# create_output_directory("output")
# save_output("output",sequence)


#
# La siguiente función crea un archivo llamado _SUCCESS en el directorio
# entregado como parámetro.
#
def create_marker(output_directory):
    with open (output_directory + "/_SUCCESS","w") as file:
        file.write ("")

# sequence = load_input("input")
# sequence= mapper(sequence)
# sequence = shuffle_and_sort(sequence)
# sequence =reducer(sequence)
# create_output_directory("output")
# save_output("output",sequence)
# create_marker("output")
#
# Escriba la función job, la cual orquesta las funciones anteriores.
#
def job(input_directory, output_directory):
    sequence = load_input(input_directory)
    sequence= mapper(sequence)
    sequence = shuffle_and_sort(sequence)
    sequence =reducer(sequence)
    create_output_directory(output_directory)
    save_output(output_directory,sequence)
    create_marker(output_directory)


if __name__ == "__main__":
     job(
         "input",
         "output",
     )
