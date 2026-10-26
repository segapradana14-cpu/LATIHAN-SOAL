public class Minuman extends Produk {

    private int ukuranMl;

    public Minuman(String nama, double harga, int stok, int ukuranMl) {
        super(nama, harga, stok);
        this.ukuranMl = ukuranMl;
    }

    public int getUkuranMl() { return ukuranMl; }

    @Override
    public double getPersenPajak() {
        return 0.05;
    }

    @Override
    public String getKategori() {
        return "Minuman";
    }

    @Override
    public String toString() {
        return super.toString() + "  " + ukuranMl + "ml";
    }
}
