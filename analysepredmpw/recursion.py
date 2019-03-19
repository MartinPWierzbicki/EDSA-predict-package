def sum_array(array):

    '''Return sum of all items in array'''
    ##More docstring and error handling to follow
    n = len(array)-1
    if n == 0:
        return array[n]
    else:
        return array[n] + sum_array(array[:n])



def fibonacci(n):

    '''Return nth term in fibonacci sequence'''
    ##More docstring and error handling to follow
    if n <= 1:
        return n

    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def factorial(n):

    '''Return n!'''
    ##More docstring and error handling to follow
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)


def reverse(word):

    '''Return word in reverse'''
    ##More docstring and error handling to follow
    n = len(word)-1
    if n == 0:
        return word[n]
    else:
        return word[n] + reverse(word[:n])
