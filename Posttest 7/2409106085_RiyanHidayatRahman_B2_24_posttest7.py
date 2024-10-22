# Variabel global
daftar_hp = {}
pengguna = {"pemilik": {"sandi": "123", "jabatan": "admin"}}
sedang_jalan = True
sudah_masuk = False
jabatan = ""

# Fungsi dengan parameter untuk menambah handphone ke dalam stok
def tambah_hp(merk, model, harga, stok):
    daftar_hp  # Mengakses variabel global
    daftar_hp[model] = {"merk": merk, "harga": harga, "stok": stok}
    return f"{merk} {model} berhasil ditambahkan ke stok."

# Fungsi rekursif untuk menampilkan stok handphone secara terbalik
def lihat_stok_terbalik(index):
    daftar_hp
    # Error handling
    if len(daftar_hp) == 0:
        return "Belum ada stok HP."
    if index < 0:
        return ""
    else:
        # Variabel lokal
        model = list(daftar_hp.keys())[index]
        hp = daftar_hp[model]
        result = f"{index + 1}. {hp['merk']} {model} - Harga: {hp['harga']}, Stok: {hp['stok']}\n"
        return result + lihat_stok_terbalik(index - 1)

# Fungsi untuk melihat stok
def lihat_stok():
    daftar_hp
    if len(daftar_hp) == 0:
        return "Belum ada stok HP."
    else:
        result = "Daftar HP yang tersedia:\n"
        for i, (model, hp) in enumerate(daftar_hp.items(), 1):
            result += f"{i}. {hp['merk']} {model} - Harga: {hp['harga']}, Stok: {hp['stok']}\n"
        return result

# Fungsi mengubah data
def ubah_hp(model, harga_baru, stok_baru):
    global daftar_hp
    if model in daftar_hp:
        daftar_hp[model]["harga"] = harga_baru
        daftar_hp[model]["stok"] = stok_baru
        return f"Data {model} telah diperbarui."
    else:
        return "Model tidak valid."

# Prosedur untuk menampilkan menu utama
def tampilkan_menu():
    print("\nSelamat datang di Toko Handphone ")
    print("1. Masuk ke sistem")
    print("2. Daftar pengguna baru")
    print("3. Tutup Toko")

# Prosedur untuk keluar dari sistem
def keluar_sistem(): 
    sudah_masuk = True
    print("Anda telah keluar dari sistem, sampai jumpa.")

# Fungsi untuk memeriksa input angka 
def input_angka(angka):
    nilai = input(angka)
    if nilai.isdigit():
        return int(nilai)
    else:
        print("Input tidak valid, harap masukkan angka.")
        return input_angka(angka)

# Program utama
while sedang_jalan:
    if not sudah_masuk:
        tampilkan_menu()
        pilih = input("Silakan pilih menu: ")

        if pilih == "1":
            nama = input("Masukkan nama: ")
            sandi = input("Masukkan sandi: ")
            if nama in pengguna and pengguna[nama]["sandi"] == sandi:
                sudah_masuk = True
                jabatan = pengguna[nama]["jabatan"]
                print(f"Selamat bekerja, {nama}!")
            else:
                print("Nama atau sandi salah, coba lagi.")

        elif pilih == "2":
            nama = input("Nama baru: ")
            if nama in pengguna:
                print("Nama ini sudah digunakan, silakan pilih yang lain.")
            else:
                sandi = input("Buat sandi baru: ")
                pengguna[nama] = {"sandi": sandi, "jabatan": "pegawai"}
                print("Pendaftaran berhasil, selamat bergabung!")

        elif pilih == "3":
            sedang_jalan = False
            print("Toko sudah tutup, sampai jumpa.")

        else:
            print("Pilihan tidak tersedia, coba lagi.")

    else:
        print("\nMenu Toko Handphone:")
        print("1. Tambah HP ke stok")
        print("2. Lihat stok HP")
        if jabatan == "admin":
            print("3. Ubah data HP")
            print("4. Hapus HP dari stok")
        print("5. Lihat stok HP secara terbalik")
        print("6. Keluar dari sistem")
        pilih = input("Silakan pilih menu: ")

        if pilih == "1":
            merk = input("Masukkan merk HP: ")
            model = input("Masukkan model HP: ")
            harga = input_angka("Harga HP: ")  
            stok = input_angka("Jumlah stok: ")  
            print(tambah_hp(merk, model, harga, stok))

        elif pilih == "2":
            print(lihat_stok())

        elif pilih == "3" and jabatan == "admin":
            if len(daftar_hp) == 0:
                print("Tidak ada HP untuk diubah.")
            else:
                model = input("Masukkan model HP yang diubah: ")
                harga_baru = input_angka("Masukkan harga baru: ")
                stok_baru = input_angka("Masukkan stok baru: ")
                print(ubah_hp(model, harga_baru, stok_baru))

        elif pilih == "4" and jabatan == "admin":
            if len(daftar_hp) == 0:
                print("Tidak ada HP untuk dihapus.")
            else:
                model = input("Masukkan model HP yang dihapus: ")
                if model in daftar_hp:
                    del daftar_hp[model]
                    print("HP telah dihapus dari stok.")
                else:
                    print("Model tidak valid, silakan coba lagi.")
        
        elif pilih == "5":
            print(lihat_stok_terbalik(len(daftar_hp) - 1))  # Memanggil fungsi rekursif
        
        elif pilih == "6":
            keluar_sistem()

        else:
            print("Pilihan tidak valid, coba lagi.")
