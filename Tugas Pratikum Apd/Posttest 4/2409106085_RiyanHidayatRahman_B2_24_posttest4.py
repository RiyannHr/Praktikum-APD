print("Selamat Datang di Praktikum")
print("Silahkan Login Terlebih Dahulu")
    
 # Informasi username dan password yang benar
id = "Riyan"  # Ganti dengan nama Anda sebagai username
pw = "85"  # NIM 085, angka 0 di depan diabaikan
count = 1
batas = 4

while count < batas:
        username = input("Masukkan Username Anda = ")
        password = input("Masukkan 3 digit terakhir NIM Anda (tanpa angka 0 di depan jika ada) = ")
    
    
        if username == id and password == pw:
            print("Anda berhasil login")
            print(" ")
            
            # Lanjutkan ke program utama
            print("MARI MENGHITUNG BERAT IDEAL ANDA!!!")
            BeratMg = float(input("Masukkan berat badan anda (dalam Mg) = "))
            Berat = BeratMg / 1000000

            TinggiKm = float(input("Masukkan Tinggi badan anda (dalam Km) = "))
            Tinggi = TinggiKm * 1000

            BMI = Berat / (Tinggi ** 2)

            if BMI < 18.5:
                print("Kategori Berat badan anda (UnderWeight)")
            elif BMI < 24.9:
                print("Kategori Berat badan anda (Normal)")
            elif BMI < 29.9:
                print("Kategori Berat badan anda (OverWeight)")
            else:
                print("Kategori Berat Badan Anda (Obesitas)")

            print(f"BMI Anda adalah {BMI :.2f}")
            print("Pilih Apa yang Anda Ingin Lakukan:")
            
            print("""  
                      ya = Kembali ke program
                      tidak = Keluar
            """)
            
            menu = (input("Masukkan Pilihan Anda (ya/tidak) = "))
            if menu == "ya":
                continue  # Mulai ulang program
            elif menu == "tidak":
                print("Terima Kasih Sudah Mampir")
                break
        else:
            count += 1
            print("Username atau password salah.")
            print(f"Jumlah kesalahan anda Sebanyak : {count - 1} kali ")
        
    
if count == batas:
        print(f"Anda telah gagal login. Program berhenti.")
        

