from data.gameaggr import ubah_stok

ID = input("Masukkan ID game: ")
amount = int(input("Masukkan jumlah: "))
ubah_stok('game.csv', ID, amount)
print(ubah_stok)