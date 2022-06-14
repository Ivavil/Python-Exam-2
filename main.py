import csv
def read_data():
    dictionary = {}
    with open('results.json', 'r') as file:
        lista_lineas = file.readlines()
        print("Lista de líneas leídas: ", lista_lineas[1])
        #dictionary.update(lista_lineas[1]) 

    return dictionary

if __name__ == "__main__":
    dic = read_data()
    print(dic)