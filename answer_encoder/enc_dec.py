import string

lowercase_alphabet = list(string.ascii_lowercase)
uppercase_alphabet = list(string.ascii_uppercase)


def clean(num):
    """if number would go out of range, this rotates
    it around to map to value"""
    while num > 25:
        num -= 26
    while num < 0:
        num += 26
    return num


def rotate_alphabet(alphabet, rot):
    rot_alphabet = []
    for i, letter in enumerate(alphabet):
        i += rot
        clean_i = clean(i)
        rot_alphabet.append(alphabet[clean_i])
    return rot_alphabet


def gen_encode_decode_dicts(alphabet, rot):
    # clean up and translate rot_numbers
    encode_dict = {}
    decode_dict = {}
    for k, v in zip(alphabet, rotate_alphabet(alphabet, rot)):
        encode_dict[k] = v
        decode_dict[v] = k
    return encode_dict, decode_dict


def prep(rot_number):
    lower_encode, lower_decode = gen_encode_decode_dicts(lowercase_alphabet, rot_number)
    upper_encode, upper_decode = gen_encode_decode_dicts(uppercase_alphabet, rot_number)
    return lower_encode, upper_encode, lower_decode, upper_decode


def encode(s, rot_number=13):
    encode_lower_dict, encode_upper_dict, na, nb = prep(rot_number)
    s_list = list(s)
    encode_list = []
    for character in s_list:
        if character in encode_lower_dict:
            encode_list.append(encode_lower_dict[character])
            continue
        if character in encode_upper_dict:
            encode_list.append(encode_upper_dict[character])
            continue
        encode_list.append(character)
    return "".join(encode_list)


def decode(s, rot_number=13):
    na, nb, decode_lower_dict, decode_upper_dict = prep(rot_number)
    s_list = list(s)
    decode_list = []
    for character in s_list:
        if character in decode_lower_dict:
            decode_list.append(decode_lower_dict[character])
            continue
        if character in decode_upper_dict:
            decode_list.append(decode_upper_dict[character])
            continue
        decode_list.append(character)
    return "".join(decode_list)


def main():
    test_string = "I like cats."
    encoded_test = encode(test_string, 13)
    print(f"{encoded_test = }")
    decoded_test = decode(encoded_test, 13)
    print(f"{decoded_test = }")


if __name__ == "__main__":
    main()
