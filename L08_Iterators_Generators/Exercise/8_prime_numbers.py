def get_primes(numbers):
    for num in numbers:
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                yield num


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))

# Create a generator function called get_primes() which should receive a list
# of integer numbers and return a list containing only the prime numbers from the initial list.
#
# Output:
# [2, 3, 5]