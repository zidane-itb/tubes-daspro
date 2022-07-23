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
        arr = [arr_length + 1, username, nama, password, 1, 0]

        return add_list(user_list, arr)

    else:

        return []


def cek_user(user, user_arr):
    for u in range(length(user_arr) - 1):
        if user_arr[u][1] == user:
            return u
    return -1


def topup(user_arr):
    InpUser = input("Masukkan username: ")
    InpSaldo = int(input("Masukkan saldo: "))

    index = cek_user(InpUser, user_arr)

    if index == -1:
        print('Username "'+InpUser+'"tidak ditemukan.')
        
        return []

    if (user_arr[index][5] + InpSaldo) < 0:
        print("Masukan tidak valid.")

    else:
        user_arr[index][5] += InpSaldo
        print('Top Up berhasil! Saldo "'+InpUser+'" bertambah menjadi', user_arr[index][5])
        
        return user_arr

    return []


# load dari user.csv ke memory
def load_user(folder_name, url_file):
    return read(folder_name=folder_name, file_name=__file_name, type_arr=[str, str, str, str, str, float], url_file=url_file)


# save dari memory ke user.csv
def save_user(user_list, folder_name, url_file):
    return write(__csv_header, user_list, folder_name, __file_name, url_file=url_file)
