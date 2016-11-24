""""The following program is a look a recursive fucntions"""

#the sum of the numbers n
def sum(n):
    if(n ==1):
        return 1
    else:
        return n + sum(n-1)

def factorial(n):
    if(n ==1):
        return 1
    else:
        return n* factorial(n-1)

def fibonaci(n):
    if n ==0 or n == 1:
        return 1
    else:
        return fibonaci(n-1) + fibonaci(n-2)

def number(n):
    if n <= 0:
        return 0
    else:
        return 3 + number(n-1)

def numbers(a,b):
    if a == 0 or b == 0:
        return 0
    else:

        return numbers(a,b-1) + a

# def power(base,exp):
#     if base == 0 or exp == 0:
#         return 0
#     else:
#         pass
#         return power(base**(exp -1), exp) * exp


def palindrome(word):
    if word[0] == word[-1]:
        return palindrome(word[1,-2])
    else:
        return False

print(factorial(5))
print(sum(5))
print(fibonaci(23))
print(number(10))
print(numbers(10,50))
# print(power(2,2))
word = "navan"
# print(palindrome(word))
