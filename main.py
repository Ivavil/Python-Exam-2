import csv
def read_data():
    dictionary = {}
    with open('results.json', 'r') as file:
        lista_lineas = file.read()
        dictionary = lista_lineas

    return dictionary

#def get_name_description(key, dictionary):
    #print(dictionary["name"])
    #print(dictionary["description"])

if __name__ == "__main__":
    dic = read_data()
    print(type(dic))
    #get_name_description(1020, dic)
   