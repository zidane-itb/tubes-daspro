from file.csv import read

__csv_header = ['game_id', 'nama', 'harga', 'user_id', 'tahun_beli']
__file_name = 'riwayat.csv'


def load_riwayat(folder_name, user_id):
    return read(folder_name, __file_name, function_validator=riwayat_validator, function_param=user_id)


def riwayat_validator(array, user_id):
    if array[3] == user_id:
        return True
    else:
        return False
