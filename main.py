# esempi lezione 1 e lezione 2
# ----- import -----
# import math
from math import *
from random import *
# --- (6) Operazioni matematiche: libreria math
''' spiegare queste differenze 
1) import math -> così importo tutti i metodi all'interno di math, ma devo richiamare
               SEMPRE la libreria math nel codice... (math.pi, math.radq ecc ecc...)
2) from math import * -> così importo tutti i metodi all'interno di math, ma NON devo richiamare
                      la libreria math nel codice... (pi, radq ecc ecc...)
3) from math import pi -> così importo solo il metodo 'pi' (e ovviamente non devo richiamare math nel codice)

print(math.pi) -> si usa nel caso 1
print(pi) -> si usa ne caso 2 e 3

'''

a1 = pi/2  # 90 ° in radianti
s1 = int(sin(a1))
c1 = int(cos(a1))

# come calcolo il seno di altri angoli noti?
# seni, coseni, conversione radianti/gradi e viceversa -> funz degrees() e radians()

a2 = pi
s2 = int(sin(a2))
c2 = int(cos(a2))

a3 = (3/2)*pi
s3 = int(sin(a3))
c3 = int(cos(s3))

#print(f"Seni -> {degrees(a1)}°= {s1}, {degrees(a2)}°= {s2}, {degrees(a3)}°= {s3}")
#print(f"Coseni ->  {degrees(a1)}°= {c1}, {degrees(a2)}°= {c2}, {degrees(a3)}°= {c3}")

# --- (7) FUNZIONI pt. 1---
'''
Le funzioni sono uno strumento che ci permette di raggruppare un insieme di istruzioni
che eseguono un compito specifico. Le funzioni accettano in input 0 o più argomenti (o parametri),
li elaborano, e restituiscono in output un risultato.'''


def stampa(a):  # parametri e variabili
    # indentazione
    return a


# --- main ---       ...aneddoto carino su quando andavo io alle superiori...
parola = 'scolapasta'  # variabili locali e globali, quale è la differenza?

# print(stampa(parola))
# print('La parola del giorno è "{}"'.format(parola))
# print('Puoi prestarmi lo {} per favore?'.format(parola))

# con step over mostra tutti i passaggi per fargli vedere come funziona l'assegnazione delle variabili

# e se usassi print al posto di return?


def somma(x, y):
    s = x + y
    return s


#primo_num = int(input('Inserire primo numero: '))
#secondo_num = int(input('Inserire secondo numero: '))


#print(somma(primo_num, secondo_num))
#print(f"{primo_num} + {secondo_num} = {somma(primo_num, secondo_num)}")

def area_rettangolo(b, h):
    area = b*h
    return area


def perimetro_rettangolo(b, h):
    perimetro = b*2 + h*2
    return perimetro


#base = int(input('Inserire la base del rettangolo: '))
#altezza = int(input("Inserire l'altezza del rettangolo: "))
#area = area_rettangolo(base, altezza)
#perimetro = perimetro_rettangolo(base, altezza)

#print(f"il rettangolo di base: {base} e altezza: {altezza} ha un perimetro pari a {perimetro} e area {area}.")


# --- (8) Esecuzione condizionale: if, elif, else ---
# Nuovi operatori matematici >, < e  ==

# Funzione che mi stampa il valore numerico maggiore
# e se i numeri sono uguale mi restituisce 'False'.
# Interessante che in python la funzione può ritornare alternativamente tipi diversi (int e bool in questo caso)


def num_max(a, b):
    if a > b:
        return a
    elif b > a:
        return b
    elif a == b:
        return False


num1 = 3
num2 = 3

# print(num_max(num1, num2))

# Iterazione e ricorsione:
'''
La ricorsione e l'iterazione eseguono ripetutamente il set di istruzioni.
La ricorsione è quando un'istruzione in una funzione si chiama ripetutamente.
L'iterazione avviene quando un loop viene ripetutamente eseguito fino a quando
la condizione di controllo diventa falsa.
Un algoritmo Iterativo userà dichiarazioni cicliche come cicli for o while
per ripetere gli stessi passaggi. Un algoritmo ricorsivo è una funzione che richiama
sé stessa fin quando la condizione base non viene soddisfatta
'''

# ricorsione


def conto_alla_rovescia_ricorsivo(n):
    if n == 0:
        print('Fine conto alla rovescia!')
    else:
        print(n)
        conto_alla_rovescia_ricorsivo(n-1)  # l'algoritmo richiama se stesso...


#  print(conto_alla_rovescia_ricorsivo(10))

# ciclo while
def conto_alla_rovescia_iterativo(n):
    while n > 0:
        print(n)
        n = n - 1  # si può scrivere anche n -= 1
    print('Fine conto alla rovescia!')


#  print(conto_alla_rovescia_iterativo(10))

# usando range()
# ciclo for e range()
def conto_alla_rovescia_for():
    cont = range(0, 11)
    for i in cont:
        print(i)

'''In matematica, si definisce fattoriale di un numero naturale n, indicato con n!,
il prodotto dei numeri interi positivi minori o uguali a tale numero.'''


def fatt(n):  # ricorsivo
    # è più intuitiva ed elegante
    if n == 0:
        return 1
    else:
        return n*fatt(n-1)


def fatt_iter(n):  # iterativo
    res = 1
    for i in range(1, n+1):
        res *= i
    return res

# Le Liste:


L = ['patate', 'carciofi', 'broccoletti', 'fagioli']

# print(L, type(L), len(L))

# Da tipo range() a tipo lista:
r = range(20)
r1 = range(0, 55, 5)
r_list = list(r)
r1_list = list(r1)

print(r)
print(r1)
print(r_list)
print(r1_list)



