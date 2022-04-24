import time
from default.liststc import length

def kerangajaib():
   x = time.time()
   arr = ['Iya.', 'Tidak.', 'Mungkin.', 'Bisa jadi.', 'Coba lagi.', 'Yes.', 'No.', 'Maybe.', 'Hai.', 'Halo.', 'Baik.', 'Jangan.', 'Silakan.', 'Nice.', 'Memang.', 'Ya tidak tahu kok tanya saya.', 'Kok kamu tanya begitu, siapa yang suruh?', 'Tidak ada.', 'Tidak peduli.', 'Kamu rasis.', 'Ayo gacha.', 'L + ratio + don`t care.', 'Bruh.', 'Ok.', 'Ngaca.', 'Oh gitu.', 'Siapa kamu?', 'Hmm.', 'Mungkin saja.', 'Coba saja.', 'Semoga beruntung.', '...']
  
   question = input('Apa pertanyaanmu? ')
   y = length(question)
   z = 42069
   m = length(arr)

   for i in range(m):
      if y%2 == 1:
         y = 3*y+1
         z -= y % 4
      else:
         y = y/2
         z += y % 4

   lcg = round((y*x)+z) % m 
   
   print(arr[lcg])