def validate(dtype, obj):
    return True if type(obj) == dtype else False


def validate_register(username):
    for char in username:

        if not __validate_register_char(char):

            return False

    return True


def __validate_register_char(char):
    ascii_usr = ord(char)

    if not (65 <= ascii_usr <= 90 or 97 <= ascii_usr <= 122 or
            ascii_usr == 45 or ascii_usr == 95 or 0 <= ascii_usr <= 9):

        return False

    else:

        return True
