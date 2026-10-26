public class Makanan extends Produk {

    private String kedaluwarsa;

    public Makanan(String nama, double harga, int stok, String kedaluwarsa) {
        super(nama, harga, stok);
        this.kedaluwarsa = kedaluwarsa;
    }

    public String getKedaluwarsa() { return kedaluwarsa; }

    @Override
    public double getPersenPajak() {
        return 0.10;
    }

    @Override
    public String getKategori() {
        return "Makanan";
    }

    @Override
    public String toString() {
        return super.toString() + "  exp: " + kedaluwarsa;
    }
}
