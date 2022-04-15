from file.csv import read, write
from default.liststc import length, add_list
from security.cipher import cipher_string
from security.validator import validate_register

__csv_header = ['id', 'username', 'nama', 'password', 'role', 'saldo']
__file_name = 'user.csv'
__role = ['admin', 'user']


# role: 1 = user, 0 = admin


def login(user_list, username, password):

    # loop through user_list untuk mencari user dengan username dan password sesuai parameter fungsi
    for i in range(length(user_list)):

        # user found, return index user di array user
        if user_list[i][1] == username and user_list[i][3] == cipher_string(password):

            return i

    # user not found, return -1
    return -1


def register(user_list, username, nama, password):
    if validate_register(username):

        # check apakah ada user yang sudah terdaftar dengan username yang sama dengan parameter fungsi
        for i in range(length(user_list)):

            # user found, return array kosong
            if username == user_list[i][1]:

                return []

        # length of array untuk menentukan id akun baru
        arr_length = length(user_list)

        # password with caesar cipher algorithm
        password = cipher_string(password)

        # add account to array
        arr = [arr_length, username, nama, password, 1, 0]

        return add_list(user_list, arr)

    else:

        return []


def load_user(folder_name):
    return read(folder_name, __file_name)


def save_user(user_list, folder_name):
    return write(__csv_header, user_list, folder_name, __file_name)
