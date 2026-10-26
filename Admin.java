public class Admin extends Pengguna {

    public Admin(String username, String nama) {
        super(username, nama);
    }

    @Override
    public String getPeran() {
        return "Admin";
    }

    @Override
    public void jalankanMenu(Inventaris inventaris) {
        boolean jalan = true;
        while (jalan) {
            System.out.println("\n--- MENU ADMIN ---");
            System.out.println("1. Lihat produk");
            System.out.println("2. Tambah makanan");
            System.out.println("3. Tambah minuman");
            System.out.println("4. Ubah stok");
            System.out.println("5. Hapus produk");
            System.out.println("0. Kembali");
            int pilih = Util.bacaInt("Pilih: ");

            try {
                switch (pilih) {
                    case 1:
                        inventaris.tampilSemua();
                        break;
                    case 2: {
                        String nama = Util.bacaString("Nama makanan: ");
                        double harga = Util.bacaDouble("Harga: ");
                        int stok = Util.bacaInt("Stok: ");
                        String exp = Util.bacaString("Kedaluwarsa (yyyy-mm-dd): ");
                        inventaris.tambah(new Makanan(nama, harga, stok, exp));
                        System.out.println("Makanan ditambahkan.");
                        break;
                    }
                    case 3: {
                        String nama = Util.bacaString("Nama minuman: ");
                        double harga = Util.bacaDouble("Harga: ");
                        int stok = Util.bacaInt("Stok: ");
                        int ml = Util.bacaInt("Ukuran (ml): ");
                        inventaris.tambah(new Minuman(nama, harga, stok, ml));
                        System.out.println("Minuman ditambahkan.");
                        break;
                    }
                    case 4: {
                        Produk p = inventaris.cariByKode(Util.bacaString("Kode produk: "));
                        if (p == null) {
                            System.out.println("Produk tidak ditemukan.");
                        } else {
                            p.setStok(Util.bacaInt("Stok baru: "));
                            System.out.println("Stok diperbarui.");
                        }
                        break;
                    }
                    case 5:
                        if (inventaris.hapus(Util.bacaString("Kode produk: "))) {
                            System.out.println("Produk dihapus.");
                        } else {
                            System.out.println("Produk tidak ditemukan.");
                        }
                        break;
                    case 0:
                        jalan = false;
                        break;
                    default:
                        System.out.println("Menu tidak valid.");
                }
            } catch (IllegalArgumentException e) {
                System.out.println("Gagal: " + e.getMessage());
            }
        }
    }
}
