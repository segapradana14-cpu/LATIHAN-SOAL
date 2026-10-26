import java.util.ArrayList;

public class Kasir extends Pengguna {

    private ArrayList<Transaksi> riwayat = new ArrayList<>();

    public Kasir(String username, String nama) {
        super(username, nama);
    }

    @Override
    public String getPeran() {
        return "Kasir";
    }

    @Override
    public void jalankanMenu(Inventaris inventaris) {
        boolean jalan = true;
        while (jalan) {
            System.out.println("\n--- MENU KASIR ---");
            System.out.println("1. Lihat produk");
            System.out.println("2. Transaksi baru");
            System.out.println("3. Riwayat transaksi");
            System.out.println("0. Kembali");
            int pilih = Util.bacaInt("Pilih: ");

            switch (pilih) {
                case 1:
                    inventaris.tampilSemua();
                    break;
                case 2:
                    transaksiBaru(inventaris);
                    break;
                case 3:
                    tampilRiwayat();
                    break;
                case 0:
                    jalan = false;
                    break;
                default:
                    System.out.println("Menu tidak valid.");
            }
        }
    }

    private void transaksiBaru(Inventaris inventaris) {
        Transaksi trx = new Transaksi(getNama());

        while (true) {
            inventaris.tampilSemua();
            String kode = Util.bacaString("Kode produk (kosong = selesai): ");
            if (kode.isEmpty()) {
                break;
            }
            Produk p = inventaris.cariByKode(kode);
            if (p == null) {
                System.out.println("Produk tidak ditemukan.");
                continue;
            }
            int jumlah = Util.bacaInt("Jumlah: ");
            try {
                trx.tambahItem(p, jumlah);
                System.out.println("Ditambahkan ke keranjang.");
            } catch (StokTidakCukupException e) {
                System.out.println("Gagal: " + e.getMessage());
            } catch (IllegalArgumentException e) {
                System.out.println("Gagal: " + e.getMessage());
            }
        }

        if (trx.isKosong()) {
            System.out.println("Keranjang kosong, transaksi dibatalkan.");
            return;
        }

        System.out.println("Total belanja: " + Util.rupiah(trx.hitungTotal()));
        System.out.println("Metode bayar: 1. Tunai  2. QRIS");
        int pilihBayar = Util.bacaInt("Pilih: ");

        Pembayaran metode;
        if (pilihBayar == 2) {
            metode = new PembayaranQRIS();
        } else {
            metode = new PembayaranTunai();
        }

        double tagihan = trx.hitungTotal() + metode.hitungBiayaLayanan(trx.hitungTotal());
        System.out.println("Tagihan (termasuk biaya layanan): " + Util.rupiah(tagihan));

        double uang = tagihan;
        if (metode.butuhInputUang()) {
            uang = Util.bacaDouble("Uang diterima: ");
        }

        if (!metode.validasi(tagihan, uang)) {
            System.out.println("Uang kurang. Transaksi dibatalkan.");
            trx.batal();
            return;
        }

        trx.cetakStruk(metode, uang);
        riwayat.add(trx);
    }

    private void tampilRiwayat() {
        if (riwayat.isEmpty()) {
            System.out.println("Belum ada transaksi.");
            return;
        }
        for (Transaksi t : riwayat) {
            System.out.println(t.getNoTransaksi() + "  total: " + Util.rupiah(t.hitungTotal()));
        }
    }
}
