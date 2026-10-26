public class PembayaranQRIS implements Pembayaran {

    @Override
    public String getMetode() {
        return "QRIS";
    }

    @Override
    public double hitungBiayaLayanan(double total) {
        return total * 0.007;
    }

    @Override
    public boolean butuhInputUang() {
        return false;
    }

    @Override
    public boolean validasi(double tagihan, double uangDiterima) {
        return true;
    }
}
