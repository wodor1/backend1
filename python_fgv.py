# első feladat


import math


def find_numbers(start=2000, finish=3200, oszthato=7, nem_oszthato=5):
    result = []

    for number in range(start, finish+1):
        if number % oszthato == 0 and number % nem_oszthato != 0:
            result.append(number)

    return result


result = find_numbers()
print(result)

# második feladat


def count_pista(names_list):
    return names_list.count("Pista")


names_list = ['Pista', 'Gabor', 'Pista', 'Gábor', 'István', 'István',
              'László', 'Katalin', 'Katalin', 'Tímea', 'Gábor', 'Pista']
pista_count = count_pista(names_list)
print(pista_count)

# harmadik feladat


def convert_to_number(text):
    try:
        number = int(text)
        return number
    except ValueError:
        print("A megadott érték nem konvertálható egész számmá.")
        return None


def print_hello(count):
    for i in range(1, count + 1):
        print(f"{i}. Helló!")


user_input = input("Kérlek, adj meg egy egész számot: ")
converted_number = convert_to_number(user_input)

if converted_number is not None:
    print_hello(converted_number)

# negyedik feladat


def szamra_alakit(szoveg):
    try:
        szam = int(szoveg)
        return szam
    except ValueError:
        print("A megadott érték nem alakítható át egész számmá.")
        return None


def kor_terulet(sugar):
    return math.pi * sugar ** 2


def kor_kerulete(sugar):
    return 2 * math.pi * sugar


bevitel = input("Kérlek, add meg a kör sugarának egész számát: ")
sugar = szamra_alakit(bevitel)

if sugar is not None:
    terulet = kor_terulet(sugar)
    kerulet = kor_kerulete(sugar)
    print(f"A kör területe: {terulet}")
    print(f"A kör kerülete: {kerulet}")
