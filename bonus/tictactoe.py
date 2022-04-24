from default.liststc import length

#PROGRAM TIC TAC TOE
papan = ["-","-","-",
        "-", "-","-",
        "-","-","-"]
Pemain = "-"
Pemain1 = "X"
Pemain2 = "O"
Bermain = True

def cetak_papan(papan):
    print(papan[0],"|",papan[1],"|",papan[2])
    print("----------")
    print(papan[3],"|",papan[4],"|",papan[5])
    print("----------")
    print(papan[6],"|",papan[7],"|",papan[8])


hitung = 0
for i in range(length(papan)):
    if papan[i] != "-":
            hitung+=1
if hitung%2 == 0:
    Pemain=Pemain1
else:
    Pemain=Pemain2

def input_pemain(papan,Pemain):
    langkah = int(input("Masukkan input antara 1-9: "))
    if papan[langkah-1] == "-" and 1<=langkah<=9:
        papan[langkah-1] = Pemain
        if Pemain==Pemain1 :
          Pemain=Pemain2
        elif Pemain==Pemain2:
          Pemain=Pemain1
    else:
        print("Yahhh sudah terisi kotak ini, silahkan pilih kotak lain!")
    return Pemain

def penentu_pemenang(papan):
    pemenang="-"
    if papan[0]==papan[1]==papan[2] and papan[2] != "-":
        pemenang=papan[2]
    elif papan[3]==papan[4]==papan[5] and papan[5] != "-":
        pemenang=papan[5]
    elif papan[6]==papan[7]==papan[8] and papan[8] != "-":
        pemenang=papan[8]
    elif papan[0]==papan[3]==papan[6] and papan[6] != "-":
        pemenang=papan[6]
    elif papan[1]==papan[4]==papan[7] and papan[7] != "-":
        pemenang=papan[7]
    elif papan[2]==papan[5]==papan[8] and papan[8] != "-":
        pemenang=papan[8]
    elif papan[0]==papan[4]==papan[8] and papan[8] != "-":
        pemenang=papan[8]
    elif papan[2]==papan[4]==papan[6] and papan[6] != "-":
        pemenang=papan[6]
    else:
        cek_kosong = 0
        for j in range(length(papan)):
            if papan[j] == "-":
                cek_kosong+=1
        if cek_kosong == 0:
            pemenang = "Seri"
    return pemenang


def tictactoe():
    while Bermain:
        cetak_papan(papan)
        Pemain = input_pemain(papan, Pemain)
        pemenang = penentu_pemenang(papan)
        if pemenang == Pemain1:
            print("Selamat! X telah memenangkan permainan ini")
        elif pemenang == Pemain2:
            print("Selamat! O telah memenangkan permainan ini")
        elif pemenang == "Seri":
            print("Seri! Tidak ada pemenang")

