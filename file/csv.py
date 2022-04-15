import os
from default.liststc import splitter_to_array, add_list, length

delimiter = ';'


def write(headers, datas, folder_name, file_name):
    folder_found = False
    url = ''

    for (root, dirs, files) in os.walk('..', topdown=True):

        # memvalidasi apakah directory sesuai dengan nama folder
        if folder_name in dirs or root == folder_name:
            url = os.path.join(root, folder_name)
            folder_found = True

            # menurut spek, jika file dengan nama yang sama ditemukan, maka harus menghapus existing file
            # terlebih dahulu
            if file_name in files:
                os.remove(file_name)

    if not folder_found:
        os.mkdir(path=folder_name)
        url = folder_name

    try:

        with open(os.path.join(url, file_name), 'w') as file:

            for header in headers:
                file.write(header + delimiter)

            file.write('\n')

            # harus pake indeks
            for data in datas:

                # harus pake indeks
                for text in data:
                    file.write(str(text) + delimiter)

                file.write('\n')

        return True

    except:

        return False


def read(folder_name, file_name, function_validator=None, function_search=None,
         function_param=None, search_param=None):
    folder_found = False
    url = ''

    for (root, dirs, files) in os.walk('..', topdown=True):
        if folder_name in dirs:
            url = os.path.join(root, folder_name)
            folder_found = True

    if not folder_found:
        raise FileNotFoundError

    with open(os.path.join(url, file_name)) as file:

        raw = file.readlines()

        data_arr = []

        for i in range(length(raw)):
            if function_validator is None:

                if i == 0:
                    pass

                else:
                    data_arr = add_list(data_arr, splitter_to_array(raw[i], delimiter))

            else:

                if i == 0:
                    pass

                else:
                    data = splitter_to_array(raw[i], delimiter)

                    if function_validator(data, function_param):

                        if function_search is None:
                            data_arr = add_list(data_arr, data)

                        else:
                            search = function_search(search_param, data)
                            data_arr = add_list(data_arr, search)

    return data_arr
