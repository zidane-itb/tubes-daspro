
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
