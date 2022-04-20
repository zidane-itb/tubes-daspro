from file.csv import read
from data.gameaggr import search_game_by_id
from default.liststc import length

__csv_header = ['game_id', 'user_id']
__file_name = 'kepemilikan.csv'

#09
def load_kepemilikan(folder_name, game_list, user_id):
    return read(folder_name, __file_name, function_validator=verify_kepemilikan, function_search=search_game,
                validator_param=user_id, search_param=game_list)


def verify_kepemilikan(array, user_id):
    try:
        if int(array[1]) == int(user_id):
            return True
    except ValueError:
        return False


def search_game(game_list, array):
    return game_list[search_game_by_id(game_list, array[0])]
