import os

from default.liststc import splitter_to_array, add_list, length, convert_arr_to_type, el_in_array

delimiter = ';'


def write(header, arr, folder_name, file_name, url_file=None):
    url = url_file
    url_none = True if not url else False
    folder_found = False
    url = ''

    if url is None:
        for (root, dirs, files) in os.walk('..', topdown=True):

            # memvalidasi apakah directory sesuai dengan nama folder
            if el_in_array(folder_name, dirs):
                url = os.path.join(root, folder_name)
                folder_found = True

                # menurut spek, jika file dengan nama yang sama ditemukan, maka harus menghapus existing file
                # terlebih dahulu
                if el_in_array(file_name, files):
                    os.remove(file_name)
    else:
        folder_found=True

    # membuat folder baru jika tidak ada folder bername file_name
    if not folder_found:
        os.mkdir(path=folder_name)
        url = folder_name

    # proses writing
    with open(os.path.join(url, file_name), 'w') as file:

        # write csv header
        for i in range(length(header)):
            file.write(header[i] + delimiter)

        file.write('\n')

        # write the data
        for i in range(0, length(arr)):

            for j in range(length(arr[i])):
                file.write(str(arr[i][j]) + delimiter)

            file.write('\n')

    # untuk optimisasi, kita melakukan pencarian url hanya sekali untuk beberapa file dengan cara melempar
    # url jika url awalnya tidak dimiliki (ditandai dengan variabel url_none)
    return url if url_none else None


def read(folder_name, file_name, type_arr=None, function_validator=None, function_search=None,
         validator_param=None, search_param=None, url_file=None):
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

    url = url_file
    url_none = True if not url_file else False
    folder_found = False

    # proses pencarian file. proses ini bisa mencakup folder dimanapun jika masih merupakan child dari folder
    # utama program
    if url is None:
        for (root, dirs, files) in os.walk('..', topdown=True):
            if el_in_array(folder_name, dirs):
                url = os.path.join(root, folder_name)
                folder_found = True
    else:
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
                # memecah string tiap line menjadi array berdasarkan delimiter
                data = splitter_to_array(raw[i], delimiter)

                # pemasukan data ke array. menggunakan parameter yang sudah dijelaskan di atas
                if type_arr is not None:
                    data = convert_arr_to_type(data, type_arr)

                if function_validator is None:

                    if function_search is None:
                        data_arr = add_list(data_arr, data)
                    else:
                        search = function_search(search_param, data)
                        data_arr = add_list(data_arr, search)

                else:

                    if function_validator(data, validator_param):
                        if function_search is None:
                            data_arr = add_list(data_arr, data)

                        else:
                            search = function_search(search_param, data)
                            data_arr = add_list(data_arr, search)

    # untuk optimisasi, kita hanya akan melakukan pencarian url sekali, lalu melempar url yang sudah ditemukan
    if url_none:
        return data_arr, url
    else:
        return data_arr
