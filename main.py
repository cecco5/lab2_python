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

#print(r)
#print(r1)
#print(r_list)
#print(r1_list)

# ---------------------------ESERCIZI PER CASA------------------------------#

# Esercizio 1: Scrivi una funzione che prende come parametro la temperatura in gradi Celsius e la trasforma in gradi
# Fahrenheit.
# Cercare su internet come si calcola la conversione da Celsius a Fahrenheit.


def celsius_fahreneit(temp):
    t_f = temp + 32
    return t_f


#tc = int(input("Inserire temperatura in gradi centigradi (°): "))
#tf = celsius_fahreneit(tc)
#print(f"La temperatura equivale a {tf}F.")


# Esercizio 2: Scrivi una funzione che prende tre numeri come parametri e restituisce il più grande tra loro.
# La funzione avrà 3 parametri, occhio!


def massimo(a, b, c):
    if a >= b and a >= c:
        m = a
    elif a <= b and a >= c:
        m = b
    else:
        m = c
    return m


#num1 = int(input("Inserire primo numero: "))
#num2 = int(input("Inserire secondo numero: "))
#num3 = int(input("Inserire terzo numero: "))

#print(f"il massimo tra i tre numeri è: {massimo(num1, num2, num3)}.")


# Esercizio 3: Scrivi una funzione che prenda come parametri le coordinate cartesiane x e y di due punti e calcoli la
# distanza tra i due.
# La funzione avrà 4 paramenti, che potrete chiamare per comodità ax, ay, bx e by.
# Cercare la formula per calcolare la distanza tra due punti cartesiani.

def distanza_2_punti(xa, ya, xb, yb):
    d = sqrt((xa-xb)**2+(ya-yb)**2)
    return d


# Punto A
xa = 2
ya = 2


# Punto B
xb = 2
yb = 4

#print(f"la distanza tra i punti A e B è: {distanza_2_punti(xa, ya, xb, yb)}")


# Esercizio 4: Scrivi un programma che, passata come parametro una lista, calcoli e stampi la radice quadrata di tutti
# gli elementi della lista.
# ricordatevi che il modulo math va sempre alla prima riga del codice!
# Potete usare questa lista: L = [256, 4, 16, 49, 121, 36]

def square_list(l):
    x = 0
    while x < len(l):
        l[x] = (l[x])**2
        x += 1
    return l


def square_list2(l):
    lt = []
    for x in l:
        lt.append(x**2)
    return lt


#L = [256, 4, 16, 49, 121, 36]
#print(square_list2(L))


# Esercizio 5: Date due liste scrivere una funzione che verifichi se i primi elementi delle due liste sono uguali
# (utilizzare indici della lista).
# In questo caso, i due parametri della funzione saranno due liste!
def same_first(l1, l2):
    if l1[0] == l2[0]:
        return True
    return False


#L1 = [256, 4, 16, 49, 121, 36]
#L2 = [25, 3, 1, 4, 11, 6]

#print(same_first(L1, L2))


# Esercizio 6: Scrivi un programma che, passata come parametro una lista di interi, fornisce in output il maggiore
# tra i numeri contenuti nella lista.

def max_list(l):
    ind = 0
    max_prov = l[ind]
    while ind < len(l):
        if l[ind] >= max_prov:
            max_prov = l[ind]
        ind += 1
    return max_prov


L1 = [256, 4, 16, 490, 121, 36]
print(max_list(L1))



























