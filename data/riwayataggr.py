from file.csv import splitter
import os

__csv_header = ['game_id', 'nama', 'harga', 'user_id', 'tahun_beli']
__nama_file = 'riwayat.csv'


def load_riwayat(folder_name, user_id):
    delimiter = ';'

    folder_found = False
    url = ''

    for (root, dirs, files) in os.walk('..', topdown=True):
        if folder_name in dirs:
            url = os.path.join(root, folder_name)
            folder_found = True

    if not folder_found:
        raise FileNotFoundError

    with open(os.path.join(url, __nama_file)) as file:
        raw_full = file.read().splitlines()
        raw_data = raw_full[1:]
        data_arr = []

        for data in raw_data:
            row = splitter(data, delimiter)

            if row[3] == user_id:
                data_arr += row[0]

    return data_arr


def search_id_in_arr(id, arr):
    i = 0
    for obj in arr:
        if obj[0] == id:
            return True, i

        i += 1
    return False, 0
