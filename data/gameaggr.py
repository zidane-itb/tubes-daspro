from default.liststc import len
from file.csv import read

__csv_header = ['id', 'nama', 'kategori', 'tahun_rilis', 'harga', 'stok']
__file_name = 'game.csv'


def search_game_by_id(game_list, game_id, lh=None, rh=None):
    game_id_conv = convert_id(game_id)

    if lh is None:
        lh = 0
    if rh is None:
        rh = len(game_list) - 1

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
    if game_id is not None:
        arr = game_list[search_game_by_id(game_list, game_id)]
        if tahun is not None:
            if arr[3] == tahun:
                return [arr]
            else:
                return []
        return [arr]
    elif game_id is None and tahun is None:
        return game_list
    else:
        arr = []
        for el in game_list:
            if int(el[3]) == tahun:
                arr += [el]
        return arr


def search_full(game_list, game_id=None, nama_game=None, harga=None, kategori=None, tahun_rilis=None):

    if game_id is not None:

        id_fulfill = True
        nama_fulfill = True
        harga_fulfill = True
        kategori_fulfill = True
        tahun_fulfill = True

        arr = game_list[search_game_by_id(game_id)]

        if nama_game is not None and nama_game != arr[1]:
            nama_fulfill = False
        if harga is not None and harga != arr[4]:
            harga_fulfill = False
        if kategori is not None and kategori != arr[2]:
            kategori_fulfill = False
        if tahun_rilis is not None and tahun_rilis != arr[3]:
            tahun_fulfill = False

        if id_fulfill and nama_fulfill and harga_fulfill and kategori_fulfill and tahun_fulfill:
            return arr
        else:
            return []

    else:
        arr = []
        for game in game_list:
            if (nama_game is not None and nama_game == game[1]) or (harga is not None and harga == game[4]) or (
                    kategori is not None and kategori == game[2]) or (
                    tahun_rilis is not None and tahun_rilis == game[3]):
                arr += [game]
        return arr


def load_game(folder_name):
    return read(folder_name, __file_name)


def convert_id(game_id):
    return int(game_id[4:])
