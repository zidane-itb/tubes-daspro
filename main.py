from data.useraggr import load_user
from data.gameaggr import load_game
from front.interaction import register_front, tambah_game_front, login_front, search_my_game_front
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

    print('loading...')

    loader = load(folder_name)

    print('Selamat datang!')

    user_arr = loader[0]
    game_arr = loader[1]
    riwayat_arr = None

    logged_in_arr = []

    while True:
        menu = input('>>> ')

        if menu.strip() == 'login':

            if not logged_in_arr:

                logged_in_arr = login_front(user_arr)

            else:

                print('sudah login')

        else:

            if not logged_in_arr:

                print('login terlebih dahulu')

            else:
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

                    # harusnya disini berisi array dengan game milik user (perlu koreksi)
                    search_arr = search_my_game_front(game_arr)

                    if not search_arr:
                        print('Game tidak ditemukan')

                    else:
                        # display array
                        pass
