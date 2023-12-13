def print_row(n, count):
    print(" " * (n - count), end="")
    print("* " * count)


def print_triangle(n):
    for row in range(1, n + 1):
        print_row(n, row)


def print_reverse_triangle(n):
    for row in range(n - 1, 0, -1):
        print_row(n, row)


def create_rhombus(n):
    print_triangle(n)
    print_reverse_triangle(n)


n = int(input())

create_rhombus(n)

#       Variant 2      #
# for row in range(1,n + 1):
#     print(" " * (n - row) + "* " * row)
#
# for row in range(n - 1, 0, -1):
#     print(" " * (n - row) + "* " * row)

#       Variant 3      #
# for row in range(1,n + 1):
#     print(" " * (n - row), end="")
#     print(*['*'] * row)
#
# for row in range(n - 1, 0, -1):
#     print(" " * (n - row), end="")
#     print(*['*'] * row)


# Create a program that reads a positive integer N as input and
# prints on the console a rhombus with size n:

# Input:
#   3
# Output:
#      *
#     * *
#    * * *
#     * *
#      *
