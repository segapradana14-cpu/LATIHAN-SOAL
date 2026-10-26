public abstract class Pengguna {
    private String username;
    private String nama;

    public Pengguna(String username, String nama) {
        this.username = username;
        this.nama = nama;
    }

    public String getUsername() { return username; }
    public String getNama() { return nama; }

    public abstract String getPeran();
    public abstract void jalankanMenu(Inventaris inventaris);

    public void tampilSalam() {
        System.out.println("\nHalo, " + nama + " (" + getPeran() + ")");
    }
}
