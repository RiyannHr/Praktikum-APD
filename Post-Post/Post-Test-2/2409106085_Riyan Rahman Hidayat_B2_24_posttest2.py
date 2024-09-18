# Input
nama_barang = input("masukan nama barang = ")
harga_barang = float(input("masukan harga barang = "))
jumlah_barang = int(input("masukan jumlah barang = "))
diskon_barang = float(input("Masukkan diskon barang = "))

# Proses
total_sebelum_diskon = jumlah_barang * harga_barang
total_diskon = (diskon_barang/100) * total_sebelum_diskon
total_bayar = total_sebelum_diskon - total_diskon
sisa_baginya = int(diskon_barang % 3)

#output
print(f"Anda membeli {jumlah_barang:.0f} {nama_barang} dengan harga satuan {harga_barang:.0f}, total sebelum diskon adalah {total_sebelum_diskon:.0f}, total diskon adalah {diskon_barang:.0f} dan total yang harus dibayar adalah {total_bayar:.0f}")
print(f"{diskon_barang:.0f} dibagi dengan 3 sisanya {sisa_baginya}")

                            