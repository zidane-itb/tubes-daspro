from default.liststc import length, add_list
from file.csv import read, write

__csv_header = ['id', 'nama', 'kategori', 'tahun_rilis', 'harga', 'stok']
__file_name = 'game.csv'


# search game by id, binary search (sorted game array)
def search_game_by_id(game_list, game_id, lh=None, rh=None):
    game_id_conv = convert_id(game_id)

    if lh is None:
        lh = 0
    if rh is None:
        rh = length(game_list) - 1

    if rh >= lh:
        middle = lh + (rh - lh) // 2
        if convert_id(game_list[middle][0]) == game_id_conv:
            return middle

        if convert_id(game_list[middle][0]) > game_id_conv:
            return search_game_by_id(game_list, game_id, lh, middle - 1)
        else:
            return search_game_by_id(game_list, game_id, middle + 1, rh)
    else:
        return -1


def search_game_by_id_tahun(game_list, game_id=None, tahun=None):
    # jika game id dan tahun tidak diberikan, return game_list utuh
    if game_id is None and tahun is None:

        return game_list

    # seach by game_id if game_id is not None
    elif game_id is not None:

        # menggunakan fungsi search_game_by_id untuk mencari index
        arr = game_list[search_game_by_id(game_list, game_id)]

        # mencocokkan data game berdasarkan game_id dengan data tahun (jika diberikan)
        if tahun is not None:
            if arr[3] == tahun:

                # return jika sesuai
                return [arr]

            else:

                # return array kosong jika tidak sesuai
                return []

        # return array jika field tahun tidak diisi
        return [arr]

    else:
        arr = []

        # loop array game_list
        for i in range(length(game_list)):

            # mencari elemen game_list dengan tahun yang sesuai dengan parameter
            if int(game_list[i][3]) == tahun:
                arr += [game_list[i]]

        return arr


# search game dengan full fields (tidak wajib diisi)
def search_full(game_list, game_id=None, nama_game=None, harga=None, kategori=None, tahun_rilis=None):
    if game_id is not None:

        id_fulfill = True
        nama_fulfill = True
        harga_fulfill = True
        kategori_fulfill = True
        tahun_fulfill = True

        # array game dengan game_id sesuai parameter fungsi
        arr = game_list[search_game_by_id(game_list, game_id)]

        # cek apakah semua field input user yang ada sesuai dengan data berdasarkan game_id
        if nama_game is not None and nama_game != arr[1]:
            nama_fulfill = False
        if harga is not None and harga != arr[4]:
            harga_fulfill = False
        if kategori is not None and kategori != arr[2]:
            kategori_fulfill = False
        if tahun_rilis is not None and tahun_rilis != arr[3]:
            tahun_fulfill = False

        # return array jika semua field sesuai
        if id_fulfill and nama_fulfill and harga_fulfill and kategori_fulfill and tahun_fulfill:
            return arr
        else:
            return []

    else:
        arr = []

        # loop array game_list untuk mencari game dengan parameter yang sesuai
        for i in range(length(game_list)):
            if (nama_game is not None and nama_game == game_list[i][1]) or (
                    harga is not None and harga == game_list[i][4]) or (
                    kategori is not None and kategori == game_list[i][2]) or (
                    tahun_rilis is not None and tahun_rilis == game_list[i][3]):
                # game dengan fields sesuai parameter found
                arr += [game_list[i]]

        # return array
        if not arr:
            return game_list
        else:
            return arr


def add_game(game_list, nama_game, kategori, tahun_rilis, harga, stok_awal):
    if not (
            game_list is None and nama_game is None and kategori is None and tahun_rilis is None and harga is None and stok_awal is None):

        id_num = convert_id(game_list[length(game_list) - 1][0]) + 1

        game_id = create_game_id(id_num)

        arr = [game_id, nama_game, kategori, tahun_rilis, harga, stok_awal]

        game_list = add_list(game_list, arr)

        return game_list

    else:

        return []


def ubah_stok(game_list, game_id, amount):
    amount = int(amount)
    
    for i in range(length(game_list)):

        if game_list[i][0] == game_id and amount >= 0:
            game_list[i][5] += amount
            arr = game_list
            return arr, 1

        elif game_list[i][0] == game_id and amount < 0:
            if game_list[i][5] + amount > 0:
                game_list[i][5] += amount
                arr = game_list
                return arr, -1

            else:
                arr = game_list
                return arr, 0

        else:
            return []


def list_game_toko(game_list, sort_scheme=None):
    if sort_scheme is not None:
        if sort_scheme == "tahun-" or sort_scheme == "tahun+":
            if sort_scheme == "tahun-":
                arr = game_list
                for i in range(length(arr)):
                    for j in range(i + 1, length(arr)):
                        if arr[i][3] < arr[j][3]:
                            arr[i][3], arr[j][3] = arr[j][3], arr[i][3]
                return arr
            else:
                arr = game_list
                for i in range(length(arr)):
                    for j in range(i + 1, length(arr)):
                        if arr[i][3] > arr[j][3]:
                            arr[i][3], arr[j][3] = arr[j][3], arr[i][3]
                return arr
        elif sort_scheme == "harga-" or sort_scheme == "harga+":
            if sort_scheme == "harga-":
                arr = game_list
                for i in range(length(arr)):
                    for j in range(i + 1, length(arr)):
                        if arr[i][4] < arr[j][4]:
                            arr[i][4], arr[j][4] = arr[j][4], arr[i][4]
                return arr
            else:
                arr = game_list
                for i in range(length(arr)):
                    for j in range(i + 1, length(arr)):
                        if arr[i][4] > arr[j][4]:
                            arr[i][4], arr[j][4] = arr[j][4], arr[i][4]
                return arr
        else:
            return []
    else:
        return game_list


def ubah_game(game_list, game_id, nama_game=None, kategori=None, tahun_rilis=None, harga=None):
    if game_id is not None:

        index = search_game_by_id(game_list, game_id)

        if nama_game is not None:
            game_list[index][1] = nama_game

        if kategori is not None:
            game_list[index][2] = kategori

        if tahun_rilis is not None:
            game_list[index][3] = tahun_rilis

        if harga is not None:
            game_list[index][4] = harga

        return game_list

    else:

        return game_list


def game_information(game_list, gameID):
    for i in range(length(game_list)):
        if game_list[i][0] == gameID:
            return game_list[i], i
    return [], -1


def cek_user_have_bought(game_user, gameID):
    for i in range(length(game_user)):
        if game_user[i][0] == gameID:
            return True
    return False


def cek_saldo_cukup(data_saldo_user, user_id, harga):
    for i in range(length(data_saldo_user)):
        if data_saldo_user[i][0] == user_id:
            if data_saldo_user[i][5] >= harga:
                return True
            else:
                return False
    return False


def buy_game(game_list, game_user, kepemilikan_full, riwayat_game, user_id, user_list):
    index_user = user_list[int(user_id)-1]
    user_id = index_user[0]

    gameID = input("Masukkan ID Game: ")
    gameInfo, index = game_information(game_list, gameID)

    if length(gameInfo) == 0:
        print("ID Game Salah")

    else:
        saldoCukup = cek_saldo_cukup(user_list, user_id, gameInfo[4]) # gameInfo indeks ke-4 adalah harga
        if cek_user_have_bought(game_user, gameID):
            print("Anda sudah memiliki Game tersebut!")

        elif not saldoCukup:
            print("Saldo anda tidak cukup untuk membeli Game tersebut!")

        elif gameInfo[5] == 0:  # gameInfo indeks ke-5 adalah stok
            print("Stok Game tersebut sedang habis!")

        else:
            game_list[index][5] -= 1
            game_user += [[gameInfo[0], gameInfo[1], gameInfo[2], gameInfo[3], gameInfo[4]]]
            riwayat_game += [[gameInfo[0], gameInfo[1], gameInfo[4], user_id, gameInfo[3]]]
            kepemilikan_full = add_list(kepemilikan_full, [gameInfo[0], user_id])
            index_user[5] -= gameInfo[4]

            print("Game '" + gameInfo[1] + "' berhasil dibeli!")

            return game_list, game_user, kepemilikan_full, riwayat_game, user_list

    return []


def create_game_id(id_number):
    game_id = 'GAME'

    while (length(game_id) + length(str(id_number))) < 7:
        game_id += '0'

    game_id += str(id_number)

    return game_id


def load_game(folder_name, url_file):
    return read(folder_name=folder_name, file_name=__file_name, type_arr=[None, None, None, int, float, int], url_file=url_file)


def save_game(game_list, folder_name, url_file):
    return write(__csv_header, game_list, folder_name, __file_name, url_file=url_file)


# mengubah game id dengan format GAMEXXX menjadi angka XXX
def convert_id(game_id):
    return int(str(game_id[4] + game_id[5] + game_id[6]))
