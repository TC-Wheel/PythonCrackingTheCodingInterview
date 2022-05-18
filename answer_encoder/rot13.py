def gen_encode_decode_dicts(s, rot_number=13):
    import string

    # clean up and translate rot_numbers
    def clean(num):
        """if number would go out of range, this rotates
        it around to map to value"""
        while num > 25:
            num -= 26
        while num < 0:
            num += 26
        return num

    lowercase_alphabet = list(string.ascii_lowercase)
    uppercase_alphabet = list(string.ascii_uppercase)

    def rotate_alphabet(rot=clean(rot_number)):
        rot_alphabet = []
        for i, letter in enumerate(lowercase_alphabet):
            i += rot
            clean_i = clean(i)
            rot_alphabet.append(lowercase_alphabet[clean_i])
        return rot_alphabet

    encode_dict = {}
    decode_dict = {}
    for k, v in zip(lowercase_alphabet, rotate_alphabet()):
        encode_dict[k] = v
        decode_dict[k] = v

    return encode_dict, decode_dict


def encode(s, rot_number=13):
    """"""
    encode_dict, decode_dict = gen_encode_decode_dicts(s, rot_number)
    s_list = list(s)
    encoded_list = []
    for letter in s_list:
        if letter in encode_dict:
            encoded_list.append(encode_dict[letter])
            continue
        if letter not in encode_dict and letter.lower() not in encode_dict:
            encoded_list.append(letter)
            continue
        # all that's left is the captial letters
        else:
            encoded_list.append(letter.upper())
    return "".join(encoded_list)


def decode(s, rot_number=13):
    """"""
    encode_dict, decode_dict = gen_encode_decode_dicts(s, rot_number)
    s_list = list(s)
    decoded_list = []
    for letter in s_list:
        if letter in decode_dict:
            decoded_list.append(decode_dict[letter])
            continue
        if letter not in decode_dict and letter.lower() not in decode_dict:
            decoded_list.append(letter)
            continue
        # all that's left is the captial letters
        else:
            decoded_list.append(letter.upper())
    return "".join(decoded_list)


def main():
    string_to_encode = "NO! Don't kill him!"
    encoded_string = encode(string_to_encode)
    decoded_string = decode(encoded_string)
    print(f"{encoded_string = }")
    print(f"{decoded_string = }")


if __name__ == "__main__":
    main()
