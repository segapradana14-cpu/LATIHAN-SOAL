import java.util.ArrayList;

public class Transaksi {

    private static int counter = 0;

    private final String noTransaksi;
    private String namaKasir;
    private ArrayList<ItemTransaksi> items = new ArrayList<>();

    public Transaksi(String namaKasir) {
        counter++;
        this.noTransaksi = String.format("TRX%04d", counter);
        this.namaKasir = namaKasir;
    }

    public String getNoTransaksi() { return noTransaksi; }
    public boolean isKosong() { return items.isEmpty(); }

    public void tambahItem(Produk p, int jumlah) throws StokTidakCukupException {
        if (jumlah <= 0) {
            throw new IllegalArgumentException("Jumlah harus lebih dari 0");
        }
        if (jumlah > p.getStok()) {
            throw new StokTidakCukupException(p.getNama(), jumlah, p.getStok());
        }
        items.add(new ItemTransaksi(p, jumlah));
        p.kurangiStok(jumlah);
    }

    public void batal() {
        for (ItemTransaksi item : items) {
            Produk p = item.getProduk();
            p.setStok(p.getStok() + item.getJumlah());
        }
        items.clear();
    }

    public double hitungTotal() {
        double total = 0;
        for (ItemTransaksi item : items) {
            total += item.getSubtotal();
        }
        return total;
    }

    public void cetakStruk(Pembayaran metode, double uangDiterima) {
        double total = hitungTotal();
        double biaya = metode.hitungBiayaLayanan(total);
        double tagihan = total + biaya;

        System.out.println();
        System.out.println("============== STRUK ==============");
        System.out.println("No Transaksi : " + noTransaksi);
        System.out.println("Kasir        : " + namaKasir);
        System.out.println("-----------------------------------");
        for (ItemTransaksi item : items) {
            System.out.printf("%-14s x%-3d %10s%n",
                    item.getProduk().getNama(), item.getJumlah(),
                    Util.rupiah(item.getSubtotal()));
        }
        System.out.println("-----------------------------------");
        System.out.printf("%-20s %10s%n", "Total (+pajak)", Util.rupiah(total));
        System.out.printf("%-20s %10s%n", "Biaya layanan", Util.rupiah(biaya));
        System.out.printf("%-20s %10s%n", "Tagihan", Util.rupiah(tagihan));
        System.out.printf("%-20s %10s%n", "Metode (" + metode.getMetode() + ")", Util.rupiah(uangDiterima));
        System.out.printf("%-20s %10s%n", "Kembalian", Util.rupiah(uangDiterima - tagihan));
        System.out.println("===================================");
        System.out.println("      Terima kasih, datang lagi!");
    }
}
