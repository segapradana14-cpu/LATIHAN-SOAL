# PROGRAM SOAL ALGORITMA DAN PEMROGRAMAN (NOMOR 1 - 50)
# Semua soal digabung dalam satu file. Setiap kali selesai menjawab satu
# soal, program akan bertanya lagi mau menjawab soal nomor berapa.
# Ketik 0 untuk keluar dari program.
#
# Cara menjalankan: python soal-algoritma-1-50.py

while True:
    print("===========================================")
    print("  DAFTAR SOAL ALGORITMA DAN PEMROGRAMAN")
    print("===========================================")
    print("1-3   : Kalimat dan String")
    print("4-15  : Pola Angka")
    print("16-21 : Deret Angka")
    print("22-23 : Faktorial dan Fibonacci")
    print("24-33 : Tahun Kabisat dan Habis Dibagi")
    print("34-41 : Animasi Angka 0")
    print("42-45 : Input Beberapa Angka")
    print("46-50 : Total dan Bilangan Prima")
    print("-------------------------------------------")
    print("Ketik 0 untuk keluar")
    print("-------------------------------------------")

    teks_nomor = input("Pilih nomor soal (1-50) : ")

    if teks_nomor == "0":
        print()
        print("Sampai jumpa!")
        break

    nomor = int(teks_nomor)

    # =====================================================
    # SOAL 1 : Membalik kalimat
    # =====================================================
    if nomor == 1:
        kalimat = input("Masukkan kalimat : ")

        hasil = ""
        i = len(kalimat) - 1
        while i >= 0:
            hasil = hasil + kalimat[i]
            i = i - 1

        print()
        print("Kalimat asli     :", kalimat)
        print("Kalimat terbalik :", hasil)

    # =====================================================
    # SOAL 2 : Mencari dan menghitung huruf tertentu
    # =====================================================
    elif nomor == 2:
        kalimat = input("Masukkan kalimat : ")
        huruf = input("Huruf yang dicari : ")

        if len(huruf) != 1:
            print()
            print("Masukkan tepat satu karakter untuk dicari.")
        else:
            huruf_kecil = huruf.lower()
            jumlah = 0
            posisi = ""

            i = 0
            while i < len(kalimat):
                if kalimat[i].lower() == huruf_kecil:
                    jumlah = jumlah + 1
                    if posisi == "":
                        posisi = str(i + 1)
                    else:
                        posisi = posisi + ", " + str(i + 1)
                i = i + 1

            print()
            print("Kalimat          :", kalimat)
            print("Huruf dicari     :", huruf)
            print("Jumlah ditemukan :", jumlah, "kali")
            if jumlah > 0:
                print("Posisi karakter  :", posisi)

    # =====================================================
    # SOAL 3 : Menghitung jumlah karakter
    # =====================================================
    elif nomor == 3:
        kalimat = input("Masukkan kalimat : ")

        total = len(kalimat)
        spasi = 0
        for huruf in kalimat:
            if huruf == " ":
                spasi = spasi + 1

        print()
        print("Jumlah karakter (semua)   :", total)
        print("Jumlah spasi              :", spasi)
        print("Jumlah karakter non-spasi :", total - spasi)

    # =====================================================
    # SOAL 4 : 122333444455555666666
    # Angka n diulang sebanyak n kali, n dari 1 sampai 6
    # =====================================================
    elif nomor == 4:
        hasil = ""
        n = 1
        while n <= 6:
            i = 1
            while i <= n:
                hasil = hasil + str(n)
                i = i + 1
            n = n + 1

        print()
        print(hasil)

    # =====================================================
    # SOAL 5 : 666666555554444333221
    # Sama seperti soal 4, tapi n dari 6 turun ke 1
    # =====================================================
    elif nomor == 5:
        hasil = ""
        n = 6
        while n >= 1:
            i = 1
            while i <= n:
                hasil = hasil + str(n)
                i = i + 1
            n = n - 1

        print()
        print(hasil)

    # =====================================================
    # SOAL 6 : 112123123412345123456
    # Deret naik 1..n, n dari 1 sampai 6
    # =====================================================
    elif nomor == 6:
        hasil = ""
        n = 1
        while n <= 6:
            i = 1
            while i <= n:
                hasil = hasil + str(i)
                i = i + 1
            n = n + 1

        print()
        print(hasil)

    # =====================================================
    # SOAL 7 : 654321543214321321211
    # Deret turun n..1, n dari 6 sampai 1
    # =====================================================
    elif nomor == 7:
        hasil = ""
        n = 6
        while n >= 1:
            i = n
            while i >= 1:
                hasil = hasil + str(i)
                i = i - 1
            n = n - 1

        print()
        print(hasil)

    # =====================================================
    # SOAL 8 : 112333123455555123456
    # n ganjil -> angka diulang, n genap -> deret naik
    # =====================================================
    elif nomor == 8:
        hasil = ""
        n = 1
        while n <= 6:
            if n % 2 == 1:
                i = 1
                while i <= n:
                    hasil = hasil + str(n)
                    i = i + 1
            else:
                i = 1
                while i <= n:
                    hasil = hasil + str(i)
                    i = i + 1
            n = n + 1

        print()
        print(hasil)

    # =====================================================
    # SOAL 9 : 122123444412345666666
    # Kebalikan soal 8: n ganjil -> deret naik, n genap -> diulang
    # =====================================================
    elif nomor == 9:
        hasil = ""
        n = 1
        while n <= 6:
            if n % 2 == 1:
                i = 1
                while i <= n:
                    hasil = hasil + str(i)
                    i = i + 1
            else:
                i = 1
                while i <= n:
                    hasil = hasil + str(n)
                    i = i + 1
            n = n + 1

        print()
        print(hasil)

    # =====================================================
    # SOAL 10 : 654321555554321333211
    # n dari 6 turun ke 1: n genap -> deret turun, n ganjil -> diulang
    # =====================================================
    elif nomor == 10:
        hasil = ""
        n = 6
        while n >= 1:
            if n % 2 == 0:
                i = n
                while i >= 1:
                    hasil = hasil + str(i)
                    i = i - 1
            else:
                i = 1
                while i <= n:
                    hasil = hasil + str(n)
                    i = i + 1
            n = n - 1

        print()
        print(hasil)

    # =====================================================
    # SOAL 11 : 666666123454444123221
    # n dari 6 turun ke 1: n genap -> diulang, n ganjil -> deret naik
    # =====================================================
    elif nomor == 11:
        hasil = ""
        n = 6
        while n >= 1:
            if n % 2 == 0:
                i = 1
                while i <= n:
                    hasil = hasil + str(n)
                    i = i + 1
            else:
                i = 1
                while i <= n:
                    hasil = hasil + str(i)
                    i = i + 1
            n = n - 1

        print()
        print(hasil)

    # =====================================================
    # SOAL 12 : 122123123455555666666123456712345678999999999
    # Baris 1 = naik, baris 2 = ulang, lalu berpasangan naik-naik/ulang-ulang
    # =====================================================
    elif nomor == 12:
        hasil = ""
        n = 1
        while n <= 9:
            if n == 1:
                tipe = "naik"
            elif n == 2:
                tipe = "ulang"
            else:
                pasangan = (n - 3) // 2
                if pasangan % 2 == 0:
                    tipe = "naik"
                else:
                    tipe = "ulang"

            if tipe == "naik":
                i = 1
                while i <= n:
                    hasil = hasil + str(i)
                    i = i + 1
            else:
                i = 1
                while i <= n:
                    hasil = hasil + str(n)
                    i = i + 1
            n = n + 1

        print()
        print(hasil)

    # =====================================================
    # SOAL 13 : 112333444412345123456777777788888888123456789
    # Kebalikan aturan soal 12
    # =====================================================
    elif nomor == 13:
        hasil = ""
        n = 1
        while n <= 9:
            if n == 1:
                tipe = "naik"
            elif n == 2:
                tipe = "ulang"
            else:
                pasangan = (n - 3) // 2
                if pasangan % 2 == 0:
                    tipe = "naik"
                else:
                    tipe = "ulang"

            if tipe == "naik":
                i = 1
                while i <= n:
                    hasil = hasil + str(n)
                    i = i + 1
            else:
                i = 1
                while i <= n:
                    hasil = hasil + str(i)
                    i = i + 1
            n = n + 1

        print()
        print(hasil)

    # =====================================================
    # SOAL 14 : 888888887777777654321543214444333211
    # n dari 8 turun ke 1, berpasangan: ulang, turun, ulang, turun
    # =====================================================
    elif nomor == 14:
        hasil = ""
        n = 8
        while n >= 1:
            pasangan = (8 - n) // 2
            if pasangan % 2 == 0:
                tipe = "ulang"
            else:
                tipe = "turun"

            if tipe == "ulang":
                i = 1
                while i <= n:
                    hasil = hasil + str(n)
                    i = i + 1
            else:
                i = n
                while i >= 1:
                    hasil = hasil + str(i)
                    i = i - 1
            n = n - 1

        print()
        print(hasil)

    # =====================================================
    # SOAL 15 : 876543217654321666666555554321321221
    # Kebalikan aturan soal 14
    # =====================================================
    elif nomor == 15:
        hasil = ""
        n = 8
        while n >= 1:
            pasangan = (8 - n) // 2
            if pasangan % 2 == 0:
                tipe = "ulang"
            else:
                tipe = "turun"

            if tipe == "ulang":
                i = n
                while i >= 1:
                    hasil = hasil + str(i)
                    i = i - 1
            else:
                i = 1
                while i <= n:
                    hasil = hasil + str(n)
                    i = i + 1
            n = n - 1

        print()
        print(hasil)

    # =====================================================
    # SOAL 16 : 1 5 3 7 5 9 7 11 9 13 11 15  =>  n+4, n-2, ...
    # =====================================================
    elif nomor == 16:
        hasil = ""
        n = 1
        i = 0
        while i < 12:
            if hasil == "":
                hasil = str(n)
            else:
                hasil = hasil + " " + str(n)

            if i % 2 == 0:
                n = n + 4
            else:
                n = n - 2
            i = i + 1

        print()
        print(hasil)

    # =====================================================
    # SOAL 17 : 2 12 7 17 12 22 17 27 22 32  =>  n+10, n-5, ...
    # =====================================================
    elif nomor == 17:
        hasil = ""
        n = 2
        i = 0
        while i < 10:
            if hasil == "":
                hasil = str(n)
            else:
                hasil = hasil + " " + str(n)

            if i % 2 == 0:
                n = n + 10
            else:
                n = n - 5
            i = i + 1

        print()
        print(hasil)

    # =====================================================
    # SOAL 18 : 5 2 7 4 9 6 11 8 13 10 15 12  =>  n-3, n+5, ...
    # =====================================================
    elif nomor == 18:
        hasil = ""
        n = 5
        i = 0
        while i < 12:
            if hasil == "":
                hasil = str(n)
            else:
                hasil = hasil + " " + str(n)

            if i % 2 == 0:
                n = n - 3
            else:
                n = n + 5
            i = i + 1

        print()
        print(hasil)

    # =====================================================
    # SOAL 19 : 3 9 4 12 7 21 16 48 43 129  =>  n*3, n-5, ...
    # =====================================================
    elif nomor == 19:
        hasil = ""
        n = 3
        i = 0
        while i < 10:
            if hasil == "":
                hasil = str(n)
            else:
                hasil = hasil + " " + str(n)

            if i % 2 == 0:
                n = n * 3
            else:
                n = n - 5
            i = i + 1

        print()
        print(hasil)

    # =====================================================
    # SOAL 20 : 1 2 4 7 8 10 13 14 16 19 20 22 25  =>  n+1, n+2, n+3, ...
    # =====================================================
    elif nomor == 20:
        hasil = ""
        n = 1
        i = 0
        while i < 13:
            if hasil == "":
                hasil = str(n)
            else:
                hasil = hasil + " " + str(n)

            sisa = i % 3
            if sisa == 0:
                n = n + 1
            elif sisa == 1:
                n = n + 2
            else:
                n = n + 3
            i = i + 1

        print()
        print(hasil)

    # =====================================================
    # SOAL 21 : 1 2 4 8 16 32 64 128 256 512  =>  n*2
    # =====================================================
    elif nomor == 21:
        hasil = ""
        n = 1
        i = 0
        while i < 10:
            if hasil == "":
                hasil = str(n)
            else:
                hasil = hasil + " " + str(n)
            n = n * 2
            i = i + 1

        print()
        print(hasil)

    # =====================================================
    # SOAL 22 : Faktorial n!
    # =====================================================
    elif nomor == 22:
        n = int(input("Masukkan nilai n : "))

        if n < 0:
            print()
            print("Nilai n harus bilangan bulat >= 0.")
        elif n == 0:
            print()
            print("0! = 1")
        else:
            uraian = ""
            hasil = 1
            i = n
            while i >= 1:
                if uraian == "":
                    uraian = str(i)
                else:
                    uraian = uraian + " x " + str(i)
                hasil = hasil * i
                i = i - 1

            print()
            print(str(n) + "! = " + uraian + " = " + str(hasil))

    # =====================================================
    # SOAL 23 : Deret Fibonacci
    # =====================================================
    elif nomor == 23:
        maksimum = int(input("Nilai maksimum Fibonacci : "))

        if maksimum < 0:
            print()
            print("Nilai maksimum harus bilangan >= 0.")
        else:
            deret = ""
            banyak_suku = 0
            a = 0
            b = 1

            while a <= maksimum:
                if deret == "":
                    deret = str(a)
                else:
                    deret = deret + ", " + str(a)
                banyak_suku = banyak_suku + 1

                berikutnya = a + b
                a = b
                b = berikutnya

            print()
            print("Deret :", deret)
            print("Banyaknya suku :", banyak_suku)

    # =====================================================
    # SOAL 24-28 : Tahun kabisat berakhiran digit tertentu
    # =====================================================
    elif nomor == 24 or nomor == 25 or nomor == 26 or nomor == 27 or nomor == 28:
        awal = int(input("Masukkan n_awal  : "))
        akhir = int(input("Masukkan n_akhir : "))

        if awal > akhir:
            print()
            print("Periksa kembali n_awal dan n_akhir.")
        else:
            if nomor == 24:
                digit_akhir = 0
            elif nomor == 25:
                digit_akhir = 2
            elif nomor == 26:
                digit_akhir = 4
            elif nomor == 27:
                digit_akhir = 6
            else:
                digit_akhir = 8

            hasil = ""
            jumlah = 0
            tahun = awal
            while tahun <= akhir:
                kabisat = False
                if tahun % 4 == 0 and tahun % 100 != 0:
                    kabisat = True
                if tahun % 400 == 0:
                    kabisat = True

                if kabisat and tahun % 10 == digit_akhir:
                    if hasil == "":
                        hasil = str(tahun)
                    else:
                        hasil = hasil + ", " + str(tahun)
                    jumlah = jumlah + 1
                tahun = tahun + 1

            print()
            print("Tahun kabisat berakhiran " + str(digit_akhir) + " dari " + str(awal) + " sampai " + str(akhir) + ":")
            if jumlah == 0:
                print("(tidak ada yang memenuhi)")
            else:
                print(hasil)
                print()
                print("Banyaknya :", jumlah, "tahun")

    # =====================================================
    # SOAL 29-33 : Bilangan habis dibagi
    # =====================================================
    elif nomor == 29 or nomor == 30 or nomor == 31 or nomor == 32 or nomor == 33:
        awal = int(input("Masukkan n_awal  : "))
        akhir = int(input("Masukkan n_akhir : "))

        if awal > akhir:
            print()
            print("Periksa kembali n_awal dan n_akhir.")
        else:
            if nomor == 29:
                pembagi = 3
            elif nomor == 30:
                pembagi = 4
            elif nomor == 31:
                pembagi = 5
            elif nomor == 32:
                pembagi = 6
            else:
                pembagi = 7

            hasil = ""
            jumlah = 0
            angka = awal
            while angka <= akhir:
                if angka % pembagi == 0:
                    if hasil == "":
                        hasil = str(angka)
                    else:
                        hasil = hasil + ", " + str(angka)
                    jumlah = jumlah + 1
                angka = angka + 1

            print()
            print("Bilangan habis dibagi " + str(pembagi) + " dari " + str(awal) + " sampai " + str(akhir) + ":")
            if jumlah == 0:
                print("(tidak ada yang memenuhi)")
            else:
                print(hasil)
                print()
                print("Banyaknya :", jumlah, "bilangan")

    # =====================================================
    # SOAL 34-41 : Animasi angka 0 berjalan di layar
    # =====================================================
    elif nomor >= 34 and nomor <= 41:
        import os
        import shutil
        import sys
        import time

        if os.name == "nt":
            os.system("")

        ukuran = shutil.get_terminal_size(fallback=(80, 24))
        kolom_kanan = ukuran.columns
        baris_bawah = ukuran.lines
        kolom_kiri = 1
        baris_atas = 1

        daftar_baris = []
        daftar_kolom = []

        if nomor == 34:
            # kiri atas -> kanan atas, diulang lagi dari kiri ke kanan
            kolom = kolom_kiri
            while kolom <= kolom_kanan:
                daftar_baris.append(baris_atas)
                daftar_kolom.append(kolom)
                kolom = kolom + 1
            kolom = kolom_kiri
            while kolom <= kolom_kanan:
                daftar_baris.append(baris_atas)
                daftar_kolom.append(kolom)
                kolom = kolom + 1

        elif nomor == 35:
            # kiri atas -> kanan atas, lalu kembali dari kanan ke kiri
            kolom = kolom_kiri
            while kolom <= kolom_kanan:
                daftar_baris.append(baris_atas)
                daftar_kolom.append(kolom)
                kolom = kolom + 1
            kolom = kolom_kanan
            while kolom >= kolom_kiri:
                daftar_baris.append(baris_atas)
                daftar_kolom.append(kolom)
                kolom = kolom - 1

        elif nomor == 36:
            # kiri bawah -> kanan bawah, diulang lagi dari kiri ke kanan
            kolom = kolom_kiri
            while kolom <= kolom_kanan:
                daftar_baris.append(baris_bawah)
                daftar_kolom.append(kolom)
                kolom = kolom + 1
            kolom = kolom_kiri
            while kolom <= kolom_kanan:
                daftar_baris.append(baris_bawah)
                daftar_kolom.append(kolom)
                kolom = kolom + 1

        elif nomor == 37:
            # kiri bawah -> kanan bawah, lalu kembali dari kanan ke kiri
            kolom = kolom_kiri
            while kolom <= kolom_kanan:
                daftar_baris.append(baris_bawah)
                daftar_kolom.append(kolom)
                kolom = kolom + 1
            kolom = kolom_kanan
            while kolom >= kolom_kiri:
                daftar_baris.append(baris_bawah)
                daftar_kolom.append(kolom)
                kolom = kolom - 1

        elif nomor == 38:
            # kiri atas -> kiri bawah, diulang lagi dari atas ke bawah
            baris = baris_atas
            while baris <= baris_bawah:
                daftar_baris.append(baris)
                daftar_kolom.append(kolom_kiri)
                baris = baris + 1
            baris = baris_atas
            while baris <= baris_bawah:
                daftar_baris.append(baris)
                daftar_kolom.append(kolom_kiri)
                baris = baris + 1

        elif nomor == 39:
            # kiri atas -> kiri bawah, lalu kembali dari bawah ke atas
            baris = baris_atas
            while baris <= baris_bawah:
                daftar_baris.append(baris)
                daftar_kolom.append(kolom_kiri)
                baris = baris + 1
            baris = baris_bawah
            while baris >= baris_atas:
                daftar_baris.append(baris)
                daftar_kolom.append(kolom_kiri)
                baris = baris - 1

        elif nomor == 40:
            # kanan atas -> kanan bawah, diulang lagi dari atas ke bawah
            baris = baris_atas
            while baris <= baris_bawah:
                daftar_baris.append(baris)
                daftar_kolom.append(kolom_kanan)
                baris = baris + 1
            baris = baris_atas
            while baris <= baris_bawah:
                daftar_baris.append(baris)
                daftar_kolom.append(kolom_kanan)
                baris = baris + 1

        else:
            # nomor == 41 : kanan atas -> kanan bawah, lalu kembali dari bawah ke atas
            baris = baris_atas
            while baris <= baris_bawah:
                daftar_baris.append(baris)
                daftar_kolom.append(kolom_kanan)
                baris = baris + 1
            baris = baris_bawah
            while baris >= baris_atas:
                daftar_baris.append(baris)
                daftar_kolom.append(kolom_kanan)
                baris = baris - 1

        sys.stdout.write("\x1b[?25l")  # sembunyikan kursor
        sys.stdout.flush()

        # Dibungkus try/finally supaya kursor PASTI dikembalikan normal
        # dan layar PASTI dibersihkan, walaupun animasi dihentikan paksa
        # (misalnya ditekan Ctrl+C) atau terjadi error di tengah jalan.
        try:
            i = 0
            while i < len(daftar_baris):
                sys.stdout.write("\x1b[2J\x1b[H")
                sys.stdout.write("\x1b[" + str(daftar_baris[i]) + ";" + str(daftar_kolom[i]) + "H0")
                sys.stdout.flush()
                time.sleep(0.06)
                i = i + 1
        finally:
            sys.stdout.write("\x1b[2J\x1b[H")
            sys.stdout.write("\x1b[?25h")  # tampilkan kembali kursor
            sys.stdout.flush()

        print("Animasi soal " + str(nomor) + " selesai.")

    # =====================================================
    # SOAL 42 : Cari bilangan terbesar
    # SOAL 43 : Cari bilangan terkecil
    # SOAL 44 : Hitung jumlah bilangan genap
    # SOAL 45 : Hitung jumlah bilangan ganjil
    # =====================================================
    elif nomor == 42 or nomor == 43 or nomor == 44 or nomor == 45:
        banyak = int(input("Berapa angka yang ingin dimasukkan (minimal 10) : "))
        while banyak < 10:
            print("Jumlah data minimal 10.")
            banyak = int(input("Ulangi jumlah data : "))

        angka = []
        i = 1
        while i <= banyak:
            nilai = int(input("Angka ke-" + str(i) + " : "))
            angka.append(nilai)
            i = i + 1

        teks_data = ""
        for a in angka:
            if teks_data == "":
                teks_data = str(a)
            else:
                teks_data = teks_data + ", " + str(a)

        print()
        print("Data:", teks_data)
        print("-------------------------------------------")

        if nomor == 42:
            terbesar = angka[0]
            i = 1
            while i < len(angka):
                if angka[i] > terbesar:
                    terbesar = angka[i]
                i = i + 1
            print("Bilangan terbesar :", terbesar)

        elif nomor == 43:
            terkecil = angka[0]
            i = 1
            while i < len(angka):
                if angka[i] < terkecil:
                    terkecil = angka[i]
                i = i + 1
            print("Bilangan terkecil :", terkecil)

        elif nomor == 44:
            teks_genap = ""
            banyak_genap = 0
            total_genap = 0
            for a in angka:
                if a % 2 == 0:
                    if teks_genap == "":
                        teks_genap = str(a)
                    else:
                        teks_genap = teks_genap + ", " + str(a)
                    banyak_genap = banyak_genap + 1
                    total_genap = total_genap + a

            if teks_genap == "":
                teks_genap = "-"
            print("Bilangan genap :", teks_genap)
            print("Banyaknya      :", banyak_genap, " Jumlah nilainya :", total_genap)

        else:
            teks_ganjil = ""
            banyak_ganjil = 0
            total_ganjil = 0
            for a in angka:
                if a % 2 != 0:
                    if teks_ganjil == "":
                        teks_ganjil = str(a)
                    else:
                        teks_ganjil = teks_ganjil + ", " + str(a)
                    banyak_ganjil = banyak_ganjil + 1
                    total_ganjil = total_ganjil + a

            if teks_ganjil == "":
                teks_ganjil = "-"
            print("Bilangan ganjil :", teks_ganjil)
            print("Banyaknya       :", banyak_ganjil, " Jumlah nilainya :", total_ganjil)

    # =====================================================
    # SOAL 46-50 : Total bilangan dan bilangan prima
    # =====================================================
    elif nomor >= 46 and nomor <= 50:
        awal = int(input("Masukkan n_awal  : "))
        akhir = int(input("Masukkan n_akhir : "))

        if awal > akhir:
            print()
            print("Periksa kembali n_awal dan n_akhir.")

        elif nomor == 46:
            hasil = ""
            jumlah = 0
            total = 0
            n = awal
            while n <= akhir:
                if n > 0:
                    if hasil == "":
                        hasil = str(n)
                    else:
                        hasil = hasil + ", " + str(n)
                    jumlah = jumlah + 1
                    total = total + n
                n = n + 1

            print()
            print("Bilangan bulat positif " + str(awal) + ".." + str(akhir) + ":")
            print(hasil if hasil != "" else "(tidak ada)")
            print()
            print("Banyaknya :", jumlah, " Total :", total)

        elif nomor == 47:
            hasil = ""
            jumlah = 0
            total = 0
            n = awal
            while n <= akhir:
                if n % 2 == 0:
                    if hasil == "":
                        hasil = str(n)
                    else:
                        hasil = hasil + ", " + str(n)
                    jumlah = jumlah + 1
                    total = total + n
                n = n + 1

            print()
            print("Bilangan genap " + str(awal) + ".." + str(akhir) + ":")
            print(hasil if hasil != "" else "(tidak ada)")
            print()
            print("Banyaknya :", jumlah, " Total :", total)

        elif nomor == 48:
            hasil = ""
            jumlah = 0
            total = 0
            n = awal
            while n <= akhir:
                if n % 2 != 0:
                    if hasil == "":
                        hasil = str(n)
                    else:
                        hasil = hasil + ", " + str(n)
                    jumlah = jumlah + 1
                    total = total + n
                n = n + 1

            print()
            print("Bilangan ganjil " + str(awal) + ".." + str(akhir) + ":")
            print(hasil if hasil != "" else "(tidak ada)")
            print()
            print("Banyaknya :", jumlah, " Total :", total)

        elif nomor == 49:
            hasil = ""
            jumlah = 0
            n = awal
            while n <= akhir:
                prima = True
                if n < 2:
                    prima = False
                else:
                    pembagi = 2
                    while pembagi < n:
                        if n % pembagi == 0:
                            prima = False
                        pembagi = pembagi + 1

                if prima:
                    if hasil == "":
                        hasil = str(n)
                    else:
                        hasil = hasil + ", " + str(n)
                    jumlah = jumlah + 1
                n = n + 1

            print()
            print("Bilangan prima " + str(awal) + ".." + str(akhir) + ":")
            print(hasil if hasil != "" else "(tidak ada)")
            print()
            print("Banyaknya bilangan prima :", jumlah)

        else:
            jumlah = 0
            total = 0
            n = awal
            while n <= akhir:
                prima = True
                if n < 2:
                    prima = False
                else:
                    pembagi = 2
                    while pembagi < n:
                        if n % pembagi == 0:
                            prima = False
                        pembagi = pembagi + 1

                if prima:
                    jumlah = jumlah + 1
                    total = total + n
                n = n + 1

            print()
            print("Rekap bilangan prima " + str(awal) + ".." + str(akhir) + ":")
            print("Jumlah total bilangan prima :", jumlah, "bilangan")
            print("Hasil penjumlahan nilainya  :", total)

    # =====================================================
    # NOMOR DI LUAR 1-50
    # =====================================================
    else:
        print()
        print("Nomor soal harus antara 1 sampai 50.")

    print()
    print("=============================================")
    print()