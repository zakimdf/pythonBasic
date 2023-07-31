# MEMBUAT KALKULATOR TIP

print("Selamat Datang di Kalkulator Tip")
bayar = float(input("biaya yang harus anda bayar: $"))
persen = int(input("Berapa persentase yang anda berikan: "))
orang = int(input("Berapa banyak orang yang akan membayar: "))
persenan = (bayar * (persen / 100))
total = (bayar + persenan) / orang
print(f"Tiap orang harus membayar ${round(total, 2)}")
print('Tiap orang harus membayar $'"{:.2f}".format(total))
