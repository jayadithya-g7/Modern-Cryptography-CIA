# Initial Permutation Table
IP = [
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9, 1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7
]

# Final Permutation Table
FP = [
    40, 8, 48, 16, 56, 24, 64, 32,
    39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30,
    37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28,
    35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26,
    33, 1, 41, 9, 49, 17, 57, 25
]

# Expansion table
E = [
    32, 1, 2, 3, 4, 5, 4, 5,
    6, 7, 8, 9, 8, 9, 10, 11,
    12, 13, 12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21, 20, 21,
    22, 23, 24, 25, 24, 25, 26, 27,
    28, 29, 28, 29, 30, 31, 32, 1
]

# S-Boxes
S_boxes = [
    # S1
    [
        [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
        [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
    ],
    # S2
    [
        [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
        [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
        [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
        [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
    ],
    # S3
    [
        [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
        [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
        [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
        [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
    ],
    # S4
    [
        [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
        [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
        [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
        [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
    ],
    # S5
    [
        [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
        [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
        [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
        [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
    ],
    # S6
    [
        [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
        [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
        [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
        [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
    ],
    # S7
    [
        [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
        [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
        [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
        [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
    ],
    # S8
    [
        [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
        [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
        [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
        [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
    ]
]

# Permutation table
P = [
    16, 7, 20, 21,
    29, 12, 28, 17,
    1, 15, 23, 26,
    5, 18, 31, 10,
    2, 8, 24, 14,
    32, 27, 3, 9,
    19, 13, 30, 6,
    22, 11, 4, 25
]

# PC-1 table (Key Permutation)
PC1 = [
    57, 49, 41, 33, 25, 17, 9,
    1, 58, 50, 42, 34, 26, 18,
    10, 2, 59, 51, 43, 35, 27,
    19, 11, 3, 60, 52, 44, 36,
    63, 55, 47, 39, 31, 23, 15,
    7, 62, 54, 46, 38, 30, 22,
    14, 6, 61, 53, 45, 37, 29,
    21, 13, 5, 28, 20, 12, 4
]

# PC-2 table (Key Permutation)
PC2 = [
    14, 17, 11, 24, 1, 5,
    3, 28, 15, 6, 21, 10,
    23, 19, 12, 4, 26, 8,
    16, 7, 27, 20, 13, 2,
    41, 52, 31, 37, 47, 55,
    30, 40, 51, 45, 33, 48,
    44, 49, 39, 56, 34, 53,
    46, 42, 50, 36, 29, 32
]

# Left Rotations
SHIFT = [
    1, 1, 2, 2, 2, 2, 2, 2,
    1, 2, 2, 2, 2, 2, 2, 1
]

def left_shift(key, shift):
    return key[shift:] + key[:shift]

def key_schedule(key):
    key = permute(key, PC1, 56)
    left_half = key[:28]
    right_half = key[28:]
    round_keys = []
    
    for shift in SHIFT:
        left_half = left_shift(left_half, shift)
        right_half = left_shift(right_half, shift)
        combined_key = left_half + right_half
        round_key = permute(combined_key, PC2, 48)
        round_keys.append(round_key)
    
    return round_keys

def permute(block, table, n):
    return ''.join(block[i - 1] for i in table[:n])

def xor(block1, block2):
    return ''.join(str(int(b1) ^ int(b2)) for b1, b2 in zip(block1, block2))

def sbox_substitution(block):
    sub_blocks = [block[i:i + 6] for i in range(0, len(block), 6)]
    result = ''
    for i, sub_block in enumerate(sub_blocks):
        row = int(sub_block[0] + sub_block[-1], 2)
        col = int(sub_block[1:5], 2)
        sbox_val = S_boxes[i][row][col]
        result += f'{sbox_val:04b}'
    return result

def des_function(right, key):
    expanded_right = permute(right, E, 48)
    xored_right = xor(expanded_right, key)
    substituted = sbox_substitution(xored_right)
    permuted = permute(substituted, P, 32)
    return permuted

def des_encrypt(block, round_keys):
    block = permute(block, IP, 64)
    left, right = block[:32], block[32:]
    
    for i in range(16):
        new_right = xor(left, des_function(right, round_keys[i]))
        left, right = right, new_right
    
    combined_block = right + left
    cipher_block = permute(combined_block, FP, 64)
    return cipher_block

def des_decrypt(block, round_keys):
    block = permute(block, IP, 64)
    left, right = block[:32], block[32:]
    
    for i in range(15, -1, -1):
        new_right = xor(left, des_function(right, round_keys[i]))
        left, right = right, new_right
    
    combined_block = right + left
    plain_block = permute(combined_block, FP, 64)
    return plain_block

def triple_des_encrypt(block, key1, key2, key3=None):
    if key3 is None:
        key3 = key1  # If 3rd key not there, DES-112
    
    round_keys1 = key_schedule(key1)
    round_keys2 = key_schedule(key2)
    round_keys3 = key_schedule(key3)
    
    block = des_encrypt(block, round_keys1)
    block = des_decrypt(block, round_keys2)
    block = des_encrypt(block, round_keys3)
    
    return block

def triple_des_decrypt(block, key1, key2, key3=None):
    if key3 is None:
        key3 = key1  # If 3rd key not there, DES-112
    
    round_keys1 = key_schedule(key1)
    round_keys2 = key_schedule(key2)
    round_keys3 = key_schedule(key3)
    
    block = des_decrypt(block, round_keys3)
    block = des_encrypt(block, round_keys2)
    block = des_decrypt(block, round_keys1)
    
    return block

plaintext = '0123456789ABCDEF'  # 64-bit block
key = '133457799BBCDFF1'  # 56-bit key

# Convert hex to binary
plaintext_bin = bin(int(plaintext, 16))[2:].zfill(64)
key_bin = bin(int(key, 16))[2:].zfill(64)

round_keys = key_schedule(key_bin)

ciphertext = des_encrypt(plaintext_bin, round_keys)
decrypted = des_decrypt(ciphertext, round_keys)

print(f'Ciphertext: {hex(int(ciphertext, 2))[2:].upper()}')
print(f'Decrypted: {hex(int(decrypted, 2))[2:].upper()}')

# Triple DES (DES-168)
key1 = '0123456789ABCDEF'
key2 = '23456789ABCDEF01'
key3 = '3456789ABCDEF012'

key1_bin = bin(int(key1, 16))[2:].zfill(64)
key2_bin = bin(int(key2, 16))[2:].zfill(64)
key3_bin = bin(int(key3, 16))[2:].zfill(64)

triple_ciphertext = triple_des_encrypt(plaintext_bin, key1_bin, key2_bin, key3_bin)
triple_decrypted = triple_des_decrypt(triple_ciphertext, key1_bin, key2_bin, key3_bin)

print(f'Triple DES Ciphertext: {hex(int(triple_ciphertext, 2))[2:].upper()}')
print(f'Triple DES Decrypted: {hex(int(triple_decrypted, 2))[2:].upper()}')
