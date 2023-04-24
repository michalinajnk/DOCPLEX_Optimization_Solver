"""
import math

from docplex.mp.model import Model

n = 6
k = 4
m = Model(name="test")

x = []
for i in range(0,n):
    x.append([m.binary_var(name="x{0}{1}".format(i,j)) for j in range(0,k)])

values = [
[7,2,9,3],
[0,6,7,1],
[4,1,6,3],
[1,4,8,5],
[3,3,9,8],
[3,2,2,2]
];

m.maximize(m.sum(x[i][j]*values[i][j] for i in range(0,n) for j in range(0,k)))

for i in range(0, n):
    m.add_constraint(m.sum(x[i][j] for j in range(0, k)) <= 1)

m.solve(log_output=True)
m.print_solution()
m.print_information()


#2.1 Problem sumy podzbioru (Subset Sum Problem, SSP

#NIE MA OGRANICZEN
# T, var x[], int s[]
#jest albo nie jest 1 lub 0 dla liczby xi
#suma mozliwie bliska do T

 #m.minimize(abs((Suma po od i do n)xi*s1 - T))



#5.1 Problem inspekcji

def_matrix_distances = []

for i in range(0, nOCircles):
    for j in range(0, nOCircles):
        def_matrix_distances.append(math.sqrt(math.pow((points[i][0]-points[j][0], 2)) + math.pow((points[i][1]-points[j][1], 2))))


#n kół
#koło jako trójka -> (ai, bi, ri)
#punkt startowy (x0, y0) ∈ R


#trasa jak najkrotsza (cyklu) n punktow
# n punktow które znajduja sie wewnątrz lub na krawedzi danego okregu



#rozwiazanie to punkty po kolei



#dane
#a[]
#b[]
#r[]

#znajdz X[], Y[]

#FUNKJA CELU
m.minimize(Sum(for i from 0 to n+1) math.sqrt((xi-xi+1)^2 + (yi-yi+1)^2)


#ograniczenia
'''
-wewnatrz koła
dla kazdego i from 1 to n abs(srodek koła(ai) - xi)  <= ri
dla kazdego i from 1 to n abs(srodek koła(bi) - yi)  <= ri

-promien jest wiekszy od 0
dla każdego i from 1 to n r1 > 0

-dane punkty początkowe
x0 =
y0 =
'''

#5.2 Kwadratowe zagadnienie przydziału

#dane:
#wspolrzedne kola i promienie i przepływ macierz NxN (na diagonali zera)
#A[]     B[]            R[]        F[]

#ograniczenia
'''
-wewnatrz koła
dla kazdego i from 1 to n abs(srodek koła(ai) - xi)  <= ri
dla kazdego i from 1 to n abs(srodek koła(bi) - yi)  <= ri

-promien jest wiekszy od 0
dla każdego i from 1 to n r1 > 0
'''

#D[i,j] -> wypełnij
'''
(for i ->n)
    ( for j 0->n)
            d[i,j] =  math.sqrt((x1-x2)^2 + (y1-y2)^2)

macierz nxn odległosci  wartosci to -> math.sqrt((x1-x2)^2 + (y1-y2)^2) -> element to d[i,j]
m.minimize (for i ->n)
                ( for j 0->n)
                    Sum(f[i,j]* D[i,j]))

'''
#szukane to te punkty

# Create decision variables
x = [model.continuous_var(lb=circles[i][0]-circles[i][2], ub=circles[i][0]+circles[i][2], name='x_{}'.format(i))
     for i in range(n)]
y = [model.continuous_var(lb=circles[i][1]-circles[i][2], ub=circles[i][1]+circles[i][2],  name='y_{}'.format(i))
     for i in range(n)]





"""