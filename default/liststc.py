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
    diff = []
    if not arr:
        return []

    else:
        for a in range(1, length(arr)):
            b = 0
            for b in range(length(arr[b])):
                if diff[a] < length(arr[b][a]):
                    diff[a] = length(arr[b][a])
        for i in range(length(arr)):
            print(str(i+1) + '. ', end='')
            for j in range(length(arr[i])):
                if j == length(arr[i])-1:
                    print(arr[i][j])
                else:
                    text = "{isi:<{diff}s}".format(isi=arr[i][j], diff=diff[j])
                    print(text, end=' | ')
        return []