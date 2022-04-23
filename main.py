import argparse

from data.gameaggr import load_game,buy_game
from data.kepemilikanaggr import load_kepemilikan, load_kepemilikan_full
from data.useraggr import load_user, topup
from data.riwayataggr import load_riwayat
from front.interaction import register_front, login_front, search_my_game_front, \
    search_game_at_store_front, ubah_stok_front, list_game_toko_front, tambah_game_front, ubah_game_front, help_front, \
    save_front, exit_front


def load(nama_folder, user_id):
    arr_game = load_game(nama_folder)
    arr_kepemilikan = load_kepemilikan(nama_folder, arr_game, user_id)
    arr_kepemilikan_full = load_kepemilikan_full(nama_folder)
    arr_riwayat = load_riwayat(nama_folder)

    return arr_game, arr_kepemilikan, arr_kepemilikan_full, arr_riwayat


def get_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("param")

    args = parser.parse_args()

    return args.param


def login(user_arr):
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

    user_arr = load_user(folder_name)

    print('Selamat datang! Silahkan login terlebih dahulu')

    # F03
    logged_in_arr = login(user_arr)

    loader = load(folder_name, logged_in_arr[0])
    game_arr = loader[0]
    kepemilikan_arr = loader[1]
    kepemilikan_full = loader[2]
    riwayat_arr = loader[3]

    while True:
        menu = input('>>> ')

        # F02
        if menu.strip() == 'register':

            if logged_in_arr[4] == '0':

                user_arr = register_front(user_arr)

            else:

                print('tidak terdaftar sebagai admin')

        # F04
        elif menu.strip() == 'tambah_game':

            if logged_in_arr[4] == '0':

                arr = tambah_game_front(game_arr)

                game_arr = arr

            else:

                print('tidak terdaftar sebagai admin')

        # F05
        elif menu.strip() == 'ubah_game':

            if logged_in_arr[4] == '0':

                arr = ubah_game_front(game_arr)

                if arr:
                    game_arr = arr

                    print(game_arr)

                if not arr:
                    pass

            else:

                print('tidak terdaftar sebagai admin')

        # F06
        elif menu.strip() == 'ubah_stok':

            if logged_in_arr[4] == '0':

                search_arr = ubah_stok_front(game_arr)
                game_arr = search_arr

                print(search_arr)

            else:

                print('tidak terdaftar sebagai admin')

        # F07
        elif menu.strip() == 'list_game_toko':
            search_arr = list_game_toko_front(game_arr)
            print(search_arr)

        # F08
        elif menu.strip() == 'buy_game':
            tup = buy_game(game_arr, kepemilikan_arr, kepemilikan_full, riwayat_arr, logged_in_arr[0], user_arr)

            if tup:

                game_arr = tup[0]
                kepemilikan_arr = tup[1]
                kepemilikan_full = tup[2]
                riwayat_arr = tup[3]
                user_arr = tup[4]

            else:
                pass

        # F09
        elif menu.strip() == 'list_game':
            search_arr = kepemilikan_arr
            if not search_arr:
                print("Maaf, kamu belum membeli game. Ketik perintah beli_game untuk beli.")
            else:
                print(search_arr)

        # F10
        elif menu.strip() == 'search_my_game':

            search_arr = search_my_game_front(kepemilikan_arr)

            if not search_arr:
                print('Game tidak ditemukan')

            else:
                print(search_arr)

        # F11
        elif menu.strip() == 'search_game_at_store':

            search_arr = search_game_at_store_front(game_arr)

            if not search_arr:
                print('Game tidak ditemukan')

            else:
                print(search_arr)

        # F12
        elif menu.strip() == 'topup':
            arr = topup(user_arr)

            if arr:
                user_arr = arr

            else:
                pass

        # F13
        elif menu.strip() == 'riwayat':
            print(kepemilikan_arr)

        # F14
        elif menu.strip() == 'help':
            help_front(logged_in_arr[4])

        # F16
        elif menu.strip() == 'save':
            save_front()

        elif menu.strip() == 'exit':
            exit_front(user_arr, game_arr, riwayat_arr, kepemilikan_full)
