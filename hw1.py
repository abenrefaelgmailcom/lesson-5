### Exercise 1: Print Stars Recursively
from itertools import count


def print_stars(n):
    if n == 0:
        return
    print('*', end='')
    print_stars(n - 1)
print_stars(5)



### Exercise 2: Count Character in Word

def count_chars(a, chars):
    if len(chars) ==0:
        return 0
    count = 1 if chars[0] == a else 0
    return count + count_chars(a, chars[1:])
print(count_chars('a', 'paper'))

### Exercise 3: Print Digits Forward

def print_digits_forward(num):
    if num < 10:
        print(num, end =' ')
        return
    print_digits_forward(num // 10)
    print(num % 10, end =' ')
print_digits_forward(527)


### Exercise 4: Count Odd Digits

def count_odd_digits(n):
    if n == 0:
        return 0
    digit = n % 10
    is_odd = 1 if digit % 2 == 1 else 0
    return is_odd + count_odd_digits(n // 10)

print(count_odd_digits(1423657966))

### Exercise 5: Reverse Print Word Recursively

def reverse_print(word):
    if len(word) == 0:
        return
    reverse_print(word[1:])
    print(word[0], end='')
reverse_print('code')