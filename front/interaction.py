from security.validator import validate_register
from data.useraggr import register, login
from data.gameaggr import search_game_by_id_tahun, search_full, ubah_stok, list_game_toko


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


def search_game_at_store_front(game_list):
    game_id = input('Masukkan ID game: ')
    nama_game = input('Masukkan nama game: ')
    harga_game = input('Masukkan harga game: ')
    kategori_game = input('Masukkan kategori game: ')
    tahun_rilis = input('Masukkan tahun rilis game: ')

    game_id = None if game_id.strip() == '' else game_id
    nama_game = None if nama_game.strip() == '' else nama_game
    harga_game = None if harga_game.strip() == '' else harga_game
    kategori_game = None if kategori_game.strip() == '' else kategori_game
    tahun_rilis = None if tahun_rilis.strip() == '' else tahun_rilis

    arr = search_full(game_list, game_id, nama_game, harga_game, kategori_game, tahun_rilis)

    return arr

def ubah_stok_front(game_list):
    ID = input("Masukkan ID game: ")
    amount = int(input("Masukkan jumlah: "))
    search_arr = ubah_stok(game_list, ID, amount)
    arr = None
    if search_arr == []:
        arr = game_list
        print("Tidak ada game dengan ID tersebut!")
    elif search_arr[2] == 0:
        arr = search_arr[0]
        print("Stok game "+ ID +" gagal dikurangi karena stok kurang. Stok sekarang: "+search_arr[1])
    elif search_arr[2] == -1:
        arr = search_arr[0]
        print("Stok game "+ ID +" berhasil dikurangi. Stok sekarang: "+search_arr[1])
    elif search_arr[2] == 1:
        arr = search_arr[0]
        print("Stok game "+ ID +" berhasil ditambahkan. Stok sekarang: "+search_arr[1])
    return arr

def list_game_toko_front(game_list):
    sort_scheme = input("Skema sorting: ")
    arr = list_game_toko(game_list, sort_scheme)
    if arr == []:
        print("Skema sorting tidak valid!")
        return arr
    else:
        return arr

