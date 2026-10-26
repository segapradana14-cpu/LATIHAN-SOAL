public class ItemTransaksi {
    private Produk produk; 
    private int jumlah;

    public ItemTransaksi(Produk produk, int jumlah) {
        this.produk = produk;
        this.jumlah = jumlah;
    }

    public Produk getProduk() { return produk; }
    public int getJumlah() { return jumlah; }

   
    public double getSubtotal() {
        return produk.hitungHarga(jumlah);
    }
}
