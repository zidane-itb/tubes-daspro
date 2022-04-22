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
    # seach by game_id if game_id is not None
    if game_id is not None:

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

    # jika game id dan tahun tidak diberikan, return game_list utuh
    elif game_id is None and tahun is None:

        return game_list

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
        return arr


def add_game(game_list, nama_game, kategori, tahun_rilis, harga, stok_awal):
    if not (game_list is None and nama_game is None and kategori is None and
            tahun_rilis is None and harga is None and stok_awal is None):

        id_num = convert_id(game_list[length(game_list) - 1][0]) + 1

        game_id = create_game_id(id_num)

        arr = [game_id, nama_game, kategori, tahun_rilis, harga, stok_awal]

        game_list = add_list(game_list, arr)

        return game_list

    else:

        return []


def create_game_id(id_number):
    game_id = 'GAME'

    while (length(game_id) + length(str(id_number))) < 7:
        game_id += '0'

    game_id += str(id_number)

    return game_id


def load_game(folder_name):
    return read(folder_name, __file_name)


def save_game(game_list, folder_name):
    return write(__csv_header, game_list, folder_name, __file_name)


# mengubah game id dengan format GAMEXXX menjadi angka XXX
def convert_id(game_id):
    return int(str(game_id[4] + game_id[5] + game_id[6]))
