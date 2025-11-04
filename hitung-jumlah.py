kalimat = input("masukan kalimat :")
huruf = ""

kalimat = kalimat.lower()

jumlah = 0

for karakter in kalimat:
    if karakter:
        jumlah += 1
print(f"jumlah kalimat dalam teks adalah : {jumlah}")