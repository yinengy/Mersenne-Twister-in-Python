# coefficients for MT19937
(w, n, m, r) = (32, 624, 397, 31)
a = 0x9908B0DF
(u, d) = (11, 0xFFFFFFFF)
(s, b) = (7, 0x9D2C5680)
(t, c) = (15, 0xEFC60000)
l = 18
f = 1812433253

# make a arry to store the state of the generator
MT = [0 for i in range(n)]
index = n+1
lower_mask = int(bin(1 << r),2) - 0b1
upper_mask = int(str(-~lower_mask)[-w:])

# initialize the generator from a seed
def mt_seed(seed):
    global index
    index = n
    MT[0] = seed
    for i in range(1,n):
        temp = f * (MT[i-1]^(MT[i-1] >> (w-2))) + i
        MT[i] = int(str(temp)[-w:])

# Extract a tempered value based on MT[index]
# calling twist() every n numbers
def extract_number():
    global index
    index = 0
    if index >= n:
        if index > n:
            raise RuntimeError('Generator was never seeded')
        twist()

    y = MT[index]
    y =  y ^ ((y >> u) & d)
    y = y ^ ((y << t) & c)
    y = y ^ ((y << s) & b)
    y = y ^ (y >> l)

    index += 1
    return int(str(y)[-w:])

# Generate the next n values from the series x_i 
def twist():
    global index
    for i in range(0,n):
        x = (MT[i] & upper_mask) + (MT[(i+1) % n] & lower_mask)
        xA = x >> 1
        if (x % 2) != 0:
            xA = xA ^ a
        MT[i] = MT[(i + m) % n] ^ xA

    index = 0

def main(seed):
    mt_seed(seed)
    print(extract_number())

main(0)