kalimat = input("masukan kalimat :")
huruf = input("masukan huruf yang ingin di cari :")

kalimat = kalimat.lower()
huruf = huruf.lower()

jumlah = 0

for totalnya in kalimat:
    if totalnya == huruf:
        jumlah += 1

print(f"jumlah huruf '{huruf} dalam kalimat adalah : {jumlah}")