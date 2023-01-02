import random
import string
lower_cases =  string.ascii_lowercase
upper_cases = string.ascii_uppercase
nums = string.digits
special = string.punctuation

def password_generator():
    lower= ''.join(random.choice(lower_cases) for i in range(6))
    upper= ''.join(random.choice(upper_cases) for j in range(6))
    numbers = ''.join(random.choice(nums) for k in range(6))
    symbols = ''.join(random.choice(special) for m in range(6))
    results = lower+upper+numbers+symbols
    final = ''.join(random.choice(results) for x in range(12))
    print(final)


password_generator()
