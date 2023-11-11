import math

gyumolcsok = ['alma', 'körte', 'ananász', 'kiwi']

gyumolcsok.sort()


def kiiras():
    for i in range(4):
        print(gyumolcsok[i])


def korkerulet(r):
    return 2 * r * math.pi


def korterulet(r):
    return r * r * math.pi


kiiras()
print(korkerulet(5))
print(korterulet(5))
