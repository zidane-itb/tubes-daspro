from security.validator import validate_register
from data.useraggr import register, login
from data.gameaggr import search_game_by_id_tahun


def register_front(user_arr):
    nama_reg = input('Masukkan nama: ')
    username_reg = input('Masukkan username: ')
    password_reg = input('Masukkan password: ')

    if validate_register(username_reg):

        arr = register(user_arr, username_reg, nama_reg, password_reg)

        if not arr:

            print('Username', username_reg, 'sudah terpakai, silakan menggunakan username lain')

            return user_arr

        else:

            print('Username', username_reg, 'telah berhasil register ke dalam "Binomo"')

            return arr

    else:

        print('Username hanya dapat mengandung alfabet A-Za-z, underscore “_”, strip “-”, dan angka 0-9.')

        return user_arr


def tambah_game_front():
    nama_game_tambah = None
    kategori_tambah = None
    tahun_tambah = None
    harga_tambah = None
    stok_tambah = None

    while True:

        try:

            nama_game_tambah = input('Masukan nama game: ')
            kategori_tambah = input('Masukan kategori game: ')
            tahun_tambah = int(input('Masukan tahun rilis game: '))
            harga_tambah = float(input('Masukan harga game: '))
            stok_tambah = int(input('Masukkan stok awal game: '))

            if (nama_game_tambah == '' or nama_game_tambah is None) or (
                    kategori_tambah == '' or kategori_tambah is None):

                pass

            else:

                break

        except ValueError:

            print('Format input salah')


def login_front(user_arr):
    username_login = input('username: ')
    password_login = input('password: ')

    index = login(user_arr, username_login, password_login)

    if index == -1:

        print('username atau password salah')

        return []

    else:
        logged_in_arr = user_arr[index]

        print('Berhasil login sebagai', logged_in_arr[2])

        return logged_in_arr


def search_my_game_front(game_arr):
    game_id_search = input('Masukkan ID Game: ')
    tahun_rilis_search = input('Masukkan tahun rilis game: ')

    game_id_search = None if game_id_search.strip() == '' else game_id_search
    tahun_rilis_search = None if tahun_rilis_search.strip() == '' else tahun_rilis_search

    try:
        tahun_rilis_search = int(tahun_rilis_search)

        arr = search_game_by_id_tahun(game_arr, game_id_search, tahun_rilis_search)

        return arr

    except ValueError:
        print('Tahun rilis tidak valid')

        return []
