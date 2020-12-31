import base64

def hex_to_base64(hex_string):
    raw_data = bytes.fromhex(hex_string)
    base64_result = base64.b64encode(raw_data)
    return base64_result.decode('utf-8')


def fixed_xor(data):
    key = '686974207468652062756c6c277320657965'
    xor_result = int(data, 16) ^ int(key, 16)
    return hex(xor_result)[2:]


def main():
    secret_data = input('enter data: ')
    print('result in hex: ' + fixed_xor(secret_data))


main()
