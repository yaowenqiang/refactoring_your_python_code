def fizzbuzz(number):
    if number % 15 == 0:
        return "FizzBuzz"
    if number % 3 == 0:
        return "Fizz"
    if number % 5 == 0:
        return 'Buzz'
    return str(number)

def fizzbuzz_v2(number):
    result = ''
    if number % 3 == 0:
        result += "Fizz"
    if number % 5 == 0:
        result += "Buzz"
    if result == '':
        result = str(number)
    return result

def fizzbuzz_v3(number):
    value = str()
    if number % 3 == 0:
        value += "Fizz"
    if number % 5 == 0:
        value += "Buzz"
    return value or str(number)

def divisible_by_5(number):
    return number % 5 == 0
    
def divisible_by_3(number):
    return number % 3 == 0

def fizzbuzz_v4(number):
    if divisible_by_3(number) and divisible_by_5(number):
        return "FizzBuzz"
    if divisible_by_3(number):
        return "Fizz"
    if divisible_by_5(number):
        return "Buzz"
    return str(number)

def fizzbuzz_v4(number):
    if number % 3 == 0 and number % 5 == 0: return "FizzBuzz"
    if number % 3 == 0: return "Fizz"
    if number % 5 == 0: return "Buzz"
    return str(number)

def fizzbuzz_v5(number):
    fb_dict = {3:'Fizz', 5:'Buzz'}
    result = str()
    for key in fb_dict:
        if number % key == 0:
            result += fb_dict[key]
    return result or str(number)

def fizzbuzz_v6(number):
    substitutions = [(3, 'Fizz'), (5, 'Buzz')]
    return [''.join(s for d, s in  substitutions if number % d == 0) or str(x) for x in range(1, number + 1)]

def fizzbuzz_v7(number):
    fb_dict = {3:'Fizz', 5:'Buzz'}
    result = str()
    for key ,value in fb_dict.items():
        if number % key == 0:
            result += value
    return result or str(number)