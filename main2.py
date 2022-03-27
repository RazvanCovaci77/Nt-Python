# Să se scrie o funcție care primește un număr nedefinit de parametrii și să se calculeze suma parametrilor care reprezintă
# numere întregi sau reale.


def get_v_integer():
        m = 0
        number = None
    while number is None:
        try:
            number = m
        except ValueError:
            return 0
        else:
            return number

def my_sum(num):
    sum= 0

    for i in num:
        if get_v_integer(num):
            sum = sum + i

    return sum

print("Suma parametrilor este:", get_v_integer(1, 5, -3, "abc", [12, 56, "cad"]))


# Să se scrie o funcție recursivă care primește ca parametru un număr întreg și returnează:
# suma tuturor numerelor de la [0, n]

def my_sum_recur(n):
    if n <= 1:
        return n
    else:
        return n + my_sum_recur(n-1)

print('Suma tuturor numerelor de la [0, n] este:',  my_sum_recur(2))

# suma numerelor pare de la [0, n]

def my_sum_recur_par(n):
    if n == 0:
        return 0
    elif n % 2 != 0:
        return my_sum_recur_par(n-1)
    else:
        return n + my_sum_recur_par(n - 1)

print('Suma tuturor numerelor pare de la [0, n] este:',  my_sum_recur_par(7))

# suma numerelor impare de la [0. n]
def my_sum_recur_odd(n):
    if n == 0:
        return 0
    elif n % 2 == 0:
        return my_sum_recur_odd(n-1)
    else:
        return n + my_sum_recur_odd(n - 1)

print('Suma tuturor numerelor impare de la [0, n] este:',  my_sum_recur_odd(7))

#Să se scrie o funcție care citește de la tastatură și returnează valoarea dacă aceasta este un număr întreg, altfel
# returnează valoarea 0.

def get_valid_integer():

    number = None
    while number is None:
        number = input('number= ')
        try:
            number = int(number)
        except ValueError:
            return 0
        else:
            return number

print("Valoarea este:", get_valid_integer())
