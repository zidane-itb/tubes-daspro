import argparse

from data.gameaggr import load_game, list_game_toko
from data.kepemilikanaggr import load_kepemilikan
from data.useraggr import load_user
from front.interaction import register_front, tambah_game_front, login_front, search_my_game_front, \
    search_game_at_store_front, ubah_stok_front, list_game_toko_front


def load(nama_folder, user_id):
    try:
        arr_game = load_game(nama_folder)
        arr_kepemilikan = load_kepemilikan(nama_folder, arr_game, user_id)

    except FileNotFoundError:
        print('')
    return arr_game, arr_kepemilikan


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

    logged_in_arr = login(user_arr)

    loader = load(folder_name, logged_in_arr[0])
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

                pass

            else:

                print('tidak terdaftar sebagai admin')

        elif menu.strip() == 'search_my_game':

            search_arr = search_my_game_front(kepemilikan_arr)

            if not search_arr:
                print('Game tidak ditemukan')

            else:
                print(search_arr)

        elif menu.strip() == 'search_game_at_store':

            search_arr = search_game_at_store_front(game_arr)

            if not search_arr:
                print('Game tidak ditemukan')

            else:
                print(search_arr)

        elif menu.strip() == 'save':

            pass

        elif menu.strip() == 'test':
            pass
        
        elif menu.strip() == 'ubah_stok':
            search_arr = ubah_stok_front(game_arr)
        
        elif menu.strip() == 'list_game_toko':
            search_arr = list_game_toko_front(game_arr)
            print(search_arr)

        elif menu.strip() == 'list_game':
            search_arr = kepemilikan_arr
            if search_arr == []:
                print("Maaf, kamu belum membeli game. Ketik perintah beli_game untuk beli.")
            else:
                print(search_arr)

