from datetime import datetime
import os

# Membuat fungsi generator bilangan acak kongruensial linier (LCG)
def generate_random(seed=None):
    modulus = 2147483647  # Bilangan prima terbesar yang dapat diwakili dalam bilangan 32-bit
    multiplier = 16807    # Multiplier yang relatif prima dengan modulus
    increment = 0         # Increment dapat diabaikan karena tidak terlalu mempengaruhi kualitas bilangan acak
    if seed is None:
        seed = datetime.now().microsecond + os.getpid()
    while True:
        next_value = (multiplier * seed + increment) % modulus
        yield next_value
        seed = next_value
# Fungsi untuk menghasilkan bilangan acak dalam rentang tertentu atau tanpa rentang
def random_number(range_of_random=None):
    rng = generate_random()
    modulus = 2147483647
    if range_of_random is not None:
        min_range, max_range = range_of_random
        next_value = (next(rng) / modulus) * (max_range - min_range) + min_range
    else:
        next_value = next(rng)
    return int(next_value)
    
def random_number_arr(range_of_random=None, n=1):
    rng = generate_random()  # Menggunakan generator untuk rng
    modulus = 2147483647
    result = []
    if range_of_random is not None:
        min_range, max_range = range_of_random
        for _ in range(n):
            next_value = (next(rng) / modulus) * (max_range - min_range) + min_range
            result.append(int(next_value))
    else:
        for _ in range(n):
            result.append(next(rng))
    return result

# Contoh penggunaan
#n = 3  # Panjang array yang diinginkan
#print(random_number_arr([0,5], n))
#[1, 1, 4]

# contoh aplikasi
#print(random_number([1,100]))
#11
#47
#72
#24
#9
#45
#89
#56
