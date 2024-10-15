daftar_hp = {}
pengguna = {"pemilik": {"sandi": "123", "jabatan": "admin"}}
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
        print("5. Keluar dari sistem")
        pilih = input("Silakan pilih menu: ")

        if pilih == "1":
            merk = input("Masukkan merk HP: ")
            model = input("Masukkan model HP: ")
            harga = int(input("Harga HP: "))
            stok = int(input("Jumlah stok: "))
            daftar_hp[model] = {"merk": merk, "harga": harga, "stok": stok}
            print(f"{merk} {model} berhasil ditambahkan ke stok.")
        
        elif pilih == "2":
            if len(daftar_hp) == 0:
                print("Belum ada stok HP.")
            else:
                print("Daftar HP yang tersedia:")
                for i, (model, hp) in enumerate(daftar_hp.items(), 1):
                    print(f"{i}. {hp['merk']} {model} - Harga: {hp['harga']}, Stok: {hp['stok']}")
        
        elif pilih == "3" and jabatan == "admin":
            if len(daftar_hp) == 0:
                print("Tidak ada HP untuk diubah.")
            else:
                print("Pilih HP yang ingin diubah:")
                for i, (model, hp) in enumerate(daftar_hp.items(), 1):
                    print(f"{i}. {hp['merk']} {model} - Harga: {hp['harga']}, Stok: {hp['stok']}")
                model = input("Masukkan model HP yang diubah: ")
                if model in daftar_hp:
                    daftar_hp[model]["harga"] = int(input("Masukkan harga baru: "))
                    daftar_hp[model]["stok"] = int(input("Masukkan stok baru: "))
                    print("Data HP telah diperbarui.")
                else:
                    print("Model tidak valid, silakan ulangi.")
        
        elif pilih == "4" and jabatan == "admin":
            if len(daftar_hp) == 0:
                print("Tidak ada HP untuk dihapus.")
            else:
                print("Pilih HP yang ingin dihapus:")
                for i, (model, hp) in enumerate(daftar_hp.items(), 1):
                    print(f"{i}. {hp['merk']} {model} - Harga: {hp['harga']}, Stok: {hp['stok']}")
                model = input("Masukkan model HP yang dihapus: ")
                if model in daftar_hp:
                    del daftar_hp[model]
                    print("HP telah dihapus dari stok.")
                else:
                    print("Model tidak valid, silakan coba lagi.")
        
        elif pilih == "5":
            sudah_masuk = False
            print("Anda telah keluar dari sistem, sampai jumpa.")
        
        else:
            print("Pilihan tidak valid, coba lagi.")
