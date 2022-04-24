# implementasi fungsi len bawaan python
def length(arr):
    i = 0

    # karena tidak boleh melakukan loop tanda index, kita melakukan while loop hingga arr[i] melempar
    # exception berupa IndexError
    while True:
        try:
            arr[i]

            i += 1

        except IndexError:
            break

    return i


# implementasi fungsi append bawaan python. fungsi ini bisa menerima lebih dari 1 elemen untuk di add_list
# ke list
def add_list(arr, *args):
    for i in range(length(args)):
        arr += [args[i]]

    return arr


# implementasi fungsi split bawaan python. fungsi ini memisahkan string berdasarkan elemen delimiter lalu
# mengubahnya menjadi array
def splitter_to_array(string, delimiter):
    cur = ''
    arr = []

    for i in range(length(string)):
        if string[i] == delimiter:
            arr += [cur]
            cur = ''

        else:
            cur += string[i]

    return arr


def el_in_array(el, arr):
    for i in arr:
        if i == el:
            return True

    return False


def convert_arr_to_type(el_arr, type_arr):
    num = length(el_arr)

    if num == length(type_arr):
        for i in range(num):
            if type_arr[i] is not None:
                el_arr[i] = type_arr[i](el_arr[i])

    return el_arr


def print_format(list_arr):
    arr = list_arr
    maxnama = 0
    maxharga = 0
    maxkateg = 0
    maxtahun = 0
    if not arr:
        return []

    if length(arr) == 1:
        print(str(1) + '. ', end='')
        arr = arr[0]
        for k in range(length(arr)):
            if k == 1:
                text = "{isi:<{diff}s}".format(isi=str(arr[k]), diff=str(maxnama))
                print(text, end=' | ')
            elif k == 2:
                text = "{isi:<{diff}s}".format(isi=str(arr[k]), diff=str(maxharga))
                print(text, end=' | ')
            elif k == 3:
                text = "{isi:<{diff}s}".format(isi=str(arr[k]), diff=str(maxkateg))
                print(text, end=' | ')
            elif k == 4:
                text = "{isi:<{diff}s}".format(isi=str(arr[k]), diff=str(maxtahun))
                print(text, end=' | ')
            else:
                text = "{isi:<{diff}s}".format(isi=str(arr[k]), diff='0')
                print(text, end=' | ')
        print('')
        return []

    else:

        for a in range(length(arr)):
            if maxnama < length(str(arr[a][1])):
                maxnama = length(str(arr[a][1]))

            if maxharga < length(str(arr[a][2])):
                maxharga = length(str(arr[a][2]))

            if maxkateg < length(str(arr[a][3])):
                maxkateg = length(str(arr[a][3]))

            if maxtahun < length(str(arr[a][4])):
                maxtahun = length(str(arr[a][4]))

        for i in range(length(arr)):
            print(str(i + 1) + '. ', end='')
            for j in range(length(arr[i])):
                if j == length(arr[i]) - 1:
                    print(arr[i][j])
                else:
                    if j == 1:
                        text = "{isi:<{diff}s}".format(isi=str(arr[i][j]), diff=str(maxnama))
                        print(text, end=' | ')
                    elif j == 2:
                        text = "{isi:<{diff}s}".format(isi=str(arr[i][j]), diff=str(maxharga))
                        print(text, end=' | ')
                    elif j == 3:
                        text = "{isi:<{diff}s}".format(isi=str(arr[i][j]), diff=str(maxkateg))
                        print(text, end=' | ')
                    elif j == 4:
                        text = "{isi:<{diff}s}".format(isi=str(arr[i][j]), diff=str(maxtahun))
                        print(text, end=' | ')
                    else:
                        text = "{isi:<{diff}s}".format(isi=str(arr[i][j]), diff='0')
                        print(text, end=' | ')

        print('')
        return []
