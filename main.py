import argparse

from data.gameaggr import load_game
from data.kepemilikanaggr import load_kepemilikan
from data.useraggr import load_user
from front.interaction import register_front, tambah_game_front, login_front, search_my_game_front


def load(nama_folder, user_id):
    arr_game = load_game(nama_folder)
    arr_kepemilikan = load_kepemilikan(nama_folder, arr_game, user_id)
    return arr_game, arr_kepemilikan


def get_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("param")

    args = parser.parse_args()

    return args.param


def login():
    arr = []
    while True:
        if not arr:
            arr = login_front(user_arr)
        else:
            break

    return arr


if __name__ == '__main__':
    folder_name = get_args()

    print('loading...')

    loader = load(folder_name)

    print('Selamat datang! Silahkan login terlebih dahulu')

    user_arr = load_user(folder_name)

    logged_in_arr = login()

    game_arr = loader[0]
    kepemilikan_arr = loader[1]

    while True:
        menu = input('>>> ')

        if menu.strip() == 'register':

            if logged_in_arr[4] == '0':

                user_arr = register_front(user_arr)

            else:

                print('tidak terdaftar sebagai admin')

        elif menu.strip() == 'tambah_game':

            if logged_in_arr[4] == '0':

                game_arr = tambah_game_front()

            else:

                print('tidak terdaftar sebagai admin')

        elif menu.strip() == 'search_my_game':

            search_arr = search_my_game_front(kepemilikan_arr)

            if not search_arr:
                print('Game tidak ditemukan')

            else:
                # display array
                pass
