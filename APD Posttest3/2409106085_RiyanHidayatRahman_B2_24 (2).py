# Fungsi untuk menghitung BMI
def calculate_bmi(weight_mg, height_km):
    # Mengkonversi berat dari mg ke kg
    weight_kg = weight_mg / 1_000_000
    
    # Mengkonversi tinggi dari km ke meter
    height_meters = height_km * 1_000
    
    # Menghitung BMI
    bmi = weight_kg / (height_meters ** 2)
    
    # Menentukan kategori BMI
    if bmi < 18.5:
        category = "Berat badan kurang (Underweight)"
    elif bmi < 24.9:
        category = "Berat badan normal (Normal)"
    elif bmi < 29.9:
        category = "Berat badan berlebih (Overweight)"
    else:
        category = "Obesitas (Obese)"
    
    return bmi, category

# Meminta input berat badan dalam mg dan tinggi badan dalam km
weight_mg = float(input("Masukkan berat badan dalam mg: "))
height_km = float(input("Masukkan tinggi badan dalam km: "))

# Menghitung BMI dan mendapatkan kategori
bmi, category = calculate_bmi(weight_mg, height_km)

# Menampilkan hasil
print(f"Nilai BMI Anda adalah: {bmi:.2f}")
print(f"Kategori: {category}")
