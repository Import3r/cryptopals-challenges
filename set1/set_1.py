import base64
import string

def hex_to_base64(hex_string):
    raw_data = bytes.fromhex(hex_string)
    base64_result = base64.b64encode(raw_data)
    return base64_result.decode('utf-8')


def fixed_xor(data):
    key = '686974207468652062756c6c277320657965'
    xor_result = int(data, 16) ^ int(key, 16)
    return hex(xor_result)[2:]

def score_englishness(cipher):
    freq = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}
    score = 0
    for letter in cipher:
        freq[letter.upper()] += 1
    cipher_freq = [i[0] for i in sorted(freq.items(), key= lambda x: x[1], reverse=True)]
    for letter in 'ETAOIN':
        if letter in cipher_freq[:7]:
            score += 1
    for letter in 'VKJXQZ':
        if letter in cipher_freq[-6:]:
            score += 1
    return score
    
def xor_strings(string1, string2):
    return ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(string1,string2))

def main():
    user_hex = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'  # input('enter your hex string: ')
    print(xor_strings(bytes.fromhex(user_hex).decode('utf-8'), 'a'))
    # results = sorted(strings.items(), key=lambda x: x[1], reverse=True)

main()
