def kalkulator_bmi():
    berat = float(input("Masukkan berat badan (kg): "))
    tinggi = float(input("Masukkan tinggi badan (m): "))
    
    bmi = berat / (tinggi ** 2)
    print(f"BMI: {bmi:.2f}")

kalkulator_bmi()
