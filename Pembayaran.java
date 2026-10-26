public interface Pembayaran {
    String getMetode();
    double hitungBiayaLayanan(double total);
    boolean butuhInputUang();
    boolean validasi(double tagihan, double uangDiterima);
}
