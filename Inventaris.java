import java.util.ArrayList;

public class Inventaris {
    
    private ArrayList<Produk> daftar = new ArrayList<>();
    
    public void tambah(Produk p) {
        daftar.add(p);
    }

    public Produk cariByKode(String kode) {
        for (Produk p : daftar) {
            if (p.getKode().equalsIgnoreCase(kode)) {
                return p;
            }
        }
        return null;
    }

    public boolean hapus(String kode) {
        Produk p = cariByKode(kode);
        if (p == null) {
            return false;
        }
        return daftar.remove(p);
    }

    public void tampilSemua() {
        if (daftar.isEmpty()) {
            System.out.println("(belum ada produk)");
            return;
        }
        System.out.println("---------------- DAFTAR PRODUK ----------------");
        for (Produk p : daftar) {
            System.out.println(p);  
        }
        System.out.println("-----------------------------------------------");
    }
}
