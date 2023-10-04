
def read_file() -> str:
    f = open('/home/rai/Documents/github-projects/dam2-m15-uf1/data/paraules.csv', 'r')
    row2 = f.readline()
    row2 = f.readline()
    words_row2 = row2.split(',')
    return words_row2[2]

def create_dict() ->  dict:
    cat_esp = {'gat' : 'gato', 'llum' : 'luz', 'mar' : 'mar', 'arbre' : 'árbol', 'llibre' : 'libro'}
    return cat_esp

paraula_cat = read_file() # llibre
diccionari = create_dict()

paraula_esp = diccionari[paraula_cat]

print(paraula_esp)

