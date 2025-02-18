def print_hello():
    """This is a comment that describes the function"""
    print("Hello!")

print_hello()

def print_number(my_number):
    print(f"My number is {my_number}.")

n1 = 2
n2 = 6
n3 = 9
n4 = 11
n5 = 14

print_number(n2)
print_number(n1)
print_number(n3)
print_number(n4)
print_number(n5)

def add_numbers(n1, n2):
    sum = n1 + n2
    return(sum)

sum1 = add_numbers(93, 777)
print(add_numbers(10, 303))
add_numbers(77, 829)
print(add_numbers(-5, -77))

def main():
    my_sum = add_numbers(34, 46)
    print(my_sum)
    print(add_numbers(2, 6))
    print(add_numbers(-4,-7))