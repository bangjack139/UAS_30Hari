def penghitung_huruf_vokal():
    kalimat = input("Masukkan sebuah kalimat: ")
    vokal = "aeiouAEIOU"
    jumlah_vokal = sum(1 for huruf in kalimat if huruf in vokal)
    
    print(f"Jumlah huruf vokal: {jumlah_vokal}")

penghitung_huruf_vokal()