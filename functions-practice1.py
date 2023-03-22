# arb_args - Takes in any number of arguments and prints them one at a time.
def arb_args (*arg):
    for a in args:
        print(a)

# inner_func - Takes in two integers. Two nested functions should perform separate, distinct math operations using the integers. 
# The result of both nested functions should then be added together and printed.
def inner_func (x, y):
    def int_1():
        return x+y
    def int_2():
        return x-y
    print(int_1()+int_2())

# lunch_lady - Takes in two strings: a student's name and their lunch preference. The function should print both strings. If a 
# lunch preference is not given, "Mystery Meat" should be printed instead.
def lunch_lady (student_name, lunch_preference="Mystery Meat"):
    print(student_name, lunch_preference) 

# sum_n_product - Accepts two integers and returns both the sum and the product.
def sum_n_product (int1, int2):
    return int1+int2, int1*int2

# alias_arb_args - Should be arb_args but assigned an alias. Remember, variables can hold functions in Python just like they can in JS. 
# Alternatively, you can call a function from inside another function.
alias_arb_args = arb_args

# arb_mean - Accepts any number of integers and prints their average.
def arb_mean (*args):
    total = 0
    for a in args:
        total += a
    print(a/len(args))

# arb_longest_string - Accepts any number of strings and returns the longest one.
def arb_longest_string (*args):
    long = 0
    longest = ""
    for a in args:
        if len(a) > long:
            long = len(a)
            longest = a
    return longest