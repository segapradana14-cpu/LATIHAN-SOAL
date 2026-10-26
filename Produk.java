public abstract class Produk {

    private static int jumlahProduk = 0;

    private final String kode;
    private String nama;
    private double harga;
    private int stok;

    public Produk(String nama, double harga, int stok) {
        jumlahProduk++;
        this.kode = String.format("P%03d", jumlahProduk);
        setNama(nama);
        setHarga(harga);
        setStok(stok);
    }

    public String getKode() { return kode; }
    public String getNama() { return nama; }
    public double getHarga() { return harga; }
    public int getStok() { return stok; }
    public static int getJumlahProduk() { return jumlahProduk; }

    public final void setNama(String nama) {
        if (nama == null || nama.trim().isEmpty()) {
            throw new IllegalArgumentException("Nama produk tidak boleh kosong");
        }
        this.nama = nama;
    }

    public final void setHarga(double harga) {
        if (harga <= 0) {
            throw new IllegalArgumentException("Harga harus lebih dari 0");
        }
        this.harga = harga;
    }

    public final void setStok(int stok) {
        if (stok < 0) {
            throw new IllegalArgumentException("Stok tidak boleh negatif");
        }
        this.stok = stok;
    }

    public abstract double getPersenPajak();
    public abstract String getKategori();

    public double hitungHarga() {
        return hitungHarga(1);
    }

    public double hitungHarga(int jumlah) {
        return harga * jumlah * (1 + getPersenPajak());
    }

    public void kurangiStok(int jumlah) {
        setStok(stok - jumlah);
    }

    @Override
    public String toString() {
        return String.format("[%s] %-14s %-8s %10s  stok: %d",
                kode, nama, getKategori(), Util.rupiah(harga), stok);
    }
}
