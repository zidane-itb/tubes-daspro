from file.csv import read, write
from data.gameaggr import search_game_by_id

__csv_header = ['game_id', 'user_id']
__file_name = 'kepemilikan.csv'


def load_kepemilikan_full(folder_name, url_file):
    return read(folder_name=folder_name, file_name=__file_name, url_file=url_file)


def load_kepemilikan(folder_name, game_list, user_id, url_file):
    return read(folder_name=folder_name, file_name=__file_name, url_file=url_file, function_validator=verify_kepemilikan,
                function_search=search_game,
                validator_param=user_id, search_param=game_list)


def verify_kepemilikan(array, user_id):
    try:
        if int(array[1]) == int(user_id):
            return True
    except ValueError:
        return False


def search_game(game_list, array):
    return game_list[search_game_by_id(game_list, array[0])]


def save_kepemilikan(arr, folder_name, url_file):
    return write(__csv_header, arr, folder_name, __file_name, url_file=url_file)
