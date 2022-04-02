__k = 3


def __get_ciphered_char(p: str):
    if 97 <= ord(p) <= 122 or 65 <= ord(p) <= 90:
        is_upper_case = p.isupper()
        p = p.lower()
        starting = 97

        # lower = 97 122 upper = 65 90

        p_p = abs(ord(p) - ord('a'))
        num_p = (p_p + __k) % 26

        final_num = starting + num_p

        return chr(final_num).upper() if is_upper_case else chr(final_num)
    else:
        return p


def cipher_string(text: str):
    final_text = ""

    for i in text:
        final_text += __get_ciphered_char(i)

    return final_text
