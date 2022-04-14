
# implementasi fungsi len bawaan python
def len(arr):
    i = 0
    for el in arr:
        i += 1
    return i


# implementasi fungsi append bawaan python. fungsi ini bisa menerima lebih dari 1 elemen untuk di append
# ke list
def append(arr, *args):
    for el in args:
        arr += [el]

    return arr
