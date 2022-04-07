from data.useraggr import load_user, login, register
from data.gameaggr import load_game, search_game_by_id_tahun
import argparse


def load(nama_folder):
    arr_user = load_user(nama_folder)
    arr_game = load_game(nama_folder)
    return arr_user, arr_game


def get_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("param")

    args = parser.parse_args()

    return args.param


if __name__ == '__main__':
    folder_name = get_args()

    loader = load(folder_name)

    user_arr = loader[0]
    game_arr = loader[1]
    riwayat_arr = None

    logged_in_arr = []

    while True:
        menu = input('>>> ')

        if menu.strip() == 'login':

            username = input('username: ')
            password = input('password: ')

            index = login(user_arr, username, password)

            if index == -1:
                print('username atau password salah')
            else:
                logged_in_arr = user_arr[index]

        elif menu.strip() == 'register':
            if not logged_in_arr:
                print('Login terlebih dahulu')
            else:
                if logged_in_arr[4] == '0':
                    nama = input('Masukkan nama: ')
                    username = input('Masukkan username: ')
                    password = input('Masukkan password: ')

                    arr = register(user_arr, username, nama, password)

                    if not arr:
                        print('Username', username, 'sudah terpakai, silakan menggunakan username lain')
                    else:
                        print('Username', username, 'telah berhasil register ke dalam "Binomo"')
                        user_arr = arr
                else:
                    print('tidak terdaftar sebagai admin')

        elif menu.strip() == 'search_my_game':
            if not logged_in_arr:
                print('Login terlebih dahulu')
            else:
                game_id = input('Masukkan ID Game: ')
                tahun_rilis = input('Masukkan tahun rilis game: ')

                game_id = None if game_id.strip() == '' else game_id
                tahun_rilis = None if tahun_rilis.strip() == '' else tahun_rilis

                try:
                    tahun_rilis = int(tahun_rilis)

                    arr = search_game_by_id_tahun(game_arr, game_id, tahun_rilis)

                    print(arr)

                except ValueError:
                    print('Tahun rilis tidak valid')

