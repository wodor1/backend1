def find_numbers(start=2000, finish=3200, oszthato=7, nem_oszthato=5):
    result = []

    for number in range(start, finish+1):
        if number % oszthato == 0 and number % nem_oszthato != 0:
            result.append(number)

    return result


result = find_numbers()
print(result)
