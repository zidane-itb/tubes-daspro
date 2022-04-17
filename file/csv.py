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
         validator_param=None, search_param=None):

    # penjelasan parameter fungsi
    #
    # folder_name: nama folder
    #
    # file_name: nama_file
    #
    # function_validator: jika tidak semua lines dari file ingin disimpan sebagai array, maka akan dilakukan validasi
    #                     di tiap line data menggunakan fungsi ini
    #
    # function_search: jika ingin menggunakan data di tiap line file untuk melakukan proses search, maka fungsi
    #                  function_search akan dijalankan. karena berada di fungsi load, artinya tidak akan ada field
    #                  yang merupakan input user selain folder_name, maka diasumsikan fungsi ini akan selalu memberikan
    #                  array yang memiliki isi
    #
    # validator_param: parameter yang akan digunakan sebagai validator di function_validator
    #
    # search_param: parameter yang akan digunakan function_search

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

            # karena line 0 dari data merupakan header, maka kita bisa melewati i = 0
            if i == 0:
                pass

            else:
                if function_validator is None:

                    data = splitter_to_array(raw[i], delimiter)

                    if function_search is None:
                        data_arr = add_list(data_arr, data)
                    else:
                        search = function_search(search_param, data)
                        data_arr = add_list(data_arr, search)

                else:

                    data = splitter_to_array(raw[i], delimiter)

                    if function_validator(data, validator_param):
                        if function_search is None:
                            data_arr = add_list(data_arr, data)

                        else:
                            search = function_search(search_param, data)
                            data_arr = add_list(data_arr, search)

    return data_arr
