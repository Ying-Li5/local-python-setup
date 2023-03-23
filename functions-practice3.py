# name_args - Accepts any number of named arguments and prints them in the pattern key : value one at a time.
def name_args(*args):
    for a in args.key():
        print(f"{a}:{args[a]}")

name_args(name="Alax", animal='dog', breed="corgi", age=5)

# all_true - Returns True if all the elements in an iterable are true. Hint: there is an existing built-in function that could be very helpful here.
def all_true(iterable):
    return all(iterable)

print(all_true([True, True, True]))
print(all_true([True, False]))

# one_true - Returns True if one of the elements in an iterable is true. Hint: there is an existing built-in function that could be very helpful here.
def one_true(iterable):
    return(iterable)

print(one_true([True, True, True]))
print(one_true([False, False, False]))
print(one_true([True, False]))

# recursive_factorial - Uses recursion to find the factorial of an integer.
def recursive_factorial(n):
    if n <= 1:
        return 1
    else:
        return n * recursive_factorial(n-1)
    
print(recursive_factorial(5))
print(recursive_factorial(10))

# recursive_deduplicate - Recursively removes all adjacent duplicate letters from a string.
    # Input: AABBCCDD
    # Output: ABCD
def recursive_deduplicate(corgi, i=0):
    if len(corgi) <= 1 or i == len(corgi)-1:
        return corgi
    else:
        if corgi[i] == corgi [i+1]:
            return recursive_deduplicate(corgi[0:i]+corgi[i+1:], i)
        else:
            return recursive_deduplicate(corgi, i+1)
        
print(recursive_deduplicate("aaaa"))
print(recursive_deduplicate("aaba"))
print(recursive_deduplicate("apple"))
print(recursive_deduplicate(""))
      
# recursive_reverse - Uses recursion to reverse a string.
def recursive_reverse(corgi, i=0):
  if len(corgi)==0:
    return ""
  elif i == len(corgi)-1:
    return corgi[0]
  else:
    return corgi[-1-i] + recursive_reverse(corgi, i+1)

print(recursive_reverse("aaaa"))
print(recursive_reverse("aaba"))
print(recursive_reverse("apple"))
print(recursive_reverse(""))