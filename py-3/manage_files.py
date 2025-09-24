import os
from pathlib import Path

# open()
# Retorna un objeto de archivo.
# r (read): Permite leer un archivo. (Este puede ser omitido, se asume que siempre sera r)
# w (write): Se sobreescribe el archivo. (Reemplaza todo el contenido anterior; si no existe el archivo lo crea)
# a (append): Agrega datos al final.
# a+ (append + read): Agrega datos al final y los puede leer.

def read_doc(path, *, mode, enc):
    if not path:
        return
    
    try:
        # Path(__file__)
        # Retorna la url absoluta del archivo que se esta ejecutando.
        # .parent: retorna la ruta padre.
        current_path = Path(__file__).parent
        full_path = current_path / path

        # Cuando se utiliza with no es extrictamente necesario utilizar el bloque try except.
        # Nota: si no se utiliza with se debe utilizar file.close().
        with open(full_path, mode, encoding=enc) as file:
            data = file.read()
            return data
    except FileNotFoundError:
        return "El archivo no se encontro."
    
# print(read_doc("test-folder/document.html", mode="r", enc="utf-8"))

def add_new_text(file_path, content):
    with open(file_path, 'a+', encoding="utf-8") as f:
        f.write(content)
        # seek()
        # Permite mover el puntero del archivo
        # 0: inicio del archivo | 1: current pointer | 2: final del archivo
        f.seek(0)
        print(f.read())

article_path = Path(__file__).parent / 'test-folder/article-1.txt'
add_new_text(article_path, '\nLo mismo pasa cuando desarrollamos aplicaciones con Javascript ya sea vainilla o en con algún framework/librería; casi siempre existirán tareas que deban ejecutarse en segundo plano para que la aplicación que desarrollamos no “espere” a que termine un proceso demasiado tardado. \nSi se ejecutara un programa con el comportamiento natural de javascript (línea por línea) a una gran cantidad de aplicaciones les afectaría en su rendimiento y como repercusión los usuarios lo terminarían pagando al esperar una cantidad de tiempo ridícula para poder utilizar ciertas partes de una aplicación.\n')

# os.path.exists(path)
# Verifica si existe un folder.
is_exist_folder = lambda path_folder: os.path.exists(path_folder)

def generate_files(content_files):
    if len(content_files) == 0:
        return
    
    try:
        path = Path(__file__).parent / "test-folder/files"

        if not is_exist_folder(path):
            # os.mkdir(path)
            # Crea carpetas dentro del OS.
            os.mkdir(path)

        new_file = None

        for i, content in enumerate(content_files):
            if not isinstance(content, str):
                continue

            if len(content) < 1:
                continue

            new_file = open(f"{path}/archive-{i}.txt", "w")
            new_file.write(content)

    except FileNotFoundError:
        print('El archivo no existe.')
    finally:
        new_file.close()
        print("Los archivos se generaron con exito")

generate_files(["Texto número 11", "", 12.3, "Python + Javascript <3", "AEJ", 1, "", None, "Nuevo texto"])