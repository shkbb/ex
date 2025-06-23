from collections import Counter

def find_duplicates(lst):
    count = Counter(lst)
    return sorted([num for num, freq in count.items() if freq > 1])

input_str = input("Введіть числа через пробіл: ")

numbers = list(map(int, input_str.split()))

result = find_duplicates(numbers)
print("Повторювані елементи:", result)
