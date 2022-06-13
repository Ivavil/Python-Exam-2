import random
import re

def choose_secret():
    """Dado un nombre de fichero, esta función devuelve una palabra aleatoria de este fichero transformada a mayúsculas.
    Args:
      filename: El nombre del fichero. Ej. "palabras_reduced.txt"
    Returns:
      secret: Palabra elegida aleatoriamente del fichero transformada a mayúsculas. Ej. "CREMA"
    """
    f = open("palabras_reduced.txt", mode="rt", encoding="utf-8")

    lista_lineas = f.readlines()
    print("Lista de líneas leídas: ", lista_lineas)
    indice = int(random.random() * len(lista_lineas))
    print(lista_lineas[indice])
    secret = str(lista_lineas[indice])

    f.close()

    return secret.upper()
    
def compare_words():
    """Dadas dos palabras en mayúsculas (word y secret), esta función calcula las posiciones de las letras de word que aparecen en la misma posición en secret, y las posiciones de las letras de word que aparecen en secret pero en una posición distinta.
    Args:
      word: Una palabra. Ej. "CAMPO"
      secret: Una palabra. Ej. "CREMA"
    Returns:
      same_position: Lista de posiciones de word cuyas letras coinciden en la misma posición en secret. En el caso anterior: [0]
      same_letter: Lista de posiciones de word cuyas letras están en secret pero en posiciones distintas. En el caso anterior: [1,2]
    """
    #word = word.upper()
    same_letter = []
    same_position = []
    for i in range(5):
      if word[i].upper() == secret[i]:
        same_position.append(i)
      elif secret.count(word[i].upper()) > 0:
        same_letter.append(i)

    print(same_position)
    print(same_letter)

    return same_position, same_letter

def print_word():
    """Dada una palabra, una lista same_position y otra lista same_letter, esta función creará un string donde aparezcan en mayúsculas las letras de la palabra que ocupen las posiciones de same_position, en minúsculas las letras de la palabra que ocupen las posiciones de same_letter y un guión (-) en el resto de posiciones
    Args:
      word: Una palabra. Ej. "CAMPO"
      same_letter_position: Lista de posiciones. Ej. [0]
      same_letter: Lista de posiciones. Ej. [1,2]
    Returns:
      transformed: La palabra aplicando las transformaciones. En el caso anterior: "Cam--"
    """
    transformed = ""
    for i in range(5):
      if same_position.count(i) > 0:
        transformed = transformed + str(word[i].upper())
      elif same_letter.count(i) > 0:
        transformed = transformed + str(word[i].lower()) 
      else:
        transformed = transformed + "-"

      print(word + " " + secret)

    return transformed

    
def choose_secret_advanced():
    """Dado un nombre de fichero, esta función filtra solo las palabras de 5 letras que no tienen acentos (á,é,í,ó,ú). De estas palabras, la función devuelve una lista de 15 aleatorias no repetidas y una de estas 15, se selecciona aleatoriamente como palabra secret.
    Args:
      filename: El nombre del fichero. Ej. "palabras_extended.txt"
    Returns:
      selected: Lista de 15 palabras aleatorias no repetidas que tienen 5 letras y no tienen acentos
      secret: Palabra elegida aleatoriamente de la lista de 15 seleccionadas transformada a mayúsculas
    """
    lista_palabras_filtradas = []
    f = open("palabras_extended.txt", mode="rt", encoding="utf-8")

    lista_lineas = f.readlines()

    if len(lista_lineas) == 0:
      raise ValueError("La posición está fuera de rango")

    for i in range(len(lista_lineas)):
      x = re.findall("[a-zA-Z]", lista_lineas[i])
      if len(lista_lineas[i]) == 6  and len(lista_lineas[i]) == (len(x) + 1):
        lista_palabras_filtradas.append(lista_lineas[i][0:5])

    indice = int(random.random() * len(lista_palabras_filtradas))
    secret = str(lista_palabras_filtradas[indice])

    selected = []
    while len(selected) < 15:
      indice = int(random.random() * len(lista_palabras_filtradas))
      if(selected.count(lista_palabras_filtradas[indice]) == 0):
        selected.append(lista_palabras_filtradas[indice])

    print(selected)

    f.close()

    return selected, secret.upper() 
 
def check_valid_word():
    """Dada una lista de palabras, esta función pregunta al usuario que introduzca una palabra hasta que introduzca una que esté en la lista. Esta palabra es la que devolverá la función.
    Args:
      selected: Lista de palabras.
    Returns:
      word: Palabra introducida por el usuario que está en la lista.
    """


if __name__ == "__main__":
    try:
      selected, secret=choose_secret_advanced()
      print("Palabra a adivinar: "+secret)#Debug: esto es para que sepas la palabra que debes adivinar
      for repeticiones in range(0,6):
          word = input("Introduce una nueva palabra: ").upper()
          same_position, same_letter = compare_words()
          resultado=print_word()
          print(resultado)
          if word == secret:
              print("HAS GANADO!!")
              exit()
      print("LO SIENTO, NO LA HAS ADIVINIDADO. LA PALABRA ERA "+secret)   
    except ValueError:
      print("Error leyendo los datos")
