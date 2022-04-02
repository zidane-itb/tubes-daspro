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
        return game_list[search_game_by_id(game_list, game_id)]
    elif game_id is None and tahun is None:
        return game_list
    else:
        arr = []
        for el in game_list:
            if el[3] == tahun:
                arr += el
        return arr


def load_game(folder_name):
    return read(folder_name, __file_name)


def convert_id(game_id):
    return int(game_id[4:])

# arr = [['GAME001', 'PA'], ['GAME002', 'PAR'], ['GAME003', 'PARA'], ['GAME004', 'PARAM'], ['GAME005', 'PARAMP']]
# objs = search_game_by_id(arr, 'GAME027')
# print(objs)
