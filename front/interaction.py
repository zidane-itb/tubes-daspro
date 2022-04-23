from data.gameaggr import search_game_by_id_tahun, search_full, ubah_stok, list_game_toko, add_game, ubah_game, \
    search_game_by_id, save_game
from data.useraggr import register, login, save_user
from data.kepemilikanaggr import save_kepemilikan
from data.riwayataggr import save_riwayat
from security.validator import validate_register
from sys import exit



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


def tambah_game_front(game_list):
    nama_game_tambah = None
    kategori_tambah = None
    tahun_tambah = None
    harga_tambah = None
    stok_tambah = None

    while True:
        correct = True

        nama_game_tambah = input('Masukan nama game: ')
        kategori_tambah = input('Masukan kategori game: ')
        tahun_tambah = input('Masukan tahun rilis game: ')
        harga_tambah = input('Masukan harga game: ')
        stok_tambah = input('Masukkan stok awal game: ')

        if (nama_game_tambah == '' or nama_game_tambah is None) or (kategori_tambah == '' or kategori_tambah is None):
            correct = False

        try:

            tahun_tambah = int(tahun_tambah)
            harga_tambah = float(harga_tambah)
            stok_tambah = int(stok_tambah)

        except ValueError:
            correct = False

        if correct:

            break

        else:

            print('format salah')

    arr = add_game(game_list, nama_game_tambah, kategori_tambah,
                   tahun_tambah, harga_tambah, stok_tambah)

    print('Berhasil menambahkan game', nama_game_tambah)

    return arr


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

        tahun_rilis_search = int(tahun_rilis_search) if tahun_rilis_search is not None else None

    except ValueError:

        print('Tahun rilis tidak valid')

        return []

    arr = search_game_by_id_tahun(game_arr, game_id_search, tahun_rilis_search)

    return arr


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
    id_game = None
    amount = None

    while True:
        id_game = input('Masukkan ID Game:')

        if id_game.strip() == '':
            pass

        else:
            break

    while True:
        amount = input("Masukkan jumlah: ")
        correct = True

        try:
            amount = float(amount)

        except ValueError:
            correct = False

        if correct:
            break

    search_arr = ubah_stok(game_list, id_game, amount)
    arr = None

    if not search_arr:
        arr = game_list
        print("Tidak ada game dengan ID tersebut!")
    elif search_arr[1] == 0:
        arr = search_arr[0]
        print("Stok game ", id, " gagal dikurangi karena stok kurang. Stok sekarang: ", search_arr[1])
    elif search_arr[1] == -1:
        arr = search_arr[0]
        print("Stok game ", id, " berhasil dikurangi. Stok sekarang: ", search_arr[1])
    elif search_arr[1] == 1:
        arr = search_arr[0]
        print("Stok game ", id, " berhasil ditambahkan. Stok sekarang: ", search_arr[1])

    return arr


def list_game_toko_front(game_list):
    sort_scheme = input("Skema sorting: ")
    arr = list_game_toko(game_list, sort_scheme)
    if not arr:
        print("Skema sorting tidak valid!")
        return arr
    else:
        return arr


def ubah_game_front(game_list):
    id_game = None

    while True:
        id_game = input('Masukkan ID Game: ')

        if id_game.strip() == '':
            pass

        else:
            break

    index = search_game_by_id(game_list, id_game)

    while True:
        if index != -1:
            nama_game = input('Masukkan Nama Game: ')
            kategori = input('Masukkan Kategori: ')
            tahun_rilis = input('Masukkan Tahun Rilis: ')
            harga = input('Masukkan Harga: ')

            correct = True

            nama_game = None if nama_game.strip() == '' else nama_game
            kategori = None if kategori.strip() == '' else kategori
            tahun_rilis = None if tahun_rilis.strip() == '' else tahun_rilis
            harga = None if harga.strip() == '' else harga

            try:

                tahun_rilis = int(tahun_rilis)
                harga = float(harga)

            except ValueError:
                if tahun_rilis is not None and harga is not None:
                    correct = False

            except TypeError:

                try:
                    harga = float(harga)

                except TypeError:
                    pass

                except ValueError:
                    correct = False

            if correct:
                arr = ubah_game(game_list, id_game, nama_game, kategori, tahun_rilis, harga)

                return arr

            else:
                print('Input tidak valid.')

                pass

        else:

            print('Game ID:', id_game, 'tidak berada di database.')

            return []


def save_front(user_arr, game_arr, riwayat_arr, kepemilikan_full):
    nama_folder = input('Masukkan nama folder penyimpanan: ')

    print('Saving...')

    try:
        succeed = True
        save_user(user_arr, nama_folder)
        save_game(game_arr, nama_folder)
        save_riwayat(riwayat_arr, nama_folder)
        save_kepemilikan(kepemilikan_full, nama_folder)

    except Exception as e:
        print(e)
        succeed = False

    if succeed:
        print('Data telah disimpan pada folder', str(nama_folder)+'!')
        exit()
    else:
        print('Penyimpanan data gagal, silahkan coba lagi.')


def exit_front(user_arr, game_arr, riwayat_arr, kepemilikan_full):
    ans = None

    while True:
        ans = input('Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ').lower()

        if ans == 'y' or ans =='n':
            break

    if ans =='y':
        save_front(user_arr, game_arr, riwayat_arr, kepemilikan_full)

    else:
        pass


def help_front(role):
    if role == "0":
        print("===========================HELP===========================")
        print("1. register - Untuk melakukan registrasi user baru")
        print("2. login - Untuk melakukan login ke dalam sistem")
        print("3. tambah_game - Untuk menambah game yang dijual pada toko")
        print("4. ubah_game - Untuk mengubah game yag dijual pada toko")
        print("5. ubah_stok - Untik mengubah stok game yang dijual pada toko")
        print("6. list_game_toko - Untuk melihat list game yang dijual pada toko")
        print("7. search_game_at_store - Untuk mencari game yang dijual pada toko")
        print("8. topup - Untuk menambah/mengurangi saldo dari user")
        print("9. save - Untuk menyimpan data file setelah melakukan perubahan")
    elif role == "1":
        print("===========================HELP===========================")
        print("1. login - Untuk melakukan login ke dalam sistem")
        print("2. list_game_toko - Untuk melihat list game yang dijual pada toko")
        print("3. buy_game - Untuk membeli game")
        print("4. list_game - Untuk melihat list game yang dimiliki")
        print("5. search_my_game - Untuk mencari game yang dimiliki berdasarkan id game/tahun rilis")
        print("6. search_game_at_store - Untuk mencari game yang dijual pada toko")
        print("7. save - Untuk menyimpan data file setelah melakukan perubahan")
    else:
        return
