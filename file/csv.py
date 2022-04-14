import os

delimiter = ';'


def write(headers, datas, folder_name, file_name):

    folder_found = False
    url = ''

    for (root, dirs, files) in os.walk('.', topdown=True):

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


def read(folder_name, file_name):

    folder_found = False
    url = ''

    for (root, dirs, files) in os.walk('.', topdown=True):
        if folder_name in dirs:
            url = os.path.join(root, folder_name)
            folder_found = True

    if not folder_found:
        raise FileNotFoundError

    with open(os.path.join(url, file_name)) as file:
        # splitlines gk boleh
        raw_full = file.read().splitlines()
        # [a:b] gk boleh
        raw_data = raw_full[1:]
        data_arr = []

        # harus pake indeks
        for data in raw_data:
            data_arr += [splitter(data)]

    return data_arr


def splitter(string):
    cur = ''
    arr = []
    # harus pake indeks biasa
    for el in string:
        if el == delimiter:
            arr += [cur]
            cur = ''
        else:
            cur += el
    return arr
