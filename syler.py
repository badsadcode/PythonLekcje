# Tom's Random Name Generator
# ---------------------------
# Wczytuje z pliku syl.txt listę sylab. Prosi użytkownika
# o wpisanie ilości sylab w imieniu oraz ilość imion do wygenerowania
# Następnie losuje sylabe z listy i dodaje ją do imienia tyle razy ile imie
# ma mieć sylab. Proste :P
# Na koniec zapisuje imiona do pliku jedno pod drugim. 

import random
fhandle =  open('syl.txt')
lista = []
for li in fhandle:
    li.strip()
    lista.append(li)

ils = input('Podaj ilosc sylab:')
ili = input('Ile chcesz imion wygenerowac?:')
fhandle.close
fahandle = open('imiona.txt','w+')

for d in range(int(ili)):
    imie = ''
    
    for i in range(int(ils)):
        random.seed(random.randrange(12321321421))
        sylaba = random.randrange(len(lista))
        imie = (imie + lista[sylaba].strip())

    print (str(d+1),': Siema! Masz na imie', imie.capitalize())
    
    fahandle.write(imie+'\n')
    
fahandle.close()
                              
    


    
