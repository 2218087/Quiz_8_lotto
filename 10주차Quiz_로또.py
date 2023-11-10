import random

def generate_lotto_numbers():
    lotto_numbers = []

    while len(lotto_numbers) < 6:
        number = random.randint(1, 45)
        if number in lotto_numbers:
            print("로또번호에 해당 숫자가 있습니다.")
        if number not in lotto_numbers:
            print("로또번호에 해당 숫자가 없습니다.")
            lotto_numbers.append(number)

    lotto_numbers.sort()
    return lotto_numbers


generated_numbers = generate_lotto_numbers()
print("로또번호:", generated_numbers)
