import base64

def hex_to_base64(hex_string):
    raw_data = bytes.fromhex(hex_string)
    base64_result = base64.b64encode(raw_data)
    return base64_result.decode('utf-8')


def main():
    hex_input = input('hex: ')
    print('base64: ' + hex_to_base64(hex_input))

main()
