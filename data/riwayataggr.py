from file.csv import read, write

__csv_header = ['game_id', 'nama', 'harga', 'user_id', 'tahun_beli']
__file_name = 'riwayat.csv'


def load_riwayat(folder_name, url_file):
    return read(folder_name=folder_name, file_name=__file_name, url_file=url_file)


def save_riwayat(arr, folder_name, url_file):
    return write(__csv_header, arr, folder_name, __file_name, url_file=url_file)


def riwayat_validator(array, user_id):
    if array[3] == user_id:
        return True
    else:
        return False
