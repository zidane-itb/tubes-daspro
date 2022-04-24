import argparse
import sys

from data.gameaggr import load_game,buy_game
from data.kepemilikanaggr import load_kepemilikan, load_kepemilikan_full
from data.useraggr import load_user, topup
from data.riwayataggr import load_riwayat
from front.interaction import register_front, login_front, search_my_game_front, \
    search_game_at_store_front, ubah_stok_front, list_game_toko_front, tambah_game_front, ubah_game_front, help_front, \
    save_front, exit_front
from file.magicconchshell import kerangajaib
from default.liststc import print_format


def load(nama_folder, user_id, url_file):
    arr_game = load_game(folder_name=nama_folder, url_file=url_file)
    arr_kepemilikan = load_kepemilikan(folder_name=nama_folder, game_list=arr_game, user_id=user_id, url_file=url_file)
    arr_kepemilikan_full = load_kepemilikan_full(folder_name=nama_folder, url_file=url_file)
    arr_riwayat = load_riwayat(folder_name=nama_folder, url_file=url_file)

    return arr_game, arr_kepemilikan, arr_kepemilikan_full, arr_riwayat


def get_args():
    parser = argparse.ArgumentParser(usage='python program_binomo.py <nama_folder>')

    parser.add_argument("param", nargs='*')

    args = parser.parse_args()

    return args.param, parser


def login(user_arr):
    arr = []
    while True:
        if not arr:
            arr = login_front(user_arr)
        else:
            break

    return arr


if __name__ == '__main__':
    folder_name, arg_obj = get_args()
    folder_name = folder_name[0]

    if not folder_name:
        print('Tidak ada nama folder yang diberikan!')
        arg_obj.print_usage()
        sys.exit()

    print('loading...')

    try:
        user_arr, url_file = load_user(folder_name, url_file=None)

    except FileNotFoundError:
        print('Folder "'+str(folder_name)+'" tidak ditemukan.')
        sys.exit()

    print('Selamat datang! Silahkan login terlebih dahulu')

    # F03
    logged_in_arr = login(user_arr)

    loader = load(nama_folder=folder_name, user_id=logged_in_arr[0], url_file=url_file)
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

                print('Tidak terdaftar sebagai admin')

        # F04
        elif menu.strip() == 'tambah_game':

            if logged_in_arr[4] == '0':

                arr = tambah_game_front(game_arr)

                game_arr = arr

            else:

                print('Tidak terdaftar sebagai admin')

        # F05
        elif menu.strip() == 'ubah_game':

            if logged_in_arr[4] == '0':

                arr = ubah_game_front(game_arr)

                if arr:
                    game_arr = arr

                if not arr:
                    pass

            else:

                print('Tidak terdaftar sebagai admin')

        # F06
        elif menu.strip() == 'ubah_stok':

            if logged_in_arr[4] == '0':

                search_arr = ubah_stok_front(game_arr)
                game_arr = search_arr

                print(search_arr)

            else:

                print('Tidak terdaftar sebagai admin')

        # F07
        elif menu.strip() == 'list_game_toko':
            
            search_arr = list_game_toko_front(game_arr)

            if search_arr:
                print("Daftar game di toko:")
                print_format(search_arr)

        # F08
        elif menu.strip() == 'buy_game':
            
            if logged_in_arr[4] == '1':
                tup = buy_game(game_arr, kepemilikan_arr, kepemilikan_full, riwayat_arr, logged_in_arr[0], user_arr)

                if tup:

                    game_arr = tup[0]
                    kepemilikan_arr = tup[1]
                    kepemilikan_full = tup[2]
                    riwayat_arr = tup[3]
                    user_arr = tup[4]

                else:
                    print('Anda tidak memiliki game tersebut.')
                    pass

            else:

                print('Tidak terdaftar sebagai user.')

        # F09
        elif menu.strip() == 'list_game':
            
            if logged_in_arr[4] == '1':
                search_arr = kepemilikan_arr
                if not search_arr:
                    print("Maaf, kamu belum membeli game. Ketik perintah beli_game untuk beli.")
                else:
                    print('Daftar game:')
                    print_format(search_arr)
            else:

                print('Tidak terdaftar sebagai user.')

        # F10
        elif menu.strip() == 'search_my_game':

            if logged_in_arr[4] == '1':

                search_arr = search_my_game_front(kepemilikan_arr)

                if not search_arr:
                    print('Daftar game pada inventory yang memenuhi kriteria:')
                    print('Tidak ada game pada inventory-mu yang memenuhi kriteria.')

                else:
                    print('Daftar game pada inventory yang memenuhi kriteria:')
                    print(search_arr)
                    print_format(search_arr)
            else:

                print('Tidak terdaftar sebagai user.')

        # F11
        elif menu.strip() == 'search_game_at_store':

            search_arr = search_game_at_store_front(game_arr)

            if not search_arr:
                print('Daftar game pada toko yang memenuhi kriteria:')
                print('Tidak ada game pada toko yang memenuhi kriteria.')

            else:
                print('Daftar game pada toko yang memenuhi kriteria:')
                print_format(search_arr)

        # F12
        elif menu.strip() == 'topup':

            if logged_in_arr[4] == '0':
                try:
                    arr = topup(user_arr)

                    if arr:
                        user_arr = arr

                    else:
                        pass

                except ValueError:
                    print('Input tidak valid')

            else:
                print('Tidak terdaftar sebagai admin')

        # F13
        elif menu.strip() == 'riwayat':
        
            if logged_in_arr[4] == '1':
                print(kepemilikan_arr)

            else:

                print('Tidak terdaftar sebagai user.')

        # F14
        elif menu.strip() == 'help':
            help_front(logged_in_arr[4])

        # F16
        elif menu.strip() == 'save':
            save_front(user_arr, game_arr, riwayat_arr, kepemilikan_full)

        #F17
        elif menu.strip() == 'exit':
            exit_front(user_arr, game_arr, riwayat_arr, kepemilikan_full)
        
        #B02
        elif menu.strip() == 'kerangajaib':
            kerangajaib()
