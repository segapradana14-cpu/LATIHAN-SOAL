public class StokTidakCukupException extends Exception {
    private static final long serialVersionUID = 1L;
    public StokTidakCukupException(String namaProduk, int diminta, int tersedia) {
        super("Stok " + namaProduk + " tidak cukup (diminta " + diminta
                + ", tersedia " + tersedia + ")");
    }
}
