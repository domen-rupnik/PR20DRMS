from csv import DictReader
import operator
import matplotlib.pyplot as plt

starost_vozil = dict()

for i in range(1,13):
    for j in range(2015,2020):
        file = 'podatki/Podatki_{:02d}'.format(i) + str(j) + '.csv'
        podatki = DictReader(open(file, 'rt', encoding='ANSI'), delimiter=';')

        if j not in starost_vozil:
            starost_vozil[j] = {'novo': 0, 'mlajse' : 0, 'starejse': 0}

        for row in podatki:
            if '5A-Leto izdelave' in row and str(row['Status vozila (opis)']) == 'registrirano' and row['5A-Leto izdelave'] is not None:
                try:
                    leto_izdelave = int(row['5A-Leto izdelave'])
                    if j == leto_izdelave:
                        starost_vozil[j]['novo'] += 1
                    elif (j - leto_izdelave) <= 5:
                        starost_vozil[j]['mlajse'] += 1
                    else:
                        starost_vozil[j]['starejse'] += 1
                except:
                    #Napaka v podatkih
                    None

leta = list(starost_vozil.keys())
nova = [j['novo'] for i, j in starost_vozil.items()]
mlajsa = [j['mlajse'] for i, j in starost_vozil.items()]
starejsa = [j['starejse'] for i, j in starost_vozil.items()]

plt.bar([i-0.2 for i in leta], nova, width=0.2, color='lightgreen', align='center', label='Nova')
plt.bar(leta, mlajsa, width=0.2, color='orange', align='center', label='5 let stara')
plt.bar([i+0.2 for i in leta], starejsa, width=0.2, color='r', align='center', label='Starejša')
plt.xlabel('Leta')
plt.ylabel('Število registriranih vozil')
plt.legend(loc=2)
plt.show()

