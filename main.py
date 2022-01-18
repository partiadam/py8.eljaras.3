'''
3. Feladat
Írj eljárást, amely paraméterül kapott 2 számot összehasonlít, és a képernyőre kiírja, melyik a nagyobb szám! Kezeld azt az esetet is, ha a két szám egyenlő!
'''

def osszehasonlit(szam1, szam2):
    if szam1 > szam2:
        print(f'A nagyobb szám: {szam1}')
    if szam1 < szam2:
        print(f'A kisebb szám: {szam1}')
    if szam1 == szam2:
        print('A két szám egyenlő.')

osszehasonlit(2,2)
