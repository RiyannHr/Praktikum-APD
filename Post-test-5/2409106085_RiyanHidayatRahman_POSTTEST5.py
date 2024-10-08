# Data awal
daftar_hp = []
pengguna = [["pemilik", "123", "admin"]]
sedang_jalan = True
sudah_masuk = False
jabatan = ""

# Program utama
while sedang_jalan:
    if not sudah_masuk:
        print("\nSelamat datang di Toko Handphone ")
        print("1. Masuk ke sistem")
        print("2. Daftar pengguna baru")
        print("3. Tutup Toko")
        pilih = input("Silakan pilih menu: ")

        if pilih == "1":
            nama = input("Masukkan nama: ")
            sandi = input("Masukkan sandi: ")
            ketemu = False
            for p in pengguna:
                if p[0] == nama and p[1] == sandi:
                    ketemu = True
                    sudah_masuk = True
                    jabatan = p[2]
                    print(f"Selamat bekerja, {nama}!")
                    break
            if not ketemu:
                print("Nama atau sandi salah, coba lagi.")

        elif pilih == "2":
            nama = input("Nama baru: ")
            ada = False
            for p in pengguna:
                if p[0] == nama:
                    ada = True
                    break
            if ada:
                print("Nama ini sudah digunakan, silakan pilih yang lain.")
            else:
                sandi = input("Buat sandi baru: ")
                pengguna.append([nama, sandi, "pegawai"])
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
        print("5. Keluar dari sistem")
        pilih = input("Silakan pilih menu: ")

        if pilih == "1":
            merk = input("Masukkan merk HP: ")
            model = input("Masukkan model HP: ")
            harga = int(input("Harga HP: "))
            stok = int(input("Jumlah stok: "))
            daftar_hp.append([merk, model, harga, stok])
            print(f"{merk} {model} berhasil ditambahkan ke stok.")
        
        elif pilih == "2":
            if len(daftar_hp) == 0:
                print("Belum ada stok HP.")
            else:
                print("Daftar HP yang tersedia:")
                for i, hp in enumerate(daftar_hp, 1):
                    print(f"{i}. {hp[0]} {hp[1]} - Harga: {hp[2]}, Stok: {hp[3]}")
        
        elif pilih == "3" and jabatan == "admin":
            if len(daftar_hp) == 0:
                print("Tidak ada HP untuk diubah.")
            else:
                print("Pilih HP yang ingin diubah:")
                for i, hp in enumerate(daftar_hp, 1):
                    print(f"{i}. {hp[0]} {hp[1]} - Harga: {hp[2]}, Stok: {hp[3]}")
                nomor = int(input("Masukkan nomor HP yang diubah: ")) - 1
                if 0 <= nomor < len(daftar_hp):
                    hp = daftar_hp[nomor]
                    hp[2] = int(input("Masukkan harga baru: "))
                    hp[3] = int(input("Masukkan stok baru: "))
                    print("Data HP telah diperbarui.")
                else:
                    print("Nomor tidak valid, silakan ulangi.")
        
        elif pilih == "4" and jabatan == "admin":
            if len(daftar_hp) == 0:
                print("Tidak ada HP untuk dihapus.")
            else:
                print("Pilih HP yang ingin dihapus:")
                for i, hp in enumerate(daftar_hp, 1):
                    print(f"{i}. {hp[0]} {hp[1]} - Harga: {hp[2]}, Stok: {hp[3]}")
                nomor = int(input("Masukkan nomor HP yang dihapus: ")) - 1
                if 0 <= nomor < len(daftar_hp):
                    del daftar_hp[nomor]
                    print("HP telah dihapus dari stok.")
                else:
                    print("Nomor tidak valid, silakan coba lagi.")
        
        elif pilih == "5":
            sudah_masuk = False
            print("Anda telah keluar dari sistem, sampai jumpa.")
        
        else:
            print("Pilihan tidak valid, coba lagi.")
