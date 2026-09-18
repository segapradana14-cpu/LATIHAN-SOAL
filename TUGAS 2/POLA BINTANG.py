# PROGRAM SOAL FORMASI BINTANG (NOMOR 1 - 20)
# Setiap kali selesai menjawab satu soal, program akan bertanya lagi
# mau menjawab soal nomor berapa. Ketik 0 untuk keluar.
#
# Catatan: soal nomor 3 dan 6, serta nomor 15 dan 16, terlihat
# menghasilkan bentuk yang sama persis pada gambar soal, jadi kodenya
# dibuat sama.
#
# Cara menjalankan: python soal-bintang-1-20.py

while True:
    print("===========================================")
    print("  DAFTAR SOAL FORMASI BINTANG")
    print("===========================================")
    print("Pilih nomor soal dari 1 sampai 20")
    print("Ketik 0 untuk keluar")
    print("-------------------------------------------")

    teks_nomor = input("Pilih nomor soal (1-20) : ")

    if teks_nomor == "0":
        print()
        print("Sampai jumpa!")
        break

    nomor = int(teks_nomor)
    print()

    # =====================================================
    # SOAL 1 : Segitiga terbalik menyatu di tengah (jam pasir bagian atas)
    # Baris pertama penuh 11 bintang, baris berikutnya terbelah dua
    # dengan celah tengah yang makin lebar
    # =====================================================
    if nomor == 1:
        baris = 1
        while baris <= 6:
            if baris == 1:
                print("*" * 11)
            else:
                kiri = 7 - baris
                spasi_tengah = 2 * (baris - 1) - 1
                print("*" * kiri + " " * spasi_tengah + "*" * kiri)
            baris = baris + 1

    # =====================================================
    # SOAL 2 : Piramida menaik ke kanan
    # Jumlah bintang bertambah 2 setiap baris, spasi kiri berkurang 1
    # =====================================================
    elif nomor == 2:
        baris = 1
        while baris <= 6:
            spasi = 6 - baris
            bintang = 2 * baris - 1
            print(" " * spasi + "*" * bintang)
            baris = baris + 1

    # =====================================================
    # SOAL 3 : Dua segitiga siku bertumpuk (1,2,3 lalu 1,2,3 lagi)
    # =====================================================
    elif nomor == 3:
        baris = 1
        while baris <= 6:
            if baris <= 3:
                bintang = baris
            else:
                bintang = baris - 3
            print("*" * bintang)
            baris = baris + 1

    # =====================================================
    # SOAL 4 : Kebalikan soal 1 (celah tengah makin sempit, baris
    # terakhir menyatu penuh)
    # =====================================================
    elif nomor == 4:
        baris = 1
        while baris <= 6:
            if baris == 6:
                print("*" * 11)
            else:
                bintang = baris
                spasi_tengah = 11 - 2 * baris
                print("*" * bintang + " " * spasi_tengah + "*" * bintang)
            baris = baris + 1

    # =====================================================
    # SOAL 5 : Piramida menurun (kebalikan soal 2)
    # =====================================================
    elif nomor == 5:
        baris = 1
        while baris <= 6:
            spasi = baris - 1
            bintang = 13 - 2 * baris
            print(" " * spasi + "*" * bintang)
            baris = baris + 1

    # =====================================================
    # SOAL 6 : Sama seperti soal 3
    # =====================================================
    elif nomor == 6:
        baris = 1
        while baris <= 6:
            if baris <= 3:
                bintang = baris
            else:
                bintang = baris - 3
            print("*" * bintang)
            baris = baris + 1

    # =====================================================
    # SOAL 7 : Jam pasir vertikal (mengecil lalu membesar lagi)
    # =====================================================
    elif nomor == 7:
        baris = 1
        while baris <= 9:
            if baris <= 5:
                bintang = 6 - baris
            else:
                bintang = baris - 4
            print(" " + "*" * bintang)
            baris = baris + 1

    # =====================================================
    # SOAL 8 : Kotak dengan batas 0 di kiri, baris bawah semua 0
    # =====================================================
    elif nomor == 8:
        baris = 1
        while baris <= 5:
            print("0" + "*" * 10)
            baris = baris + 1
        print("0" * 11)

    # =====================================================
    # SOAL 9 : Sama seperti soal 8, tapi 0 di kanan
    # =====================================================
    elif nomor == 9:
        baris = 1
        while baris <= 5:
            print("*" * 10 + "0")
            baris = baris + 1
        print("0" * 11)

    # =====================================================
    # SOAL 10 : Jam pasir vertikal yang lebih besar (mirip soal 7,
    # tapi mulai dari 6)
    # =====================================================
    elif nomor == 10:
        baris = 1
        while baris <= 10:
            if baris <= 6:
                bintang = 7 - baris
            else:
                bintang = baris - 5
            print(" " + "*" * bintang)
            baris = baris + 1

    # =====================================================
    # SOAL 11 : Baris atas semua 0, sisanya seperti soal 8
    # =====================================================
    elif nomor == 11:
        print("0" * 11)
        baris = 1
        while baris <= 5:
            print("0" + "*" * 10)
            baris = baris + 1

    # =====================================================
    # SOAL 12 : Baris atas semua 0, sisanya seperti soal 9
    # =====================================================
    elif nomor == 12:
        print("0" * 11)
        baris = 1
        while baris <= 5:
            print("*" * 10 + "0")
            baris = baris + 1

    # =====================================================
    # SOAL 13 : Tangga 0 dari kiri atas menuju kanan bawah
    # =====================================================
    elif nomor == 13:
        baris = 1
        while baris <= 6:
            jumlah_nol = baris
            jumlah_bintang = 7 - baris
            print("0" * jumlah_nol + "*" * jumlah_bintang)
            baris = baris + 1

    # =====================================================
    # SOAL 14 : Tangga bintang dari kiri atas menuju kanan bawah
    # (kebalikan soal 13)
    # =====================================================
    elif nomor == 14:
        baris = 1
        while baris <= 6:
            jumlah_bintang = baris
            jumlah_nol = 7 - baris
            print("*" * jumlah_bintang + "0" * jumlah_nol)
            baris = baris + 1

    # =====================================================
    # SOAL 15 : Tangga 0 dari kanan atas menuju kiri bawah
    # (soal 13 dibalik urutan barisnya)
    # =====================================================
    elif nomor == 15:
        baris = 1
        while baris <= 6:
            jumlah_nol = 7 - baris
            jumlah_bintang = baris
            print("0" * jumlah_nol + "*" * jumlah_bintang)
            baris = baris + 1

    # =====================================================
    # SOAL 16 : Sama seperti soal 15
    # =====================================================
    elif nomor == 16:
        baris = 1
        while baris <= 6:
            jumlah_nol = 7 - baris
            jumlah_bintang = baris
            print("0" * jumlah_nol + "*" * jumlah_bintang)
            baris = baris + 1

    # =====================================================
    # SOAL 17 : Satu tanda bintang bergeser dari kanan ke kiri,
    # sisanya nol
    # =====================================================
    elif nomor == 17:
        baris = 1
        while baris <= 6:
            posisi_bintang = 8 - baris
            baris_teks = ""
            kolom = 1
            while kolom <= 7:
                if kolom == posisi_bintang:
                    baris_teks = baris_teks + "*"
                else:
                    baris_teks = baris_teks + "0"
                kolom = kolom + 1
            print(baris_teks)
            baris = baris + 1

    # =====================================================
    # SOAL 18 : Satu tanda bintang bergeser dari kiri ke kanan,
    # sisanya nol (kebalikan soal 17)
    # =====================================================
    elif nomor == 18:
        baris = 1
        while baris <= 6:
            posisi_bintang = baris
            baris_teks = ""
            kolom = 1
            while kolom <= 7:
                if kolom == posisi_bintang:
                    baris_teks = baris_teks + "*"
                else:
                    baris_teks = baris_teks + "0"
                kolom = kolom + 1
            print(baris_teks)
            baris = baris + 1

    # =====================================================
    # SOAL 19 : Kotak berbingkai 0 dengan bintang di dalamnya
    # =====================================================
    elif nomor == 19:
        print("0" * 7)
        baris = 1
        while baris <= 4:
            print("0" + "*" * 5 + "0")
            baris = baris + 1
        print("0" * 7)

    # =====================================================
    # SOAL 20 : Baris berselang-seling 0, bintang, dan sama dengan
    # =====================================================
    elif nomor == 20:
        print("0" * 7)
        print("*" * 7)
        print("=" * 7)
        print("0" * 7)
        print("*" * 7)
        print("=" * 7)

    # =====================================================
    # NOMOR DI LUAR 1-20
    # =====================================================
    else:
        print("Nomor soal harus antara 1 sampai 20.")

    print()
    print("=============================================")
    print()