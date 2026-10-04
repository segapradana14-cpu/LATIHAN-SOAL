package kalkulator_pbo;

import java.util.Scanner;

public class KALKULATOR_PBO {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.println("=== KALKULATOR SEDERHANA ===");
        System.out.println("1. Penjumlahan");
        System.out.println("2. Pengurangan");
        System.out.println("3. Perkalian");
        System.out.println("4. Pembagian");
        System.out.println("5. Pangkat");
        System.out.print("Pilih operasi (1-5): ");

        // Pastikan input pilihan berupa angka
        if (!input.hasNextInt()) {
            System.out.println("Pilihan tidak valid. Jalankan ulang program.");
            input.close();
            return;
        }
        int pilihan = input.nextInt();

        if (pilihan < 1 || pilihan > 5) {
            System.out.println("Pilihan tidak valid. Jalankan ulang program.");
            input.close();
            return;
        }

        System.out.print("Masukkan angka pertama: ");
        double a = input.nextDouble();
        System.out.print("Masukkan angka kedua: ");
        double b = input.nextDouble();

        switch (pilihan) {
            case 1:
                System.out.println("Hasil: " + a + " + " + b + " = " + (a + b));
                break;
            case 2:
                System.out.println("Hasil: " + a + " - " + b + " = " + (a - b));
                break;
            case 3:
                System.out.println("Hasil: " + a + " * " + b + " = " + (a * b));
                break;
            case 4:
                if (b == 0) {
                    System.out.println("Error: pembagian dengan nol tidak diperbolehkan.");
                } else {
                    System.out.println("Hasil: " + a + " / " + b + " = " + (a / b));
                }
                break;
            case 5:
                System.out.println("Hasil: " + a + " ^ " + b + " = " + Math.pow(a, b));
                break;
        }

        input.close();
    }
}
