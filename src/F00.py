from datetime import datetime
import os

# Membuat fungsi generator bilangan acak kongruensial linier (LCG)
def generate_random(seed=None):
    modulus = 2147483647  # Bilangan prima terbesar yang dapat diwakili dalam bilangan 32-bit
    multiplier = 16807    # Multiplier yang relatif prima dengan modulus
    increment = 0         # Increment dapat diabaikan karena tidak terlalu mempengaruhi kualitas bilangan acak
    if seed is None:
        seed = datetime.now().microsecond + os.getpid()
    next_value = (multiplier * seed + increment) % modulus
    return next_value

# Fungsi untuk menghasilkan bilangan acak dalam rentang tertentu
def random_number(range_of_random=None):
    next_value = generate_random()  
    modulus = 2147483647
    if range_of_random is not None:
        min_range, max_range = range_of_random
        next_value = (next_value / modulus) * (max_range - min_range) + min_range
    return int(next_value)

# contoh aplikasi
print(random_number([1,100]))
#11
#47
#72
#24
#9
#45
#89
#56
