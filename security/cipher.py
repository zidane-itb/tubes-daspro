from default.liststc import length

__k = 3


def __get_ciphered_char(p: str):

    # cek apakah char merupakan sebuah alfabet
    if 97 <= ord(p) <= 122 or 65 <= ord(p) <= 90:

        # cek apakah char merupakan huruf kapital
        is_upper_case = p.isupper()

        # merubah char menjadi huruf kecil
        p = p.lower()

        # integer starting lowercase alphabet di format ascii
        starting = 97

        # lower = 97 122 upper = 65 90

        # proses cipher
        p_p = abs(ord(p) - ord('a'))
        num_p = (p_p + __k) % 26
        final_num = starting + num_p

        # return berdasarkan apakah huruf tersebut awalnya uppercase atau bukan
        return chr(final_num).upper() if is_upper_case else chr(final_num)

    # jika char bukan merupakan alfabet, return char yang sama
    else:
        return p


# loop through string menggunakan fungsi get_ciphered_char
def cipher_string(text: str):
    final_text = ""

    for i in range(length(text)):
        final_text += __get_ciphered_char(text[i])

    return final_text
