public class PembayaranTunai implements Pembayaran {

    @Override
    public String getMetode() {
        return "Tunai";
    }

    @Override
    public double hitungBiayaLayanan(double total) {
        return 0;
    }

    @Override
    public boolean butuhInputUang() {
        return true;
    }

    @Override
    public boolean validasi(double tagihan, double uangDiterima) {
        return uangDiterima >= tagihan;
    }
}
