import os


def write(headers, datas, folder_name, file_name):
    # headers = ['Name', 'M1 Score', 'M2 Score']
    # datas = [['Alex', 62, 80], ['Brad', 45, 56], ['Joey', 85, 98]]

    delimiter = ';'

    folder_found = False
    url = ''

    for (root, dirs, files) in os.walk('..', topdown=True):
        if folder_name in dirs or root == folder_name:
            url = os.path.join(root, folder_name)
            folder_found = True

    if not folder_found:
        os.mkdir(path=folder_name)
        url = folder_name

    with open(os.path.join(url, file_name), 'w') as file:
        for header in headers:
            file.write(header + delimiter)
        file.write('\n')
        for data in datas:
            for text in data:
                file.write(str(text) + delimiter)
            file.write('\n')


def read(folder_name, file_name):
    delimiter = ';'

    folder_found = False
    url = ''

    for (root, dirs, files) in os.walk('..', topdown=True):
        if folder_name in dirs:
            url = os.path.join(root, folder_name)
            folder_found = True

    if not folder_found:
        pass

    with open(os.path.join(url, file_name)) as file:
        raw_full = file.read().splitlines()
        raw_data = raw_full[1:]
        data_arr = []

        for data in raw_data:
            data_arr += [splitter(data, delimiter)]

    return data_arr


def splitter(string, delimiter):
    cur = ''
    arr = []
    for el in string:
        if el == delimiter:
            arr += [cur]
            cur = ''
        else:
            cur += el
    return arr

