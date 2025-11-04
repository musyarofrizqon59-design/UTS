soal4 = ""
soal5 = ""
soal6 = ""
soal7 = ""
soal8 = ""
soal9 = ""
soal10 = "" 
soal11 = ""
soal12 = ""
soal13 = ""
soal14 = ""
soal15 = ""
soal16 = ""
soal17 = ""
soal18 = ""
soal19 = ""
soal20 = ""
soal21 = ""
soal22 = ""
soal23 = ""
soal24 = ""
soal25 = ""
soal26 = ""
soal27 = ""
soal28 = ""
soal29 = ""
soal30 = ""


for i in range(1, 7):
    soal4 += str(i) * i
print("soal nomor 4 :"+soal4)

for r in range(6, 0, -1):
    soal5 += str(r) * r
print("soal nomor 5 :"+soal5)

for z in range(1, 7):
    for q in range(1, z +1):
        soal6 += str(z)
print("soal nomor 6 :"+soal6)

for a in range (6, 0, -1):
    for b in range(a, 0, -1):
        soal7 += str(b)
print("soal nomor 7 :"+soal7)
  
soal8 +="1" * 2
soal8 +="2"
soal8 +="3" * 3
for i in range(1,5):
    soal8 += str(i)
soal8 +="5" * 5
for i in range(1, 7):
    soal8 += str(i)
print("soal nomor 8 :"+soal8)

soal9 +="1"
soal9 +="2" * 2
soal9 +="123"
soal9 +="4" * 4
for i in range(1, 6):
    soal9 += str(i)
soal9 +="6" * 6
print("soal nomor 9 :"+soal9)

for i in range(6, 0, -1):
    soal10 += str(i)
soal10 +="5" * 4
for i in range(5, 0, -1):
    soal10 += str(i)
soal10 +="3" * 2
for i in range(3, 0, -1):
    soal10 += str(i)
soal10 +="1"
print("soal nomor 10 :"+soal10)

soal11 +="6" * 6
for i in range(1, 6): 
    soal11 += str(i)
soal11 +="4" * 4
for i in range(1, 4):   
    soal11 += str(i)
soal11 +="221"
print("soal nomor 11 :"+soal11)

for i in range(1,3):
    soal12 += str(i)
soal12 +="2"
for i in range(1, 4):
    soal12 += str(i)
for i in range(1, 5):
    soal12 += str(i)
for i in range(5, 7):
    soal12 += str(i) * i
for i in range(1, 8):   
    soal12 += str(i)
for i in range(1, 9):
    soal12 += str(i)
soal12 +="9" * 9
print("soal nomor 12 :"+soal12)

soal13 +="1"
for b in range(1, 3):
    soal13 += str(b)
for b in range(3, 5):
    soal13 += str(b) * b
for b in range(1, 6):
    soal13 += str(b)
for b in range(1, 7):
    soal13 += str(b)
for b in range(7, 9):
    soal13 += str(b) * b
for b in range(1, 10):
    soal13 += str(b)
print("soal nomor 13 :"+soal13)
    
for k in range(8, 6, -1):
    soal14 += str(k) * k
for k in range(6, 0, -1):
    soal14 += str(k)
for k in range(5, 0, -1):
    soal14 += str(k)
for k in range(4, 2):
    soal14 += str(k) * k
for k in range(2, 0, -1):
    soal14 += str(k)
soal14 +="1"
print("soal nomor 14 :"+soal14)

for g in range(8, 0, -1):
    soal15 += str(g)
for g in range(7, 0, -1):
    soal15 += str(g)
for g in range(6, 4, -1):
    soal15 += str(g) * g
for g in range(4, 0, -1):
    soal15 += str(g)
for g in range(3, 0, -1):
    soal15 += str(g)
for g in range(2, 0, -1):
    soal15 += str(g) * g
print("soal nomor 15 :"+soal15)

n = 1
terms = 12
for i in  range(terms):
    soal16 += str(n) + " "
    if i % 2 == 0:
        n += 4
    else:
        n -= 2
print("soal nomor 16 :"+soal16)

n = 2
for i in range(10):
    soal17 += str(n) + " "
    if i % 2 ==0:
        n += 10
    else:
        n -= 5
print("soal nomor 17 :"+soal17)

n = 5
for i in range(12):
    soal18 += str(n) + " "
    if i % 2 == 0:
        n -= 3
    else:
        n += 5
print("soal nomor 18 :"+soal18)

n = 3
for i in range(10):
    soal19 += str(n) + " "
    if i % 2 == 0:
        n *= 3
    else:
        n -= 5
print("soal nomor 19 :"+soal19)

n = 1
increments = [1, 2, 3]
for i in range(13):
    soal20 += str(n) + " "
    step = increments[i % 3]
    n += step
print("soal nomor 20 :"+soal20)

n = 1
for i in range(10):
    soal21 += str(n) + " "
    n *= 2
print("soal nomor 21 :"+soal21)

n = 3
faktorial = 1
soal22 = str(n) + "! = "
for  i in range(n, 0, -1):
    soal22 += str(i) + " "
    if i > 1:
        soal22 += " x "
    faktorial *= i
soal22 += " = " + str(faktorial)
print("soal nomor 22 :"+soal22)

maks = 45
a, b = 0, 1
soal23 += str(a) + " " + str(b) + " "
while True:
    c = a + b
    if c > maks:
        break
    soal23 += str(c) + ","
    a, b = b, c
print("soal nomor 23 :"+soal23)

n_awal = 10
n_akhir = 35
for i in range(n_awal, n_akhir + 1):
    if i % 3 == 0:
        soal24 += str(i) + " "
print("soal nomor 24 :"+soal24)

n_awal = 10
n_akhir = 40
for i in range(n_awal, n_akhir + 1):
    if i % 4 == 0:
        soal25 += str(i) + " "
print("soal nomor 25 :"+soal25)

n_awal = 6
n_akhir = 11
jumlah_bulat_positif = 0
for i in range(n_awal, n_akhir + 1 ):
    if i > 0:
        jumlah_bulat_positif += 1                                               
print("soal nomor 26 :")
print("total bilangan bulat positif dari", n_awal, "hingga", n_akhir, "adalah = " , jumlah_bulat_positif)

n_awal = 5
n_akhir = 17
jumlah_genap = 0
for i in range(n_awal, n_akhir, +1):
    if i % 2 == 0:
        jumlah_genap += 1
print("soal nomor 27 :")
print("total bilangan genap dari", n_awal, "hingga", n_akhir, "adalah = ", jumlah_genap )

n_awal = 5
n_akhir = 16
jumlah_ganji = 0
for i in range(n_awal, n_akhir, +1):
    if i % 2 != 0:
        jumlah_ganji += 1
print("soal nomor 28 :")
print("total bilangan ganjil dari", n_awal, "hingga", n_akhir, "adalah =", jumlah_ganji)

n_awal = 10
n_akhir = 50
prima_list = []
for num in range(n_awal, n_akhir, +1):
    if num > 1:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                break
        else:
            prima_list.append(num)
print("soal nomor 29 : bilangan primanya adalah =", end = " ")
for p in prima_list:
    print(f"{p}", end = " ")
print()

n_awal = 10
n_akhir = 50
prima_list = []
for num in range(n_awal, n_akhir, +1):
    if num > 1:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                break
        else:
            prima_list.append(num)
print("soal nomor 30 :")
print("bilangan prima :", ' '.join(str(p)
for p in prima_list))
print("jumlah total bilangan prima :", len(prima_list))