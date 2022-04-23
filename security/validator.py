from default.liststc import length

def validate(dtype, obj):
    return True if type(obj) == dtype else False


def validate_register(username):
    for i in range(length(username)):

        if not __validate_register_char(username[i]):

            return False

    return True


def __validate_register_char(char):
    ascii_usr = ord(char)

    if not (65 <= ascii_usr <= 90 or 97 <= ascii_usr <= 122 or
            ascii_usr == 45 or ascii_usr == 95 or 0 <= ascii_usr <= 9):

        return False

    else:

        return True

def validate_game_id(game_id):
    if not game_id[0] == 'G' or game_id[1] == 'A' or game_id[2] == 'M' or game_id[3] == 'E':

        return False

    else:
        try:
            game_id[5] = int(game_id[5])
            game_id[6] = int(game_id[6])
            game_id[7] = int(game_id[7])

        except ValueError:

            return False

    return True