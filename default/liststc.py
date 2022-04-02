def len(arr):
    i = 0
    for el in arr:
        i += 1
    return i


def append(arr, *args):
    for el in args:
        arr += [el]
