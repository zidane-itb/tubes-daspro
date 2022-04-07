from file.csv import read, write
from default import liststc
from security.cipher import cipher_string

__csv_header = ['id', 'username', 'nama', 'password', 'role', 'saldo']
__file_name = 'user.csv'
__role = ['admin', 'user']


# role: 1 = user, 0 = admin


def login(user_list, username, password):
    for i, user in enumerate(user_list):
        if user[1] == username and user[3] == password:
            return i
    return -1


def register(user_list, username, nama, password):
    for user in user_list:
        if username == user[1]:
            return []

    # length of array untuk menentukan id akun baru
    arr_length = liststc.len(user_list)

    # password with caesar cipher algorithm
    password = cipher_string(password)

    # add account to array
    arr = [arr_length, username, nama, password, 1, 0]

    return user_list + arr


def load_user(folder_name):
    return read(folder_name, __file_name)


def save_user(user_list, folder_name):
    return write(__csv_header, user_list, folder_name, __file_name)
