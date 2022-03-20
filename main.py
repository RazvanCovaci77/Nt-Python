# declară o listă care conține elementele 7, 8, 9, 2, 3, 1, 4, 10, 5, 6 (în această ordine).
my_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]

# afișează lista inițială ordonată ascendent (lista inițială trebuie păstrată în aceeași formă)
# Varianta 1
my_list_asc = sorted(my_list)
print('Lista ordonata ascendent', my_list_asc)

# Varianta 2
asc = my_list
asc.sort()
print('Lista ordonata ascendent ', asc)

# afișează lista inițială ordonată descendent (lista inițială trebuie păstrată în aceeași formă)
rev = asc
rev.reverse()
print('Lista ordonata descendent ', rev)

# afișează o listă ce conține numerele pare din lista ordonată (folosind slice)
my_list_even = my_list_asc[1::2]
print('Lista ce contine numerele pare din lista ordonata crescator', my_list_even)

# afișează o listă ce conține numerele impare din lista ordonată (folosind slice)
my_list_odd = my_list_asc[::2]
print('Lista ce contine numerele impare din lista ordonata crescator', my_list_odd)

# afisează o listă ce conține numerele ce sunt multipli ai numărului 3 (folosind slice)
triple = my_list_asc[2::3]
print('Lista cu multiplii ai numarului 3 este', triple)