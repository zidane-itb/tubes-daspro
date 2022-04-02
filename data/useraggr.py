from file.csv import read
from default import liststc
from security.cipher import cipher_string

__csv_header = ['id', 'username', 'nama', 'password', 'role', 'saldo']
__file_name = 'user.csv'
role = ['admin', 'user']
# role: 1 = user, 0 = admin


def login(user_list, username, password):
    for user in user_list:
        if user[1] == username and user[3] == password:
            return True
    return False


def register(user_list, username, nama, password):
    arr_length = liststc.len(user_list)
    password = cipher_string(password)
    arr = [arr_length, username, nama, password, 1, 0]
    return user_list + arr


def load_user(folder_name):
    return read(folder_name, __file_name)

